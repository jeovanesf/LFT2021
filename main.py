# Inicio da Analise Lexixa do TypeScript

from yaml import parse
from lexico import *
from parser import *

data = '''   3 + 3   tototo 10 /* 10 */ in  //teste'''
lexer = lex.lex()
lexer.input(data)

parser = yacc.yacc()
result = parser.parse(debug=False)
