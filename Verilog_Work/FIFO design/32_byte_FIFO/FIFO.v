`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    20:02:45 06/23/2020 
// Design Name: 
// Module Name:    FIFO 
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
module FIFO(
    input rst,
    input clk,
    input wr_en,
    input rd_en,
    input [7:0] data_in,
    output [7:0] data_out,
    output buf_empty,
    output buf_full,
    output [6:0] counter
    );
reg[7:0] data_out;
reg buf_empty, buf_full;
reg[6:0] counter;
reg[5:0] rd_ptr,wr_ptr;
reg[7:0] buf_mem[31:0];

//gives the status flag empty and full
always@(counter)begin
   buf_empty = (counter==0);
   buf_full = (counter==32);
end

//set the fifo counter
always@(posedge clk or posedge rst)begin
   if(rst)
        counter <= 0;
	else if( (!buf_full && wr_en) && ( !buf_empty && rd_en))	//we do not update the counter when we are both reading and writing	 
        counter <= counter;
	else if( !buf_full && wr_en )
	     counter <= counter + 1;
   else if( !buf_empty && rd_en)
	     counter <= counter -1;
	else
	     counter <= counter;
end

//to fetch the data from fifo
always @(posedge clk or posedge rst)begin
    if(rst)
	     data_out <= 0;
	 else begin
	     if(rd_en && !buf_empty )
		     data_out <= buf_mem[rd_ptr];
		  else
		      data_out <= data_out;
	 end
end

//to write data into the fifo
always @(posedge clk)begin
     if(wr_en && !buf_full )
	     buf_mem[wr_ptr] <= data_in;
	  else
	     buf_mem[wr_ptr] <=  buf_mem[wr_ptr];
end

//to manage pointers
always @(posedge clk or posedge rst)begin
      if(rst)begin
           wr_ptr <= 0;
           rd_ptr <= 0;
      end
      else begin
          if(!buf_full && wr_en )
             wr_ptr <= wr_ptr + 1;
          else
              wr_ptr <= wr_ptr;
          if(!buf_empty && rd_en)
              rd_ptr <= rd_ptr + 1;
          else
               rd_ptr <= rd_ptr;
      end
end		
endmodule
