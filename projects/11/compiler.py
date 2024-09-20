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
            print(file)
            with open(file, "r") as f:
                tokenizer = JackTokenizer(f)
                ce = CompilationEngine(tokenizer)
                result = ce.compile_class()
                p = pathlib.Path(file)
                p = p.with_suffix(".xml")
                with open(p, "w") as out:
                    tree = ET.ElementTree(result)
                    tree.write(out, encoding="unicode")
    else:
        with open(args.input, "r") as f:
            tokenizer = JackTokenizer(f)
            p = pathlib.Path(args.input)
            p = p.with_suffix(".vm")
            with VMWriter(p) as vmwriter:
                ce = CompilationEngine(tokenizer, vmwriter)
                ce.compile_class()


if __name__ == "__main__":
    main()
