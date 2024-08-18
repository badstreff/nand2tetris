# Stage One
Stage 1: Symbol Table: Start by building the compiler’s SymbolTable module, and use it for
extending the syntax analyzer built in Project 10, as follows. Presently, whenever an identifier is
encountered in the source code, say foo, the syntax analyzer outputs the XML line <identifier> foo
</identifier>. Extend your analyzer to output the following information about each identifier:
name;
category (field, static, local, arg, class, subroutine);
index: if the identifier’s category is field, static, local, or arg,
the running index assigned to the identifier by the symbol table;
usage: whether the identifier is presently being declared (in a static / field / var variable declaration,
or in a parameter list), or used (in an expression).

Have your syntax analyzer output this information as part of its XML output, using markup tags of
your choice.
Test your new SymbolTable module and the new functionality just described by running your
extended syntax analyzer on the test Jack programs supplied in project 10. If your extended syntax
analyzer is capable of outputting the information described above, it means that you've developed
a complete executable capability to understand the semantics of Jack programs. At this stage you
www.nand2tetris.org / Copyright © Noam Nisan and Shimon Schocken

can make the switch to developing the full-scale compiler, and start generating VM code instead of
XML output. This can be done gradually, as we now turn to describe.
Stage 1.5: Make a back-up copy of the extended syntax analyzer code.

# Stage Two
Stage 2: Code Generation: We provide six Jack programs, designed to gradually unit-test the code
generation capabilities of your compiler. We advise to develop, and test, your evolving compiler on
the test programs in the order given below. This way, you will be implicitly guided to build the
compiler’s code generation capabilities in sensible stages, according to the demands presented by
each test program.
Normally, when one compiles a high-level program and runs into some difficulties, one concludes
that the program is screwed up. In this project the setting is exactly the opposite. All the supplied
test programs are error-free. Therefore, if their compilation yields any errors, it’s the compiler that
you have to fix, not the programs. Specifically, for each test program, we recommend going
through the following routine:
1. Compile the program folder using the compiler that you are developing. This action should
generate one .vm file for each source .jack file in the given folder.
2. Inspect the generated VM files. If there are visible problems, fix your compiler and go to step 1.
Remember: All the supplied test programs are error-free.
3. Load the program folder into the emulator, and run the loaded code. Note that each one of the
six supplied test programs contains specific execution guidelines; test the compiled program
(translated VM code) according to these guidelines.
4. If the program behaves unexpectedly, or some error message is displayed by the VM emulator,
fix your compiler and go to step 1.


# Test Order
Seven
ConvertToBin
Square
Average
Pong
ComplexArray