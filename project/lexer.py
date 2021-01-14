# Lexer
from tokens import Token, TokenType


WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:    # 5.5 + 6
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)
            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)
            elif self.current_char == '*':
                self.advance()
                yield Token(TokenType.MULTIPLY)
            elif self.current_char == '/':
                self.advance()
                yield Token(TokenType.DIVIDE)
            elif self.current_char == '%':
                self.advance()
                yield Token(TokenType.MODULO)
            elif self.current_char == '^':
                self.advance()
                yield Token(TokenType.EXPONENT)
            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.L_PARENTHESIS)
            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.R_PARENTHESIS)
            else:
                # raise Exception(f"Illegal Character '{self.current_char}'")
                return "Invalid Input"

    def generate_number(self):
        decimal_pts_count = 0
        number_string = self.current_char # 5.5.
        self.advance() # .

        while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_pts_count += 1
                if decimal_pts_count > 1:
                    break

            number_string += self.current_char
            self.advance()

        if number_string.startswith('.'):
            number_string = '0' + number_string # .5 = 0.5
        if number_string.endswith('.'): 
            number_string += '0'                # 5.5. = 5.50

        return Token(TokenType.NUMBER, float(number_string))
