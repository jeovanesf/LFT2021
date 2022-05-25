from lexico import *
from parser import *


data = ''' "teste" '''
lexer = lex.lex()
lexer.input(data)

parser = yacc.yacc()
result = parser.parse(debug=False)