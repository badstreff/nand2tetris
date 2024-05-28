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
// function Class1.set 0 - Class1
(Class1.set)
// push argument 0 - Class1
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
// pop static 0 - Class1
@Class1.0
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
// push argument 1 - Class1
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
// pop static 1 - Class1
@Class1.1
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
// push constant 0 - Class1
@0
D=A
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
// function Class1.get 0 - Class1
(Class1.get)
// push static 0 - Class1
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1 - Class1
@Class1.1
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
@R14
A=M
0;JMP
// function Class2.set 0 - Class2
(Class2.set)
// push argument 0 - Class2
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
// pop static 0 - Class2
@Class2.0
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
// push argument 1 - Class2
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
// pop static 1 - Class2
@Class2.1
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
// push constant 0 - Class2
@0
D=A
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
// function Class2.get 0 - Class2
(Class2.get)
// push static 0 - Class2
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static 1 - Class2
@Class2.1
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
@R14
A=M
0;JMP
// function Sys.init 0 - Sys
(Sys.init)
// push constant 6 - Sys
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 8 - Sys
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class1.set 2 - Sys
@Class1.set$ret.10 // push returnAddr
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
@2
D=D-A
@ARG
M=D
@SP // LCL = SP - reposition lcl
D=M
@LCL
M=D
// goto function
@Class1.set
0;JMP
(Class1.set$ret.10) // (return address) generate label
// pop temp 0 - Sys
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
// push constant 23 - Sys
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 15 - Sys
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Class2.set 2 - Sys
@Class2.set$ret.14 // push returnAddr
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
@2
D=D-A
@ARG
M=D
@SP // LCL = SP - reposition lcl
D=M
@LCL
M=D
// goto function
@Class2.set
0;JMP
(Class2.set$ret.14) // (return address) generate label
// pop temp 0 - Sys
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
// call Class1.get 0 - Sys
@Class1.get$ret.16 // push returnAddr
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
@Class1.get
0;JMP
(Class1.get$ret.16) // (return address) generate label
// call Class2.get 0 - Sys
@Class2.get$ret.17 // push returnAddr
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
@Class2.get
0;JMP
(Class2.get$ret.17) // (return address) generate label
// label END - Sys
(Sys.END)
// goto END - Sys
@Sys.END
0;JMP
