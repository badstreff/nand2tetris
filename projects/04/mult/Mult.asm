// Mult.asm (example of an arithmetic task): The inputs of this program are the values stored in R0
// and R1 (RAM[0] and RAM[1]). The program computes the product R0 * R1 and stores the result in
// R2 (RAM[2]). Assume that R0 ≥ 0, R1 ≥ 0, and R0 * R1 < 32768 (your program need not test these
// conditions). Your code should not change the values of R0 and R1. The supplied Mult.test script
// and Mult.cmp compare file are designed to test your program on the CPU emulator, using some
// representative R0 and R1 values.

// i = 0
@i
M=0
// return value = 0
@R2
M=0


(LOOP)
// if i - R0 == 0 
@i
D=M
@R0
D=D-M
@END
D;JEQ

// R2 = R1 + R2
@R2
D=M
@R1
D=D+M
@R2
M=D

// i++
@i
D=M
M=D+1

@LOOP
0;JMP 


(END)
@END
0;JMP // Infinite loop
