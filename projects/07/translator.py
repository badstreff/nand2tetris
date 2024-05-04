"""
7.4.3    Design Suggestions for the VM Implementation
 Usage: The VM translator accepts a single command-line argument, as
 follows:
 prompt> VMTranslator source
 where source is a file name of the form ProgName.vm. The file name may
 contain a file path. If no path is specified, the VM translator operates on the
 current folder. The first character in the file name must be an uppercase
 letter, and the vm extension is mandatory. The file contains a sequence of
 one or more VM commands. In response, the translator creates an output
 file, named ProgName.asm, containing the assembly instructions that realize
 the VM commands. The output file ProgName.asm is stored in the same
 folder as that of the input. If the file ProgName.asm already exists, it will be
 overwritten.

 Program Structure

 We propose implementing the VM translator using three modules: a main
 program called VMTranslator, a Parser, and a CodeWriter. The Parser’s job is to
make sense out of each VM command, that is, understand what the

 command seeks to do. The CodeWriter’s job is to translate the understood VM
 command into assembly instructions that realize the desired operation on
 the Hack platform. The VMTranslator drives the translation process.
"""

import argparse, uuid
from abc import ABC, abstractmethod
from io import TextIOWrapper

SEGMENT_TABLE = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}


class Command(ABC):
    @abstractmethod
    def toasm(self):
        raise NotImplementedError


class Push(Command):
    '''
        push the value from the memory segment onto the stack
    '''
    def __init__(self, args: list[str]):
        self.segment = args[0]
        self.value = int(args[1])

    def toasm(self) -> str:
        # first set D equal to the value we want to push
        if self.segment == "constant":
            asm = f"""
            @{self.value}
            D=A
            """
        elif self.segment == "temp":
            asm = f"""
            @{self.value + 5}
            D=M
            """
        elif self.segment == "pointer":
            asm = f"""
            @{self.value + 3}
            D=M
            """
        elif self.segment == "static":
            asm = f"""
            @static{self.value}
            D=M
            """
        else:
            asm = f"""
            @{self.value}
            D=A
            @{SEGMENT_TABLE[self.segment]}
            A=M
            A=A+D
            D=M
            """
        asm += f"""
            @SP
            A=M
            M=D
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n")])


class Pop(Command):
    def __init__(self, args: list[str]):
        self.segment = args[0]
        self.value = int(args[1])

    def toasm(self) -> str:
        if self.segment == "temp":
            asm = f"""
            @{self.value + 5}
            D=A
            """
        elif self.segment == "pointer":
            asm = f"""
            @{self.value + 3}
            D=A
            """
        elif self.segment == "static":
            asm = f"""
            @static{self.value}
            D=A
            """
        else:
            asm = f"""
                @{self.value}
                D=A
                @{SEGMENT_TABLE[self.segment]}
                A=M
                A=A+D
                D=A
            """
        asm += f"""
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
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Sub(Command):
    def toasm(self) -> str:
        asm = """
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
        """
        return "\n".join([line.strip() for line in asm.split("\n")])


class Add(Command):
    def toasm(self):
        asm = """
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
        """
        return "\n".join([line.strip() for line in asm.split("\n")])
class Neg(Command):
    def toasm(self):
        asm = """
            @SP
            M=M-1
            A=M
            M=-M
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n")])
class And(Command):
    def toasm(self):
        asm = """
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
        """
        return "\n".join([line.strip() for line in asm.split("\n")])
class Or(Command):
    def toasm(self):
        asm = """
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
        """
        return "\n".join([line.strip() for line in asm.split("\n")])
class Not(Command):
    def toasm(self):
        asm = """
            @SP
            M=M-1
            A=M
            M=!M
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n")])
class Eq(Command):
    def toasm(self):
        id = uuid.uuid4()
        asm = f"""
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
            @TRUE{id}
            D;JEQ

            // Save false onto stack
            @SP
            A=M
            M=0
            @CONTINUE{id}
            0;JMP

            // save true onto stack
            (TRUE{id})
            @SP
            A=M
            M=-1

            (CONTINUE{id})
            // Increment stack
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n")])
class Gt(Command):
    def toasm(self):
        id = uuid.uuid4()
        asm = f"""
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
            @TRUE{id}
            D;JGT
            // Save false onto stack
            @SP
            A=M
            M=0
            @CONTINUE{id}
            0;JMP
            // save true onto stack
            (TRUE{id})
            @SP
            A=M
            M=-1
            (CONTINUE{id})
            // Increment stack
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n")])
class Lt(Command):
    def toasm(self):
        id = uuid.uuid4()
        asm = f"""
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
            @TRUE{id}
            D;JLT
            // Save false onto stack
            @SP
            A=M
            M=0
            @CONTINUE{id}
            0;JMP
            // save true onto stack
            (TRUE{id})
            @SP
            A=M
            M=-1
            (CONTINUE{id})
            // Increment stack
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n")])


class NOP(Command):
    def toasm(self) -> str:
        return ""


class Parser:
    @staticmethod
    def parse(command: str) -> Command:
        tokens = command.strip().split(" ")
        if tokens[0].lower() == "push":
            return Push(tokens[1:])
        elif tokens[0].lower() == "pop":
            return Pop(tokens[1:])
        elif tokens[0].lower() == "add":
            return Add()
        elif tokens[0].lower() == "sub":
            return Sub()
        elif tokens[0].lower() == "neg":
            return Neg()
        elif tokens[0].lower() == "and":
            return And()
        elif tokens[0].lower() == "or":
            return Or()
        elif tokens[0].lower() == "not":
            return Not()
        elif tokens[0].lower() == "gt":
            return Gt()
        elif tokens[0].lower() == "lt":
            return Lt()
        elif tokens[0].lower() == "eq":
            return Eq()
        else:
            return NOP()


class Translator:
    def __init__(self, src: TextIOWrapper):
        self.src = src
        self.program = []
        self.program = self.src.readlines()

    def translate(self, out: str):
        with open(out, "w") as f:
            for line in self.program:
                command = Parser.parse(line)
                if command.toasm():
                    f.write(command.toasm()+"\n")



class CodeWriter:
    def setup_stack(self):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", action="store")
    parser.add_argument("--out", action="store")
    args = parser.parse_args()
    with open(args.src, "r") as f:
        translator = Translator(f)
        translator.translate(args.out)


if __name__ == "__main__":
    main()
