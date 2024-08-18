import os
import typing
import argparse
import pathlib
from enum import Enum, StrEnum, auto
import xml.etree.ElementTree as ET
from dataclasses import dataclass



class UnexpectedTokenType(Exception):
    pass


class UnexpectedTokenValue(Exception):
    pass


class OutOfTokens(Exception):
    pass


class SymbolCategory(StrEnum):
    FIELD = auto()
    STATIC = auto()
    LOCAL = auto()
    ARG = auto()
    CLASS = auto()
    SUBROUTINE = auto()
class SymbolUsage(StrEnum):
    DECLARED_STATIC = auto()
    DECLARED_FIELD = auto()
    DECLARED_VAR = auto()
    DECLARED_PARAMETER_LIST = auto()
    EXPRESSION = auto()
class SymbolTable(object):
    @dataclass
    class _entry():
        category: SymbolCategory
        index: int
        usage: SymbolUsage
    def __init__():
        pass


class TokenType(StrEnum):
    KEYWORD = auto()
    SYMBOL = auto()
    IDENTIFIER = auto()
    INT_CONST = "integerConstant"
    STRING_CONST = "stringConstant"


class Keyword(StrEnum):
    CLASS = auto()
    METHOD = auto()
    FUNCTION = auto()
    CONSTRUCTOR = auto()
    INT = auto()
    BOOLEAN = auto()
    CHAR = auto()
    VOID = auto()
    VAR = auto()
    STATIC = auto()
    FIELD = auto()
    LET = auto()
    DO = auto()
    IF = auto()
    ELSE = auto()
    WHILE = auto()
    RETURN = auto()
    TRUE = auto()
    FALSE = auto()
    NULL = auto()
    THIS = auto()


SYMBOLS = "{}[]().,;+-*/&|<>=~"


class JackTokenizer(object):
    def __init__(self, input: typing.TextIO):
        self.current_token = ""
        self.input = input
        # while self.has_more_tokens():
        #     self.advance()
        #     if self.current_token:
        #         print(f"{self.current_token} = {self.token_type()}")

    def has_more_tokens(self) -> bool:
        "check if there are more tokens"
        cur = self.input.tell()
        self.input.seek(0, os.SEEK_END)
        end = self.input.tell()
        self.input.seek(cur, os.SEEK_SET)
        return cur != end

    def advance(self):
        """
        get the next token from the input stream and makes it the current token
        should only be called if has_more_tokens() returns true
        """
        self.current_token = ""
        while c := self.input.read(1):
            cur = self.input.tell()
            next = self.input.read(1)
            self.input.seek(cur, os.SEEK_SET)
            if c.isspace():
                if not self.current_token:
                    continue
                else:
                    return
            self.current_token += c
            # consume comments
            if c in "/":
                if c == "/" and next == "/":
                    while c != "\n":
                        c = self.input.read(1)
                    self.current_token = self.current_token[:-2]
                elif c == "/" and next == "*":
                    last = ""
                    while x := self.input.read(1):
                        if last + x == "*/":
                            break
                        last = x
                    self.current_token = self.current_token[:-2]
                if not self.current_token:
                    continue
            if next in SYMBOLS:
                return
            if c == '"':
                while x := self.input.read(1):
                    self.current_token += x
                    if x == '"':
                        return
            if c in SYMBOLS:
                return

    def token_type(self) -> TokenType:
        """
        returns the type of the current token as a constant
        """
        if self.current_token in SYMBOLS:
            return TokenType.SYMBOL
        elif self.current_token in Keyword:
            return TokenType.KEYWORD
        elif self.current_token.isdigit():
            return TokenType.INT_CONST
        elif self.current_token[0] == self.current_token[-1] == '"':
            return TokenType.STRING_CONST
        else:
            return TokenType.IDENTIFIER

    def keyword(self) -> Keyword:
        """
        returns the keyword of the current token as a constant
        should only be called if self.token_type is KEYWORD
        """
        return Keyword[self.current_token]

    def symbol(self) -> str:
        """
        returns the symbol that is the current token
        should only be called if self.token_type is SYMBOL
        """
        return self.current_token

    def identifier(self) -> str:
        """
        returns the identifier that is the current token
        should only be called if self.token_type is IDENTIFIER
        """
        return self.current_token

    def int_val(self) -> int:
        """
        returns the integer value that is the current token
        should only be called if self.token_type is INT_CONST
        """
        return int(self.current_token)

    def string_val(self) -> str:
        """
        returns the string value that is the current token without opening and closing quotes
        should only be called if self.token_type is STRING_CONST
        """
        return self.current_token[1:-1]


class CompilationEngine(object):
    def __init__(self, tokenizer: JackTokenizer):
        self.tokenizer = tokenizer
        self.tokenizer.advance()

    def compile_class(self) -> ET.Element:
        root = ET.Element('class')
        self.process(root, TokenType.KEYWORD, "class")
        self.process(root, TokenType.IDENTIFIER)
        self.process(root, TokenType.SYMBOL, "{")
        while self.tokenizer.current_token != "}":
            if self.tokenizer.current_token in ["static", "field"]:
                root.append(self.compile_class_var_dec())
            elif self.tokenizer.current_token in ["constructor", "function", "method"]:
                root.append(self.compile_subroutine())
        self.process(root, TokenType.SYMBOL, "}")
        return root

    def compile_class_var_dec(self):
        root = ET.Element("classVarDec")
        self.process(root, TokenType.KEYWORD)
        if self.tokenizer.current_token in ["boolean", "char", "int"]:
            self.process(root, TokenType.KEYWORD)
        else:
            self.process(root, TokenType.IDENTIFIER)
        self.process(root, TokenType.IDENTIFIER)
        while self.tokenizer.current_token != ";":
            if self.tokenizer.current_token == ",":
                self.process(root, TokenType.SYMBOL)
            else:
                self.process(root, TokenType.IDENTIFIER)
        self.process(root, TokenType.SYMBOL, ";")
        return root

    def compile_subroutine(self):
        root = ET.Element("subroutineDec")
        self.process(root, TokenType.KEYWORD)
        if self.tokenizer.current_token in ["void", "boolean", "char", "int"]:
            self.process(root, TokenType.KEYWORD)
        else:
            self.process(root, TokenType.IDENTIFIER)
        self.process(root, TokenType.IDENTIFIER)
        self.process(root, TokenType.SYMBOL, "(")
        root.append(self.compile_parameter_list())
        self.process(root, TokenType.SYMBOL, ")")
        root.append(self.compile_subroutine_body())
        return root

    def compile_parameter_list(self):
        root = ET.Element("parameterList")
        while self.tokenizer.current_token != ")":
            if self.tokenizer.token_type() == TokenType.KEYWORD:
                self.process(root, TokenType.KEYWORD)
            elif self.tokenizer.token_type() == TokenType.IDENTIFIER:
                self.process(root, TokenType.IDENTIFIER)
            elif self.tokenizer.token_type() == TokenType.SYMBOL:
                self.process(root, TokenType.SYMBOL)
            else:
                raise Exception("Unexpected token compiling_parameter_list")
        return root

    def compile_subroutine_body(self):
        root = ET.Element("subroutineBody")
        self.process(root, TokenType.SYMBOL, "{")
        while self.tokenizer.current_token == "var":
            root.append(self.compile_var_dec())
        root.append(self.compile_statements())
        self.process(root, TokenType.SYMBOL, "}")
        return root

    def compile_var_dec(self):
        root = ET.Element("varDec")
        self.process(root, TokenType.KEYWORD, "var")
        if self.tokenizer.current_token in ["void", "boolean", "char", "int"]:
            self.process(root, TokenType.KEYWORD)
        else:
            self.process(root, TokenType.IDENTIFIER)
        while self.tokenizer.current_token != ";":
            if self.tokenizer.current_token == ",":
                self.process(root, TokenType.SYMBOL)
            else:
                self.process(root, TokenType.IDENTIFIER)
        self.process(root, TokenType.SYMBOL, ";")
        return root

    def compile_statements(self):
        root = ET.Element("statements")
        while self.tokenizer.current_token != "}":
            if self.tokenizer.current_token == "let":
                root.append(self.compile_let())
            elif self.tokenizer.current_token == "if":
                root.append(self.compile_if())
            elif self.tokenizer.current_token == "while":
                root.append(self.compile_while())
            elif self.tokenizer.current_token == "do":
                root.append(self.compile_do())
            elif self.tokenizer.current_token == "return":
                root.append(self.compile_return())
            else:
                raise Exception("Unknown token for subroutine body")
        return root

    def compile_let(self):
        root = ET.Element("letStatement")
        self.process(root, TokenType.KEYWORD, "let")
        self.process(root, TokenType.IDENTIFIER)
        if self.tokenizer.current_token == "[":
            self.process(root, TokenType.SYMBOL, "[")
            root.append(self.compile_expression())
            self.process(root, TokenType.SYMBOL, "]")
        self.process(root, TokenType.SYMBOL, "=")
        root.append(self.compile_expression())
        self.process(root, TokenType.SYMBOL, ";")
        return root

    def compile_if(self):
        root = ET.Element("ifStatement")
        self.process(root, TokenType.KEYWORD, "if")
        self.process(root, TokenType.SYMBOL, "(")
        root.append(self.compile_expression())
        self.process(root, TokenType.SYMBOL, ")")
        self.process(root, TokenType.SYMBOL, "{")
        root.append(self.compile_statements())
        self.process(root, TokenType.SYMBOL, "}")
        if self.tokenizer.current_token == "else":
            self.process(root, TokenType.KEYWORD, "else")
            self.process(root, TokenType.SYMBOL, "{")
            root.append(self.compile_statements())
            self.process(root, TokenType.SYMBOL, "}")
        return root

    def compile_while(self):
        root = ET.Element("whileStatement")
        self.process(root, TokenType.KEYWORD, "while")
        self.process(root, TokenType.SYMBOL, "(")
        root.append(self.compile_expression())
        self.process(root, TokenType.SYMBOL, ")")
        self.process(root, TokenType.SYMBOL, "{")
        root.append(self.compile_statements())
        self.process(root, TokenType.SYMBOL, "}")
        return root

    def compile_do(self):
        # requires lookahead
        root = ET.Element("doStatement")
        self.process(root, TokenType.KEYWORD, "do")
        self.process(root, TokenType.IDENTIFIER)
        if self.tokenizer.current_token == ".":
            self.process(root, TokenType.SYMBOL, ".")
            self.process(root, TokenType.IDENTIFIER)
        self.process(root, TokenType.SYMBOL, "(")
        root.append(self.compile_expression_list())
        self.process(root, TokenType.SYMBOL, ")")
        self.process(root, TokenType.SYMBOL, ";")
        return root

    def compile_return(self):
        root = ET.Element("returnStatement")
        self.process(root, TokenType.KEYWORD, "return")
        if self.tokenizer.current_token != ";":
            root.append(self.compile_expression())
        self.process(root, TokenType.SYMBOL, ";")
        return root

    def compile_expression(self):
        root = ET.Element("expression")
        root.append(self.compile_term())
        while self.tokenizer.current_token in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            self.process(root, TokenType.SYMBOL)
            root.append(self.compile_term())
        return root

    def compile_term(self):
        # requires lookahead
        root = ET.Element("term")
        if self.tokenizer.token_type() == TokenType.INT_CONST:
            self.process(root, TokenType.INT_CONST)
        elif self.tokenizer.token_type() == TokenType.STRING_CONST:
            self.process(root, TokenType.STRING_CONST)
        elif self.tokenizer.current_token in ["true", "false", "null", "this"]:
            self.process(root, TokenType.KEYWORD)
        elif self.tokenizer.current_token == "(":
            self.process(root, TokenType.SYMBOL, "(")
            root.append(self.compile_expression())
            self.process(root, TokenType.SYMBOL, ")")
        elif self.tokenizer.current_token in ["-", "~"]:
            self.process(root, TokenType.SYMBOL)
            root.append(self.compile_term())
        else:
            # do look ahead
            self.process(root, TokenType.IDENTIFIER)
            if self.tokenizer.current_token == "[": # varName[expression]
                self.process(root, TokenType.SYMBOL, "[")
                root.append(self.compile_expression())
                self.process(root, TokenType.SYMBOL, "]")
            elif self.tokenizer.current_token == "(": # subroutine call
                self.process(root, TokenType.SYMBOL, "(")
                root.append(self.compile_expression_list())
                self.process(root, TokenType.SYMBOL, ")")
            elif self.tokenizer.current_token == ".": # subroutine call
                self.process(root, TokenType.SYMBOL, ".")
                self.process(root, TokenType.IDENTIFIER)
                self.process(root, TokenType.SYMBOL, "(")
                root.append(self.compile_expression_list())
                self.process(root, TokenType.SYMBOL, ")")
            else: # varName
                pass
        return root 

    def compile_expression_list(self):# -> int:
        root = ET.Element("expressionList")
        while self.tokenizer.current_token != ")":
            root.append(self.compile_expression())
            if self.tokenizer.current_token == ",":
                self.process(root, TokenType.SYMBOL, ",")
        return root

    def _eat(self, type: TokenType, value=None):
        """
        validates that the token is of type type and advances the tokenizer
        if value is passed also validate that the value matches
        """
        if self.tokenizer.token_type() != type:
            raise UnexpectedTokenType()
        if value and self.tokenizer.current_token != value:
            raise UnexpectedTokenValue()
        if not self.tokenizer.has_more_tokens():
            raise OutOfTokens()
        self.tokenizer.advance()
    
    def process(self, root: ET.Element, expectedType: TokenType, expectedValue=None):
        e = ET.Element(str(self.tokenizer.token_type()))
        if self.tokenizer.token_type() == TokenType.STRING_CONST:
            e.text = self.tokenizer.string_val()
        else:
            e.text = self.tokenizer.current_token
        root.append(e)
        self._eat(expectedType, expectedValue)
        


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
                p = p.with_suffix('.xml')
                with open(p, "w") as out:
                    tree = ET.ElementTree(result)
                    tree.write(out, encoding="unicode")
    else:
        with open(args.input, "r") as f:
            tokenizer = JackTokenizer(f)
            ce = CompilationEngine(tokenizer)
            result = ce.compile_class()
            p = pathlib.Path(args.input)
            p = p.with_suffix('.xml')
            with open(p, "w") as out:
                tree = ET.ElementTree(result)
                tree.write(out, encoding="unicode")



if __name__ == "__main__":
    main()
