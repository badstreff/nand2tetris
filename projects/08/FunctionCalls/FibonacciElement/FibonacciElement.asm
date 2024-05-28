@256
D=A
@SP
M=D
// call Sys.init 0 - init
@Sys.init$ret.0 // push returnAddr
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nArgs reposition arg
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP // LCL = SP - reposition lcl
D=M
@LCL
M=D
// goto function
@Sys.init
0;JMP
(Sys.init$ret.0) // (return address) generate label
// function Main.fibonacci 0 - FibonacciElement
(Main.fibonacci)
// push argument 0 - FibonacciElement
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
// push constant 2 - FibonacciElement
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
AM=M-1
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE24f4a422-31e0-4820-ad46-6eb5977ed20d
D;JLT
@SP
A=M
M=0
@CONTINUE24f4a422-31e0-4820-ad46-6eb5977ed20d
0;JMP
(TRUE24f4a422-31e0-4820-ad46-6eb5977ed20d)
@SP
A=M
M=-1
(CONTINUE24f4a422-31e0-4820-ad46-6eb5977ed20d)
@SP
M=M+1
// if-goto N_LT_2 - FibonacciElement
@SP
AM=M-1
D=M
@FibonacciElement.N_LT_2
D;JNE
// goto N_GE_2 - FibonacciElement
@FibonacciElement.N_GE_2
0;JMP
// label N_LT_2 - FibonacciElement
(FibonacciElement.N_LT_2)
// push argument 0 - FibonacciElement
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
// return
@LCL
D=M
@R13 // Store LCL
M=D
@5
D=D-A
A=D
A=M
D=A
@R14 // Store retAddr
M=D
@SP // Move return value to *ARG
AM=M-1
D=M
@ARG
A=M
M=D
@ARG // Set SP to ARG+1
A=M
D=A+1
@SP
M=D
@R13  // Restore THAT
A=M
A=A-1
D=M
@THAT
M=D
@2  // Restore THIS
D=A
@R13
A=M
A=A-D
D=M
@THIS
M=D
@3  // Restore ARG
D=A
@R13
A=M
A=A-D
D=M
@ARG
M=D
@4  // Restore LCL
D=A
@R13
A=M
A=A-D
D=M
@LCL
M=D
@R14
A=M
0;JMP
// label N_GE_2 - FibonacciElement
(FibonacciElement.N_GE_2)
// push argument 0 - FibonacciElement
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
// push constant 2 - FibonacciElement
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
// call Main.fibonacci 1 - FibonacciElement
@Main.fibonacci$ret.23 // push returnAddr
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nArgs reposition arg
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP // LCL = SP - reposition lcl
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.23) // (return address) generate label
// push argument 0 - FibonacciElement
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
// push constant 1 - FibonacciElement
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
// call Main.fibonacci 1 - FibonacciElement
@Main.fibonacci$ret.27 // push returnAddr
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nArgs reposition arg
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP // LCL = SP - reposition lcl
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.27) // (return address) generate label
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
// return
@LCL
D=M
@R13 // Store LCL
M=D
@5
D=D-A
A=D
A=M
D=A
@R14 // Store retAddr
M=D
@SP // Move return value to *ARG
AM=M-1
D=M
@ARG
A=M
M=D
@ARG // Set SP to ARG+1
A=M
D=A+1
@SP
M=D
@R13  // Restore THAT
A=M
A=A-1
D=M
@THAT
M=D
@2  // Restore THIS
D=A
@R13
A=M
A=A-D
D=M
@THIS
M=D
@3  // Restore ARG
D=A
@R13
A=M
A=A-D
D=M
@ARG
M=D
@4  // Restore LCL
D=A
@R13
A=M
A=A-D
D=M
@LCL
M=D
@R14
A=M
0;JMP
// function Sys.init 0 - FibonacciElement
(Sys.init)
// push constant 4 - FibonacciElement
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1 - FibonacciElement
@Main.fibonacci$ret.13 // push returnAddr
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nArgs reposition arg
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP // LCL = SP - reposition lcl
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.13) // (return address) generate label
// label END - FibonacciElement
(FibonacciElement.END)
// goto END - FibonacciElement
@FibonacciElement.END
0;JMP
