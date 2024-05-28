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
import os

SEGMENT_TABLE = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}


class Command(ABC):
    @abstractmethod
    def toasm(self):
        raise NotImplementedError


class Push(Command):
    """
    push the value from the memory segment onto the stack
    """

    def __init__(self, args: list[str], scope: str):
        self.segment = args[0]
        self.value = int(args[1])
        self.scope = scope

    def toasm(self) -> str:
        asm = f"""
        // push {self.segment} {self.value} - {self.scope}
        """
        if self.segment == "constant":
            asm += f"""
            @{self.value}
            D=A
            """
        elif self.segment == "temp":
            asm += f"""
            @{self.value + 5}
            D=M
            """
        elif self.segment == "pointer":
            asm += f"""
            @{self.value + 3}
            D=M
            """
        elif self.segment == "static":
            asm += f"""
            @{self.scope}.{self.value}
            D=M
            """
        else:
            asm += f"""
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
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Pop(Command):
    def __init__(self, args: list[str], scope: str):
        self.segment = args[0]
        self.value = int(args[1])
        self.scope = scope

    def toasm(self) -> str:
        # Temp: This 8-word segment is also fixed and mapped directly on RAM
        # locations 5 – 12. With that in mind, any access to temp i, where i varies from
        # 0 to 7, should be translated into assembly code that accesses RAM location 5+i
        asm = f"""
        // pop {self.segment} {self.value} - {self.scope}
        """
        if self.segment == "temp":
            asm += f"""
            @{self.value + 5}
            D=A
            """
        # Unlike the virtual segments, the pointer segment
        # contains exactly two values and is mapped directly onto RAM locations 3
        # and 4.
        elif self.segment == "pointer":
            asm += f"""
            @{self.value + 3}
            D=A
            """
        # Static variables are mapped on addresses 16 to 255 of the host
        # RAM.
        elif self.segment == "static":
            asm += f"""
            @{self.scope}.{self.value}
            D=A
            """
        else:
            asm += f"""
            @{self.value}
            D=A
            @{SEGMENT_TABLE[self.segment]}
            A=M
            A=A+D
            D=A
            """
        asm += f"""
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
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Sub(Command):
    def toasm(self) -> str:
        asm = """
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
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Add(Command):
    def toasm(self):
        asm = """
            // add
            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=D+M
            @SP
            A=M
            M=D
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Neg(Command):
    def toasm(self):
        asm = """
            // neg
            @SP
            AM=M-1
            M=-M
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class And(Command):
    def toasm(self):
        asm = """
            // and
            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=D&M
            @SP
            A=M
            M=D
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Or(Command):
    def toasm(self):
        asm = """
            // or
            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=D|M
            @SP
            A=M
            M=D
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Not(Command):
    def toasm(self):
        asm = """
            // not
            @SP
            M=M-1
            A=M
            M=!M
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Eq(Command):
    def toasm(self):
        id = uuid.uuid4()
        asm = f"""
            // eq
            @SP
            AM=M-1
            D=M
            @SP
            M=M-1
            A=M
            D=M-D
            @TRUE{id}
            D;JEQ
            @SP
            A=M
            M=0
            @CONTINUE{id}
            0;JMP
            (TRUE{id})
            @SP
            A=M
            M=-1
            (CONTINUE{id})
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Gt(Command):
    def toasm(self):
        id = uuid.uuid4()
        asm = f"""
            // gt
            @SP
            AM=M-1
            D=M
            @SP
            AM=M-1
            D=M-D
            @TRUE{id}
            D;JGT
            @SP
            A=M
            M=0
            @CONTINUE{id}
            0;JMP
            (TRUE{id})
            @SP
            A=M
            M=-1
            (CONTINUE{id})
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Lt(Command):
    def toasm(self):
        id = uuid.uuid4()
        asm = f"""
            // lt
            @SP
            AM=M-1
            D=M
            @SP
            M=M-1
            A=M
            D=M-D
            @TRUE{id}
            D;JLT
            @SP
            A=M
            M=0
            @CONTINUE{id}
            0;JMP
            (TRUE{id})
            @SP
            A=M
            M=-1
            (CONTINUE{id})
            @SP
            M=M+1
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Label(Command):
    def __init__(self, args: list[str], scope: str):
        self.label = args[0]
        self.scope = scope

    def toasm(self) -> str:
        asm = f"""
        // label {self.label} - {self.scope}
        ({self.scope}.{self.label})
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Goto(Command):
    def __init__(self, args: list[str], scope: str):
        self.label = args[0]
        self.scope = scope

    def toasm(self) -> str:
        asm = f"""
        // goto {self.label} - {self.scope}
        @{self.scope}.{self.label}
        0;JMP
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class IfGoto(Command):
    def __init__(self, args: list[str], scope: str):
        self.label = args[0]
        self.scope = scope

    def toasm(self) -> str:
        asm = f"""
        // if-goto {self.label} - {self.scope}
        @SP
        AM=M-1
        D=M
        @{self.scope}.{self.label}
        D;JNE
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Function(Command):
    def __init__(self, args: list[str], scope: str):
        self.name = args[0]
        self.nVars = args[1]
        self.scope = scope

    def toasm(self) -> str:
        asm = f"""
        // function {self.name} {self.nVars} - {self.scope}
        ({self.name})
        """
        # TODO: Make this a loop in asm rather than python
        for _ in range(int(self.nVars)):
            asm += "\n" + Push(["constant", "0"], self.scope).toasm()
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Call(Command):
    def __init__(self, args: list[str], scope: str, index: int):
        self.function = args[0]
        self.nArgs = args[1]
        self.scope = scope
        self.index = index

    def toasm(self) -> str:
        retAddr = f"{self.function}$ret.{self.index}"
        asm = f"""
        // call {self.function} {self.nArgs} - {self.scope}
        @{retAddr} // push returnAddr
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
        @{self.nArgs}
        D=D-A
        @ARG
        M=D
        @SP // LCL = SP - reposition lcl
        D=M
        @LCL
        M=D
        // goto function
        @{self.function}
        0;JMP
        ({retAddr}) // (return address) generate label
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class Return(Command):
    def __init__(self, scope: str):
        self.scope = scope

    def toasm(self) -> str:
        asm = f"""
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
        """
        return "\n".join([line.strip() for line in asm.split("\n") if line.strip()])


class NOP(Command):
    def toasm(self) -> str:
        return ""


class Parser:
    @staticmethod
    def parse(command: str, scope: str, index: int) -> Command:
        tokens = command.strip().split(" ")
        if tokens[0].lower() == "push":
            return Push(tokens[1:], scope)
        elif tokens[0].lower() == "pop":
            return Pop(tokens[1:], scope)
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
        elif tokens[0].lower() == "label":
            return Label(tokens[1:], scope)
        elif tokens[0].lower() == "if-goto":
            return IfGoto(tokens[1:], scope)
        elif tokens[0].lower() == "goto":
            return Goto(tokens[1:], scope)
        elif tokens[0].lower() == "function":
            return Function(tokens[1:], scope)
        elif tokens[0].lower() == "call":
            return Call(
                tokens[1:], scope, index
            ) 
        elif tokens[0].lower() == "return":
            return Return(scope)
        else:
            return NOP()


class Translator:
    def __init__(self, src: TextIOWrapper, scope: str):
        self.src = src
        self.program = []
        self.program = self.src.readlines()
        self.scope = scope

    def translate(self, out: str):
        with open(out, "a") as f:
            index = 0
            for line in self.program:
                command = Parser.parse(line, self.scope, index)
                if command.toasm():
                    f.write(command.toasm() + "\n")
                index += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", action="store")
    args = parser.parse_args()
    src = []
    if os.path.isdir(args.src):
        base = os.path.basename(args.src)
        path = args.src
        dest = os.path.join(args.src, base) + ".asm"
        src = [
            os.path.join(args.src, file)
            for file in os.listdir(args.src)
            if os.path.isfile(os.path.join(args.src, file))
        ]
        src = [file for file in src if file[-3:] == ".vm"]
    else:
        base = os.path.basename(args.src).split(".")[0]
        path = os.path.split(args.src)[0]
        dest = os.path.join(path, base + ".asm")
        src.append(args.src)
    with open(dest, "w") as f:
        f.write("\n".join(["@256", "D=A", "@SP", "M=D\n"]))
        f.write(Call(["Sys.init", "0"], "init", 0).toasm())
        f.write("\n")
    for file in src:
        with open(file, "r") as f:
            scope = os.path.basename(file).split(".")[0]
            translator = Translator(f, scope)
            translator.translate(dest)


if __name__ == "__main__":
    main()
