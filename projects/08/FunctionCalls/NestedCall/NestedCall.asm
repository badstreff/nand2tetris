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
// function Sys.init 0 - NestedCall
(Sys.init)
// push constant 4000 - NestedCall
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0 - NestedCall
@3
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
// push constant 5000 - NestedCall
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1 - NestedCall
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
// call Sys.main 0 - NestedCall
@Sys.main$ret.12 // push returnAddr
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
@Sys.main
0;JMP
(Sys.main$ret.12) // (return address) generate label
// pop temp 1 - NestedCall
@6
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
// label LOOP - NestedCall
(NestedCall.LOOP)
// goto LOOP - NestedCall
@NestedCall.LOOP
0;JMP
// function Sys.main 5 - NestedCall
(Sys.main)
// push constant 0 - NestedCall
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0 - NestedCall
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0 - NestedCall
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0 - NestedCall
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 0 - NestedCall
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 4001 - NestedCall
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0 - NestedCall
@3
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
// push constant 5001 - NestedCall
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1 - NestedCall
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
// push constant 200 - NestedCall
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 1 - NestedCall
@1
D=A
@LCL
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
// push constant 40 - NestedCall
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 2 - NestedCall
@2
D=A
@LCL
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
// push constant 6 - NestedCall
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 3 - NestedCall
@3
D=A
@LCL
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
// push constant 123 - NestedCall
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Sys.add12 1 - NestedCall
@Sys.add12$ret.35 // push returnAddr
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
@Sys.add12
0;JMP
(Sys.add12$ret.35) // (return address) generate label
// pop temp 0 - NestedCall
@5
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
// push local 0 - NestedCall
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
// push local 1 - NestedCall
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
// push local 2 - NestedCall
@2
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
// push local 3 - NestedCall
@3
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
// push local 4 - NestedCall
@4
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
// function Sys.add12 0 - NestedCall
(Sys.add12)
// push constant 4002 - NestedCall
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0 - NestedCall
@3
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
// push constant 5002 - NestedCall
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1 - NestedCall
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
// push argument 0 - NestedCall
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
// push constant 12 - NestedCall
@12
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
