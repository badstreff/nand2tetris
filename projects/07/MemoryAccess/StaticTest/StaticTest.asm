
@111
D=A

@SP
A=M
M=D
@SP
M=M+1


@333
D=A

@SP
A=M
M=D
@SP
M=M+1


@888
D=A

@SP
A=M
M=D
@SP
M=M+1

@static8
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
@static3
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
@static1
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

@static3
D=M

@SP
A=M
M=D
@SP
M=M+1


@static1
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


@static8
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

