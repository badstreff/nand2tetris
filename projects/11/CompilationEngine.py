import xml.etree.ElementTree as ET
from VMWriter import VMWriter, MemorySegment, Command
from SymbolTable import SymbolTable, IdentifierKind
from Tokenizer import JackTokenizer, UnexpectedTokenType, UnexpectedTokenValue, OutOfTokens, TokenType


# There is probably a better way to do these 3 mappings, but it will involve a bit of a refactor
OP_TABLE = {
    "+": Command.ADD,
    "-": Command.SUB,
    "&": Command.AND,
    "|": Command.OR,
    "<": Command.LT,
    ">": Command.GT,
    "=": Command.EQ,
}
UNARY_TABLE = {
    "-": Command.NEG,
    "~": Command.NOT,
}
IdentifierKindToMemorySegment = {
    IdentifierKind.ARG: MemorySegment.ARGUMENT,
    IdentifierKind.STATIC: MemorySegment.STATIC,
    IdentifierKind.FIELD: MemorySegment.THIS,  # Not sure if this is actually correct, need to double check
    IdentifierKind.VAR: MemorySegment.LOCAL
}


class CompilationEngine(object):
    def __init__(self, tokenizer: JackTokenizer, vmwriter: VMWriter):
        self.tokenizer = tokenizer
        self.tokenizer.advance()
        self.class_symbol_table = SymbolTable()
        self.subroutine_symbol_table = SymbolTable()
        self.current_class_type = None
        self.vmwriter = vmwriter
        self.while_counter = 0
        self.if_counter = 0

    def compile_class(self) -> ET.Element:
        self._eat(TokenType.KEYWORD, "class")
        self.current_class_type = self.tokenizer.current_token
        self._eat(TokenType.IDENTIFIER)
        self._eat(TokenType.SYMBOL, "{")
        while self.tokenizer.current_token != "}":
            if self.tokenizer.current_token in ["static", "field"]:
                self.compile_class_var_dec()
            elif self.tokenizer.current_token in ["constructor", "function", "method"]:
                self.compile_subroutine()
        self._eat(TokenType.SYMBOL, "}")

    def compile_class_var_dec(self):
        class_var_kind = self.tokenizer.current_token
        self._eat(TokenType.KEYWORD)
        class_var_type = self.tokenizer.current_token
        if self.tokenizer.current_token in ["boolean", "char", "int"]:
            self._eat(TokenType.KEYWORD)
        else:
            self._eat(TokenType.IDENTIFIER)
        while self.tokenizer.current_token != ";":
            if self.tokenizer.current_token == ",":
                self._eat(TokenType.SYMBOL)
            else:
                name = self.tokenizer.current_token
                self._eat(TokenType.IDENTIFIER)
                self.class_symbol_table.define(name, class_var_type, class_var_kind)
        self._eat(TokenType.SYMBOL, ";")

    def compile_subroutine(self):
        self.subroutine_symbol_table.reset()
        if self.tokenizer.current_token == "method":
            self.subroutine_symbol_table.define("this", self.current_class_type, IdentifierKind.ARG)
        self._eat(TokenType.KEYWORD)

        if self.tokenizer.current_token in ["void", "boolean", "char", "int"]:
            self._eat(TokenType.KEYWORD)
        else:
            self._eat(TokenType.IDENTIFIER)
        name = self.tokenizer.current_token
        self._eat(TokenType.IDENTIFIER)
        self._eat(TokenType.SYMBOL, "(")
        self.compile_parameter_list()
        #FIXME: this always prints 0 for local vars because they don't actually get populated until we call compile_subroutine_body
        #TODO: MAJOR BUG
        self._eat(TokenType.SYMBOL, ")")
        self.compile_subroutine_body(self._scope_function_name(name))
        print(self.subroutine_symbol_table._table)
    
    def _scope_function_name(self, name):
        return self.current_class_type + "." + name

    def compile_parameter_list(self) -> int:
        count = 0
        while self.tokenizer.current_token != ")":
            type = self.tokenizer.current_token
            self._eat(self.tokenizer.token_type())
            name = self.tokenizer.current_token
            self._eat(TokenType.IDENTIFIER)
            self.subroutine_symbol_table.define(name, type=type, kind=IdentifierKind.ARG)
            if self.tokenizer.current_token == ",":
                self._eat(TokenType.SYMBOL)
            count += 1
        return count

    def compile_subroutine_body(self, name):
        self._eat(TokenType.SYMBOL, "{")
        while self.tokenizer.current_token == "var":
            self.compile_var_dec()
        self.vmwriter.write_function(name, self.subroutine_symbol_table.var_count(IdentifierKind.VAR))
        self.compile_statements()
        self._eat(TokenType.SYMBOL, "}")

    def compile_var_dec(self):
        self._eat(TokenType.KEYWORD, "var")
        var_type = self.tokenizer.current_token
        if var_type in ["void", "boolean", "char", "int"]:
            self._eat(TokenType.KEYWORD)
        else:
            self._eat(TokenType.IDENTIFIER)
        while self.tokenizer.current_token != ";":
            if self.tokenizer.current_token == ",":
                self._eat(TokenType.SYMBOL)
            else:
                var_name = self.tokenizer.current_token
                self._eat(TokenType.IDENTIFIER)
                self.subroutine_symbol_table.define(var_name, var_type, IdentifierKind.VAR)
        self._eat(TokenType.SYMBOL, ";")

    def compile_statements(self):
        while self.tokenizer.current_token != "}":
            if self.tokenizer.current_token == "let":
                self.compile_let()
            elif self.tokenizer.current_token == "if":
                self.compile_if()
            elif self.tokenizer.current_token == "while":
                self.compile_while()
            elif self.tokenizer.current_token == "do":
                self.compile_do() # 1st
            elif self.tokenizer.current_token == "return":
                self.compile_return() # 2nd
            else:
                raise Exception("Unknown token for subroutine body")
        return ET.Element("statements")  # TODO: DELETEME

    def compile_let(self):
        self._eat(TokenType.KEYWORD, "let")
        var_name = self.tokenizer.current_token
        self._eat(TokenType.IDENTIFIER)
        # TODO: Handle this
        if self.tokenizer.current_token == "[":
            self._eat(TokenType.SYMBOL, "[")
            self.compile_expression()
            self._eat(TokenType.SYMBOL, "]")
        self._eat(TokenType.SYMBOL, "=")
        self.compile_expression()
        try:
            kind = self.subroutine_symbol_table.kind_of(var_name)
            index = self.subroutine_symbol_table.index_of(var_name)
        except:
            kind = self.class_symbol_table.kind_of(var_name)
            index = self.class_symbol_table.index_of(var_name)
        self.vmwriter.write_pop(IdentifierKindToMemorySegment[kind], index)
        self._eat(TokenType.SYMBOL, ";")
        return ET.Element("letStatement")

    def compile_if(self):
        self.if_counter += 1
        label_if_true = f"{self.current_class_type.upper()}.IFTRUE{self.if_counter}"
        label_if_false = f"{self.current_class_type.upper()}.IFFALSE{self.if_counter}"

        self._eat(TokenType.KEYWORD, "if")
        self._eat(TokenType.SYMBOL, "(")
        self.compile_expression()
        self.vmwriter.write_arithmetic(Command.NOT)
        self.vmwriter.write_if(label_if_false)
        self._eat(TokenType.SYMBOL, ")")
        self._eat(TokenType.SYMBOL, "{")
        self.compile_statements()
        self.vmwriter.write_goto(label_if_true)
        self.vmwriter.write_label(label_if_false)
        self._eat(TokenType.SYMBOL, "}")
        if self.tokenizer.current_token == "else":
            self._eat(TokenType.KEYWORD, "else")
            self._eat(TokenType.SYMBOL, "{")
            self.compile_statements()
            self._eat(TokenType.SYMBOL, "}")
        self.vmwriter.write_label(label_if_true)

    def compile_while(self):
        # TODO: make suure this works..
        self.while_counter += 1
        label_begin = f"{self.current_class_type.upper()}.BEGINWHILE{self.while_counter}"
        label_end = f"{self.current_class_type.upper()}.ENDWHILE{self.while_counter}"
        self._eat(TokenType.KEYWORD, "while")
        self._eat(TokenType.SYMBOL, "(")
        self.vmwriter.write_label(label_begin)
        self.compile_expression()
        self.vmwriter.write_arithmetic(Command.NOT)
        self.vmwriter.write_if(label_end)
        self._eat(TokenType.SYMBOL, ")")
        self._eat(TokenType.SYMBOL, "{")
        self.compile_statements()
        self.vmwriter.write_goto(label_begin)
        self.vmwriter.write_label(label_end)
        self._eat(TokenType.SYMBOL, "}")

    def compile_do(self):
        self._eat(TokenType.KEYWORD, "do")
        function_name = self.tokenizer.current_token
        self._eat(TokenType.IDENTIFIER)
        if self.tokenizer.current_token == ".":
            self._eat(TokenType.SYMBOL, ".")
            function_name += "." + self.tokenizer.current_token
            self._eat(TokenType.IDENTIFIER)
        else:
            function_name = self.current_class_type + "." + function_name
        print(f"compiled do call to function name {function_name}")
        self._eat(TokenType.SYMBOL, "(")
        count = self.compile_expression_list()
        self.vmwriter.write_call(function_name, count)
        self._eat(TokenType.SYMBOL, ")")
        self._eat(TokenType.SYMBOL, ";")
        self.vmwriter.write_pop(MemorySegment.TEMP, 0)

    def compile_return(self):
        self._eat(TokenType.KEYWORD, "return")
        if self.tokenizer.current_token != ";":
            self.compile_expression()
        else:
            self.vmwriter.write_push(MemorySegment.CONSTANT, 0)
        self.vmwriter.write_return()
        self._eat(TokenType.SYMBOL, ";")

    # example expression = 1 + (2 * 3)
    def compile_expression(self):
        root = ET.Element("expression")
        print(self.tokenizer.current_token)
        self.compile_term()
        while self.tokenizer.current_token in ["+", "-", "*", "/", "&", "|", "<", ">", "="]:
            op = self.tokenizer.current_token
            self.process(root, TokenType.SYMBOL)
            self.compile_term()
            if op in OP_TABLE:
                self.vmwriter.write_arithmetic(Command(OP_TABLE[op]))
            elif op == "*":
                self.vmwriter.write_call("Math.multiply", 2)
            elif op == "/":
                self.vmwriter.write_call("Math.divide", 2)
            else:
                raise Exception(f"Unknown operator encounted compiling expression: {op}")
        return root

    def compile_term(self):
        # requires lookahead
        if self.tokenizer.token_type() == TokenType.INT_CONST:
            self.vmwriter.write_push(MemorySegment.CONSTANT, self.tokenizer.current_token)
            self._eat(TokenType.INT_CONST)
        elif self.tokenizer.token_type() == TokenType.STRING_CONST:
            # TODO
            self._eat(TokenType.STRING_CONST)
        elif self.tokenizer.current_token in ["true", "false", "null", "this"]:
            keyword = self.tokenizer.current_token
            self._eat(TokenType.KEYWORD)
            if keyword == "true":
                self.vmwriter.write_push(MemorySegment.CONSTANT, 1)
                self.vmwriter.write_arithmetic(Command.NEG)
            elif keyword == "false":
                self.vmwriter.write_push(MemorySegment.CONSTANT, 0)
            elif keyword == "null":
                self.vmwriter.write_push(MemorySegment.CONSTANT, 0)
            else:
                self.vmwriter.write_push(MemorySegment.POINTER, 0)
        elif self.tokenizer.current_token == "(":
            self._eat(TokenType.SYMBOL, "(")
            self.compile_expression()
            self._eat(TokenType.SYMBOL, ")")
        elif self.tokenizer.current_token in ["-", "~"]:
            op = UNARY_TABLE[self.tokenizer.current_token]
            self._eat(TokenType.SYMBOL)
            self.compile_term()
            self.vmwriter.write_arithmetic(op)
        else:
            # do look ahead
            prev = self.tokenizer.current_token
            self._eat(TokenType.IDENTIFIER)
            if self.tokenizer.current_token == "[": # varName[expression]
                # TODO 
                self._eat(TokenType.SYMBOL, "[")
                self.compile_expression()
                self._eat(TokenType.SYMBOL, "]")
            elif self.tokenizer.current_token == "(": # subroutine call form <method>(args...)
                # TODO, handle pushing this somehow
                self._eat(TokenType.SYMBOL, "(")
                count = self.compile_expression_list()
                self._eat(TokenType.SYMBOL, ")")
                self.vmwriter.write_call(self._scope_function_name(prev), count)
            elif self.tokenizer.current_token == ".": # subroutine call form <class/var>.<method>(args...)
                try:
                    kind = self.subroutine_symbol_table.index_of(prev)
                    index = self.subroutine_symbol_table.index_of(prev)
                    self.vmwriter.write_push(IdentifierKindToMemorySegment[kind], index)
                except:
                    print(f"{prev} must not be an object with a method")
                self._eat(TokenType.SYMBOL, ".")
                name = self.tokenizer.current_token
                self._eat(TokenType.IDENTIFIER)
                self._eat(TokenType.SYMBOL, "(")
                count = self.compile_expression_list()
                self._eat(TokenType.SYMBOL, ")")
                self.vmwriter.write_call(prev+"."+name, count)
            else: # varName
                try:
                    kind = self.subroutine_symbol_table.kind_of(prev)
                    index = self.subroutine_symbol_table.index_of(prev)
                except:
                    kind = self.class_symbol_table.kind_of(prev)
                    index = self.class_symbol_table.index_of(prev)
                self.vmwriter.write_push(IdentifierKindToMemorySegment[kind], index)

    def compile_expression_list(self):# -> int:
        # root = ET.Element("expressionList")
        count = 0
        while self.tokenizer.current_token != ")":
            count += 1
            self.compile_expression()
            if self.tokenizer.current_token == ",":
                self._eat(TokenType.SYMBOL, ",")
        return count

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
    
    def process(self, root: ET.Element, expectedType: TokenType, expectedValue=None) -> ET.Element:
        '''
        process takes a root ET.Element
        verifies that the current token is and expected type and (optionally) an expected value
        then appends <expectedType>current_token</expectedType> to the root and returns the ET.Element
        that was appended
        '''
        token_type = self.tokenizer.token_type()
        e = ET.Element(str(token_type))
        if self.tokenizer.token_type() == TokenType.STRING_CONST:
            e.text = self.tokenizer.string_val()
        else:
            e.text = self.tokenizer.current_token
        root.append(e)
        self._eat(expectedType, expectedValue)
        return e
        