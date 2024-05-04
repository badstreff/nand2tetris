
@17
D=A

@SP
A=M
M=D
@SP
M=M+1


@17
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
@TRUE03d71ea9-ade1-4e9f-ae93-d953127dba9a
D;JEQ

// Save false onto stack
@SP
A=M
M=0
@CONTINUE03d71ea9-ade1-4e9f-ae93-d953127dba9a
0;JMP

// save true onto stack
(TRUE03d71ea9-ade1-4e9f-ae93-d953127dba9a)
@SP
A=M
M=-1

(CONTINUE03d71ea9-ade1-4e9f-ae93-d953127dba9a)
// Increment stack
@SP
M=M+1


@17
D=A

@SP
A=M
M=D
@SP
M=M+1


@16
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
@TRUE901146cb-bcd3-4f2c-912a-a581c0a6a644
D;JEQ

// Save false onto stack
@SP
A=M
M=0
@CONTINUE901146cb-bcd3-4f2c-912a-a581c0a6a644
0;JMP

// save true onto stack
(TRUE901146cb-bcd3-4f2c-912a-a581c0a6a644)
@SP
A=M
M=-1

(CONTINUE901146cb-bcd3-4f2c-912a-a581c0a6a644)
// Increment stack
@SP
M=M+1


@16
D=A

@SP
A=M
M=D
@SP
M=M+1


@17
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
@TRUEf13183cd-7ec7-44d2-a321-e358f20fc2e9
D;JEQ

// Save false onto stack
@SP
A=M
M=0
@CONTINUEf13183cd-7ec7-44d2-a321-e358f20fc2e9
0;JMP

// save true onto stack
(TRUEf13183cd-7ec7-44d2-a321-e358f20fc2e9)
@SP
A=M
M=-1

(CONTINUEf13183cd-7ec7-44d2-a321-e358f20fc2e9)
// Increment stack
@SP
M=M+1


@892
D=A

@SP
A=M
M=D
@SP
M=M+1


@891
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
@TRUEad75eadc-df5d-425e-9618-fad11e989ab1
D;JLT
// Save false onto stack
@SP
A=M
M=0
@CONTINUEad75eadc-df5d-425e-9618-fad11e989ab1
0;JMP
// save true onto stack
(TRUEad75eadc-df5d-425e-9618-fad11e989ab1)
@SP
A=M
M=-1
(CONTINUEad75eadc-df5d-425e-9618-fad11e989ab1)
// Increment stack
@SP
M=M+1


@891
D=A

@SP
A=M
M=D
@SP
M=M+1


@892
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
@TRUE5cc56046-1f21-4f1d-860e-a1b55dc4564d
D;JLT
// Save false onto stack
@SP
A=M
M=0
@CONTINUE5cc56046-1f21-4f1d-860e-a1b55dc4564d
0;JMP
// save true onto stack
(TRUE5cc56046-1f21-4f1d-860e-a1b55dc4564d)
@SP
A=M
M=-1
(CONTINUE5cc56046-1f21-4f1d-860e-a1b55dc4564d)
// Increment stack
@SP
M=M+1


@891
D=A

@SP
A=M
M=D
@SP
M=M+1


@891
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
@TRUE2f88c71a-5b02-486a-8bfd-71617efd8414
D;JLT
// Save false onto stack
@SP
A=M
M=0
@CONTINUE2f88c71a-5b02-486a-8bfd-71617efd8414
0;JMP
// save true onto stack
(TRUE2f88c71a-5b02-486a-8bfd-71617efd8414)
@SP
A=M
M=-1
(CONTINUE2f88c71a-5b02-486a-8bfd-71617efd8414)
// Increment stack
@SP
M=M+1


@32767
D=A

@SP
A=M
M=D
@SP
M=M+1


@32766
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
@TRUE0302133e-537e-4c21-9550-349f7c02d08e
D;JGT
// Save false onto stack
@SP
A=M
M=0
@CONTINUE0302133e-537e-4c21-9550-349f7c02d08e
0;JMP
// save true onto stack
(TRUE0302133e-537e-4c21-9550-349f7c02d08e)
@SP
A=M
M=-1
(CONTINUE0302133e-537e-4c21-9550-349f7c02d08e)
// Increment stack
@SP
M=M+1


@32766
D=A

@SP
A=M
M=D
@SP
M=M+1


@32767
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
@TRUEe17ac1fa-950d-40bb-8c8b-75c75446cf76
D;JGT
// Save false onto stack
@SP
A=M
M=0
@CONTINUEe17ac1fa-950d-40bb-8c8b-75c75446cf76
0;JMP
// save true onto stack
(TRUEe17ac1fa-950d-40bb-8c8b-75c75446cf76)
@SP
A=M
M=-1
(CONTINUEe17ac1fa-950d-40bb-8c8b-75c75446cf76)
// Increment stack
@SP
M=M+1


@32766
D=A

@SP
A=M
M=D
@SP
M=M+1


@32766
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
@TRUEc8c851ed-4e94-48c4-93ab-161ab2df63c9
D;JGT
// Save false onto stack
@SP
A=M
M=0
@CONTINUEc8c851ed-4e94-48c4-93ab-161ab2df63c9
0;JMP
// save true onto stack
(TRUEc8c851ed-4e94-48c4-93ab-161ab2df63c9)
@SP
A=M
M=-1
(CONTINUEc8c851ed-4e94-48c4-93ab-161ab2df63c9)
// Increment stack
@SP
M=M+1


@57
D=A

@SP
A=M
M=D
@SP
M=M+1


@31
D=A

@SP
A=M
M=D
@SP
M=M+1


@53
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


@112
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


@SP
M=M-1
A=M
M=-M
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
D=D&M
// Save value onto stack
@SP
A=M
M=D
// Increment stack
@SP
M=M+1


@82
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
D=D|M
// Save value onto stack
@SP
A=M
M=D
// Increment stack
@SP
M=M+1


@SP
M=M-1
A=M
M=!M
@SP
M=M+1

