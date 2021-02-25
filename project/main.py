"""
 Name: Sagar Sikchi
 Batch B2
 Roll No. 65
 Course Project (System Programming): Math Interpreter using Python
 """


# Main File
from tokens import Token
from lexer import Lexer
from _parser_ import Parser
from interpreter import Interpreter
from prettytable import PrettyTable

instructions = PrettyTable()
print('\n############################## MATH INTERPRETER ##############################\n')
print('\nFollowing operations are supported and show errors also:\n')
instructions.field_names = ['Sr.No.', 'Operations', 'Description']
instructions.add_row(['1', 'Addition', '5+6, 5+ 6, 5 +6, 5 + 6'])
instructions.add_row(['2', 'Subtraction', '5-6, 5- 6, 5 -6, 5 - 6'])
instructions.add_row(['3', 'Multiplication', '5*6, 5* 6, 5 *6, 5 * 6'])
instructions.add_row(['4', 'Division', '5/6, 5/ 6, 5 /6, 5 / 6'])
instructions.add_row(['5', 'Modulo', '5%6, 5% 6, 5 %6, 5 % 6'])
instructions.add_row(['6', 'Exponent', '5^6, 5^ 6, 5 ^6, 5 ^ 6'])
instructions.add_row(['7', 'Brackets', '(5+6)*7 = 77.0'])
instructions.add_row(['8', 'Nested Brackets', '(5+(5+6))*7 = 112.0'])
print(instructions, "\n\n")

# File Handling
input_file  = 'input_file.txt'
output_file = 'output_file.txt'
i_file = open(input_file, 'r')
o_file = open(output_file, 'w')

_input_ = i_file.readline()

while _input_ != "":
    value = 0
    # _input_ = input("M2I ===> ")
    print("M2I ===> ", _input_)

    lexer = Lexer(_input_)
    tokens = lexer.generate_tokens()

    parser = Parser(tokens)
    tree = parser.parse()

    if not tree:
        tokens = "Invalid Input"
        value = "Invalid Input"
    else:
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        lexer = Lexer(_input_)
        tokens = lexer.generate_tokens()

    table = PrettyTable()
    table.field_names = ['Expression', _input_]
    table.add_row(['Tokens', list(tokens) if tree else tokens])
    table.add_row(['', ''])
    table.add_row(['Parse Tree', tree if tree else "Invalid Input"])
    table.add_row(['', ''])
    table.add_row(['Value', value])
    print(table)
    print("\n\n\n\n")

    o_file.write(str(table))
    o_file.write("\n\n\n\n")

    _input_ = i_file.readline()

i_file.close()
o_file.close()
