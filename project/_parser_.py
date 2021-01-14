from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = iter(tokens)
        self.advance()

    def raise_error(self):
        # raise Exception("Invalid Syntax")
        return "Invalid Syntax"

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def parse(self):
        try:
            if self.current_token == None:
                return None
            result = self.expression()
            if self.current_token != None:
                self.raise_error()
            return result
        except:
            return "Invalid Syntax"
        

    def expression(self):
        try:
            result = self.term_1()
            while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
                if self.current_token.type == TokenType.PLUS:
                    self.advance()
                    result = AddNode(result, self.term_1())
                elif self.current_token.type == TokenType.MINUS:
                    self.advance()
                    result = SubtractNode(result, self.term_1())
            return result
        except:
            return "Invalid Syntax"

    def term_1(self):
        try:
            result = self.term_2()
            while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
                if self.current_token.type == TokenType.MULTIPLY:
                    self.advance()
                    result = MultiplyNode(result, self.term_2())
                elif self.current_token.type == TokenType.DIVIDE:
                    self.advance()
                    result = DivideNode(result, self.term_2())
                elif self.current_token.type == TokenType.MODULO:
                    self.advance()
                    result = ModuloNode(result, self.term_2())
            return result
        except:
            return "Invalid Syntax"

    def term_2(self):
        try:
            result = self.factor()
            if self.current_token != None and self.current_token.type == TokenType.EXPONENT:
                self.advance()
                result = ExponentNode(result, self.factor())
            return result
        except:
            return "Invalid Syntax"

    def factor(self):
        try:
            token = self.current_token
            if token.type == TokenType.L_PARENTHESIS:
                self.advance()
                result = self.expression()
                if self.current_token.type != TokenType.R_PARENTHESIS:
                    self.raise_error()
                self.advance()
                return result
            elif token.type == TokenType.NUMBER:
                self.advance()
                return NumberNode(token.value)
            elif token.type == TokenType.PLUS:
                self.advance()
                return PlusNode(self.factor())
            elif token.type == TokenType.MINUS: 
                self.advance()
                return MinusNode(self.factor())

            self.raise_error()
        except:
            return "Invalid Syntax"
