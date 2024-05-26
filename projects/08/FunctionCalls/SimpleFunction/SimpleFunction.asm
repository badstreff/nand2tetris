// function SimpleFunction.test 2 - SimpleFunction
// push constant 0 - SimpleFunction
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0 - SimpleFunction
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local 0 - SimpleFunction
@0
D=A
@LCL
A=M
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 1 - SimpleFunction
@1
D=A
@LCL
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
// not
@SP
M=M-1
A=M
M=!M
@SP
M=M+1
// push argument 0 - SimpleFunction
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
// push argument 1 - SimpleFunction
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
// @R14
// 0;JMP
