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
    EQ = auto()
    GT = auto()
    LT = auto()
    AND = auto()
    OR = auto()
    NOT = auto()

class VMWriter:
    def __init__(self, output_path: str):
        self.out_path = output_path
    def write_push(self, segment: MemorySegment, index: int):
        self.out.write(f"push {segment} {index}\n")
    def write_pop(self, segment: MemorySegment, index: int):
        self.out.write(f"pop {segment} {index}\n")
    def write_arithmetic(self, command: Command):
        self.out.write(f"{command}\n")
    def write_label(self, label: str):
        self.out.write(f"label {label}\n")
    def write_goto(self, label: str):
        self.out.write(f"goto {label}\n")
    def write_if(self, label: str):
        self.out.write(f"if-goto {label}\n")
    def write_call(self, name: str, nargs: int):
        self.out.write(f"call {name} {nargs}\n")
    def write_function(self, name: str, nvars: int):
        self.out.write(f"function {name} {nvars}\n")
    def write_return(self):
        self.out.write("return\n")
    def close(self):
        self.out.close()
    def __enter__(self):
        self.out = open(self.out_path, "w")
        return self
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.out.close()
