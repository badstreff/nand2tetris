
@0
D=A

@SP
A=M
M=D
@SP
M=M+1

@0
D=A
@LCL
A=M
A=A+D
D=A
// [R13] == Addr
@R13
M=D
// Decrement stack
@SP
M=M-1
// Store value from stack in D
@SP
A=M
D=M
// Set memory to value from the stack
@R13
A=M
M=D

(BasicLoop.LOOP)


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


// D == first argument
@SP
M=M-1
A=M
D=M
// Do Addition
@SP
M=M-1
A=M
D=D+M
// Save value onto stack
@SP
A=M
M=D
// Increment stack
@SP
M=M+1

@0
D=A
@LCL
A=M
A=A+D
D=A
// [R13] == Addr
@R13
M=D
// Decrement stack
@SP
M=M-1
// Store value from stack in D
@SP
A=M
D=M
// Set memory to value from the stack
@R13
A=M
M=D

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


@1
D=A

@SP
A=M
M=D
@SP
M=M+1


// D == first argument
@SP
M=M-1
A=M
D=M
// Do Subtraction
@SP
M=M-1
A=M
D=M-D
// Save value onto stack
@SP
A=M
M=D
// Increment stack
@SP
M=M+1

@0
D=A
@ARG
A=M
A=A+D
D=A
// [R13] == Addr
@R13
M=D
// Decrement stack
@SP
M=M-1
// Store value from stack in D
@SP
A=M
D=M
// Set memory to value from the stack
@R13
A=M
M=D

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


@SP
AM=M-1
D=M
@BasicLoop.LOOP
D;JNE


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

