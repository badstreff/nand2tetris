// pop argument 1 - FibonacciSeries
@1
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1 - FibonacciSeries
@4
D=A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// pop constant 0 - FibonacciSeries
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 0 - FibonacciSeries
@0
D=A
@THAT
A=M
A=A+D
D=A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// pop constant 1 - FibonacciSeries
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 1 - FibonacciSeries
@1
D=A
@THAT
A=M
A=A+D
D=A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// pop argument 0 - FibonacciSeries
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop constant 2 - FibonacciSeries
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop argument 0 - FibonacciSeries
@0
D=A
@ARG
A=M
A=A+D
D=A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// label LOOP - FibonacciSeries
(FibonacciSeries.LOOP)
// pop argument 0 - FibonacciSeries
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// if-goto COMPUTE_ELEMENT - FibonacciSeries
@SP
AM=M-1
D=M
@FibonacciSeries.COMPUTE_ELEMENT
D;JNE
// goto END - FibonacciSeries
@FibonacciSeries.END
0;JMP
// label COMPUTE_ELEMENT - FibonacciSeries
(FibonacciSeries.COMPUTE_ELEMENT)
// pop that 0 - FibonacciSeries
@0
D=A
@THAT
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop that 1 - FibonacciSeries
@1
D=A
@THAT
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D+M
@SP
A=M
M=D
@SP
M=M+1
// pop that 2 - FibonacciSeries
@2
D=A
@THAT
A=M
A=A+D
D=A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// pop pointer 1 - FibonacciSeries
@4
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop constant 1 - FibonacciSeries
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D+M
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1 - FibonacciSeries
@4
D=A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// pop argument 0 - FibonacciSeries
@0
D=A
@ARG
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop constant 1 - FibonacciSeries
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
AM=M-1
D=M
@SP
AM=M-1
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop argument 0 - FibonacciSeries
@0
D=A
@ARG
A=M
A=A+D
D=A
@R13
M=D
@SP
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D
// goto LOOP - FibonacciSeries
@FibonacciSeries.LOOP
0;JMP
// label END - FibonacciSeries
(FibonacciSeries.END)
