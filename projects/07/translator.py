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

import argparse
from abc import ABC, abstractmethod
from io import TextIOWrapper


class Command(ABC):
    @abstractmethod
    def toasm(self):
        raise NotImplementedError


class Push(Command):
    def __init__(self, args: list[str]):
        self.segment = args[0]
        self.value = args[1]

    def toasm(self) -> str:
        if self.segment == "constant":
            asm = f"""
            @{self.value}
            D=A
            """
        else:
            asm = f"""
            @{self.value}
            D=A
            @{self.segment}
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
        self.value = args[1]

    def toasm(self) -> str:
        asm = f"""
            // D = Addr
            @{self.value}
            D=A
            @{self.segment}
            A=M
            A=A+D
            D=A

            // Decrement stack
            @SP
            M=M-1

            // Store value from stack in D
            @SP
            A=M
            D=M
        """
        return "\n".join([line.strip() for line in asm.split("\n")])


class Add(Command):
    def toasm(self) -> str:
        return "TODO: add"


class Sub(Command):
    def toasm(self):
        return "TODO: sub"


class NOP(Command):
    def toasm(self) -> str:
        return "nop"


class Parser:
    @staticmethod
    def parse(command: str) -> Command:
        tokens = command.strip().split(" ")
        if tokens[0].lower() == "push":
            return Push(tokens[1:])
        elif tokens[0].lower() == "pop":
            return Pop(tokens[1:])
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
