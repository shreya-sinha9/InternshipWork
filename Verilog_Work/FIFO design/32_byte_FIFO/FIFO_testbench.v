`timescale 1ns / 1ps

////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer:
//
// Create Date:   20:48:18 06/23/2020
// Design Name:   FIFO
// Module Name:   C:/Users/Shreya Sinha/Verilog/FIFO_testbench.v
// Project Name:  Verilog
// Target Device:  
// Tool versions:  
// Description: 
//
// Verilog Test Fixture created by ISE for module: FIFO
//
// Dependencies:
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
////////////////////////////////////////////////////////////////////////////////

module FIFO_testbench;

	// Inputs
	reg rst;
	reg clk;
	reg wr_en;
	reg rd_en;
	reg [7:0] data_in;

	// Outputs
	wire [7:0] data_out;
	wire buf_empty;
	wire buf_full;
	wire [6:0] counter;

	// Instantiate the Unit Under Test (UUT)
	FIFO uut (
		.rst(rst), 
		.clk(clk), 
		.wr_en(wr_en), 
		.rd_en(rd_en), 
		.data_in(data_in), 
		.data_out(data_out), 
		.buf_empty(buf_empty), 
		.buf_full(buf_full), 
		.counter(counter)
	);

	initial begin
		// Initialize Inputs
		rst = 0;
		clk = 0;
		wr_en = 0;
		rd_en = 0;
		data_in = 0;

		// Wait 100 ns for global reset to finish
		#100;
        
		// Add stimulus here
      rst = 1'b1;
		#20;
		rst = 1'b0;
		wr_en = 1'b1;
		data_in = 8'h0;
		#20;
		data_in = 8'h1;
		#20;
		data_in = 8'h2;
		#20;
		data_in = 8'h3;
		#20;
		data_in = 8'h4;
		#20;
		data_in = 8'h5;
		#20;
		data_in = 8'h6;
		#20;
		data_in = 8'h7;
		#20;
		data_in = 8'h8;
		#20;
		data_in = 8'h9;
		#20;
		data_in = 8'hA;
		#20;
		data_in = 8'hB;
		#20;
		data_in = 8'hC;
		#20;
		data_in = 8'hD;
		#20;
		data_in = 8'hE;
		#20;
		wr_en = 1'b0;
		rd_en = 1'b1;
		
	end
        always #10 clk = ~clk;   
endmodule

