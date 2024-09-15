from enum import StrEnum, auto

class MemorySegment(StrEnum):
    CONSTANT = auto()
    ARGUMENT = auto()
    STATIC = auto()
    LOCAL = auto()
    THIS = auto()
    THAT = auto()
    POINTER = auto()
    TEMP = auto()

class Command(StrEnum):
    ADD = auto()
    SUB = auto()
    NEG = auto()
    EG = auto()
    GT = auto()
    LT = auto()
    AND = auto()
    OR = auto()
    NOT = auto()

class VMWriter:
    def __init__(self, output_path: str):
        self.out = open(output_path, "w")
    def write_push(self, segment: MemorySegment, index: int):
        self.out.write(f"push {segment} {index}")
    def write_pop(self, segment: MemorySegment, index: int):
        self.out.write(f"pop {segment} {index}")
    def write_arithmetic(self, command: Command):
        self.out.write(f"{command}")
    def write_label(self, label: str):
        self.out.write(f"label {label}")
    def write_goto(self, label: str):
        self.out.write(f"goto {label}")
    def write_if(self, label: str):
        self.out.write(f"if-goto {label}")
    def write_call(self, name: str, nargs: int):
        self.out.write(f"call {name} {nargs}")
    def write_function(self, name: str, nvars: int):
        self.out.write(f"function {name} {nvars}")
    def write_return(self):
        self.out.write("return")
    def close(self):
        self.out.close()