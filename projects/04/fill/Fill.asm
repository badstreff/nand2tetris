// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

//// Replace this comment with your code.


// Screen The Hack computer includes a black-and-white screen organized as 256
// rows of 512 pixels per row. The screen’s contents are represented by an 8K memory
// map that starts at RAM address 16384 (0x4000). Each row in the physical screen,
// starting at the screen’s top left corner, is represented in the RAM by 32 consecu-
// tive 16-bit words. Thus the pixel at row r from the top and column c from the left
// is mapped on the c%16 bit (counting from LSB to MSB) of the word located at
// RAM[16384 þ r  32 þ c=16]. To write or read a pixel of the physical screen, one
// reads or writes the corresponding bit in the RAM-resident memory map (1 ¼ black,
// 0 ¼ white). Example:

(START)
@KBD
D=M

@SETCLEAR
D;JEQ

(SETFILL)
@R0
M=-1
@FILL
0;JMP

(SETCLEAR)
@R0
M=0
@FILL
0;JMP

// Draw a single black dot at the screen's top left corner:
(FILL) // Fill screen with value in R0
@i
M=0

(LOOP)
@i
D=M
@8192
D=D-A

@START
D;JEQ

@SCREEN
D=A
@i
A=M+D
D=A
@offset
M=D
@R0
D=M
@offset
A=M
M=D

// A=D
// M=-1

// i++
@i
D=M
M=D+1

@LOOP
0;JMP
