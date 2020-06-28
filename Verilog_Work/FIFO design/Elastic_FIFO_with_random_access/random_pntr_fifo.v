`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:29:52 06/26/2020 
// Design Name: 
// Module Name:    random_pntr_fifo 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module random_pntr_fifo#(
    parameter depth = 32,
    parameter width = 8,
    parameter log2_depth = $clog2(depth)
    )
	 (input rst,
    input clk,
    input wr_en,
    input rd_en,
    input [width-1:0] data_in,
    output reg[width-1:0] data_out,
    output reg buf_empty,
    output reg buf_full,
    output reg [log2_depth:0] counter
    );

reg[log2_depth-1:0] rd_ptr,wr_ptr;
reg[width-1:0] buf_mem[depth-1:0];
reg temp1 = 0;
reg temp2 = 0;
reg buf_data;
reg flag_data[depth-1:0];
//gives the status flag empty and full
always@(counter)begin
   buf_empty = (counter==0);
   buf_full = (counter==depth);
end

//set the fifo counter
always@(posedge clk or posedge rst)begin
   if(rst)
        counter <= 0;
	else if( (!buf_full && wr_en) && ( !buf_empty && rd_en && buf_data))//(buf_mem[rd_ptr]===8'hxx)))	//we do not update the counter when we are both reading and writing	 
        counter <= counter;
	else if( !buf_full && wr_en )
	     counter <= counter + 1;
   else if( !buf_empty && rd_en && buf_data)//(buf_mem[rd_ptr]=== 8'hxx))
	     counter <= counter -1;
	else
	     counter <= counter;
end

//to fetch the data from fifo
always @(posedge clk or posedge rst)begin
    if(rst)
	     data_out <= 0;
	 else begin
	     if(rd_en && !buf_empty && buf_data)//(buf_mem[rd_ptr]=== 8'hxx))
		     data_out <= buf_mem[rd_ptr];
		  else
		      data_out <= data_out;
	 end
end

//to write data into the fifo
always @(posedge clk)begin
     if(wr_en && !buf_full )begin
	     buf_mem[wr_ptr] <= data_in;
		  flag_data[wr_ptr] <= 1;
		  end
	  else
	     buf_mem[wr_ptr] <=  buf_mem[wr_ptr];
		  
end

//to manage pointers
always @(posedge clk or posedge rst)begin
      if(rst)begin
           wr_ptr = 0;
           rd_ptr = 0;
			  
      end
      else begin		
          wr_ptr = {$random}%(depth);
		    rd_ptr = {$random}%(depth);
			 while(wr_ptr==temp1)begin
			    wr_ptr = {$random}%(depth);
				 end
			 temp1 = wr_ptr;
			 
			 while(rd_ptr==temp2)begin
			    rd_ptr = {$random}%(depth);
				 end
			 temp2 = rd_ptr;
			 buf_data = (flag_data[rd_ptr]==1);
          			 
			 
      end
end		
endmodule

