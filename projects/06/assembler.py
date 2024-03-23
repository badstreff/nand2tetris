import argparse
from abc import ABC, abstractmethod
from io import TextIOWrapper


class Instruction(ABC):
    @abstractmethod
    def tobinary(self):
        raise NotImplementedError


class AInstruction(Instruction):
    def __init__(self, value: str):
        self.value = value

    def tobinary(self) -> str:
        try:
            num = int(self.value)
            return "{0:016b}".format(num)
        except:
            return None


class CInstruction(Instruction):
    def __init__(self, dest, comp, jump):
        self.dest = dest
        self.comp = comp
        self.jump = jump

    def tobinary(self):
        r = "111"
        # set comp bytes
        r += "1" if "M" in self.comp else "0"
        r += dict(
            [
                ("0",   "101010"), ("1",   "111111"), ("-1",  "111010"), ("D",   "001100"),
                ("A",   "110000"), ("!D",  "001101"), ("!A",  "110001"), ("-D",  "001111"),
                ("-A",  "110011"), ("D+1", "011111"), ("A+1", "110111"), ("D-1", "001110"),
                ("A-1", "110010"), ("D+A", "000010"), ("D-A", "010011"), ("A-D", "000111"),
                ("D&A", "000000"), ("D|A", "010101"), ("M",   "110000"), ("!M",  "110001"),
                ("-M",  "110011"), ("M+1", "110111"), ("M-1", "110010"), ("D+M", "000010"),
                ("D-M", "010011"), ("M-D", "000111"), ("D&M", "000000"), ("D|M", "010101"),
            ]
        )[self.comp]
        # set dest bytes
        r += "1" if self.dest and "A" in self.dest else "0"
        r += "1" if self.dest and "D" in self.dest else "0"
        r += "1" if self.dest and "M" in self.dest else "0"
        # set jmp bytes
        r += dict(
            [
                (None,   "000"), ("JGT",   "001"), ("JEQ",  "010"), ("JGE",   "011"),
                ("JLT",   "100"), ("JNE",  "101"), ("JLE",  "110"), ("JMP",  "111"),
            ]
        )[self.jump]
        return r


class Parser:
    @staticmethod
    def parse(ins: str) -> Instruction:
        if ins[0] == "@":
            return AInstruction(ins[1:])
        else:
            if "=" in ins and ";" in ins:
                dest = ins.split("=")[0]
                comp, jump = ins.split("=")[1].split[";"]
            elif "=" in ins:
                dest, comp = ins.split("=")
                jump = None
            elif ";" in ins:
                dest = None
                comp, jump = ins.split(";")
            return CInstruction(dest, comp, jump)


class SymbolTable(dict):
    def __init__(self):
        defaults = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "SCREEN": 16384,
            "KBD": 24576,
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
        }
        self.update(defaults)


class Assembler:
    MEMORY_START = 16

    def __init__(self, src: TextIOWrapper, st: SymbolTable):
        self.src = src
        self.st = st
        self.program = []
        self.program = self.src.readlines()

    def preprocess(self):
        # strip whitespace and comments
        self.program = [x.split("//")[0] for x in self.program]
        self.program = [x.strip() for x in self.program if x.strip()]
        # build symbol table
        for line in self.program:
            # handle labels
            if line.startswith("("):
                self.st[line[1:-1]] = self.program.index(line)
                self.program.remove(line)
            # handle symbols
            elif line.startswith("@"):
                symbol = line[1:]
                if not symbol.isdigit():
                    if symbol not in self.st:
                        self.st[symbol] = None
        # assign values to symbols
        next = self.MEMORY_START
        for k, v in self.st.items():
            if v is None:
                self.st[k] = next
                next += 1

    def assemble(self, out: str):
        self.preprocess()
        with open(out, "w") as f:
            for line in self.program:
                ins = Parser.parse(line)
                if isinstance(ins, AInstruction):
                    try:
                        ins.value = self.st[ins.value]
                    except:
                        pass
                print(ins.tobinary())
                f.write(ins.tobinary() + "\n")
            f.flush()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", action="store")
    parser.add_argument("--out", action="store")
    args = parser.parse_args()
    with open(args.src, "r") as f:
        st = SymbolTable()
        asm = Assembler(f, st)
        asm.assemble(args.out)


if __name__ == "__main__":
    main()
