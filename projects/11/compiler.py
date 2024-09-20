import os
import argparse
import pathlib
import xml.etree.ElementTree as ET
from VMWriter import VMWriter
from Tokenizer import JackTokenizer
from CompilationEngine import CompilationEngine


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", action="store", help="input file to analyze")
    args = parser.parse_args()
    if os.path.isdir(args.input):
        src = [
            os.path.join(args.input, file)
            for file in os.listdir(args.input)
            if os.path.isfile(os.path.join(args.input, file)) and file[-5:] == ".jack"
        ]
        for file in src:
            compile(file)
    else:
        compile(args.input)

def compile(path: str):
    '''
    Takes a single .jack file as a path paramenter and outputs a compiled .vm file in the same directory
    path: path to the .jack file to be compiled
    '''
    with open(path, "r") as f:
        tokenizer = JackTokenizer(f)
        p = pathlib.Path(path)
        p = p.with_suffix(".vm")
        with VMWriter(p) as vmwriter:
            ce = CompilationEngine(tokenizer, vmwriter)
            ce.compile_class()


if __name__ == "__main__":
    main()
