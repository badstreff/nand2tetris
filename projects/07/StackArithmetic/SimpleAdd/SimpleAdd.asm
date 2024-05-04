
@7
D=A

@SP
A=M
M=D
@SP
M=M+1


@8
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

