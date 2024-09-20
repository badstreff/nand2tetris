import os
import typing
from enum import StrEnum, auto


class UnexpectedTokenType(Exception):
    pass


class UnexpectedTokenValue(Exception):
    pass


class OutOfTokens(Exception):
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
