# Inicio da Analise Lexixa do TypeScript

import ply.lex as lex

#SIMBOLOS
#from ExpressionLanguageLex import lexer

tokens = [
   'SOMA',
   'MENOS',
   'MULTIPLICACAO',
   'DIVISAO',
   'PORCENTO',
   'MAIOR',
   'MENOR',
   'MAIORIGUAL',
   'MENORIGUAL',
   'BARRA',
   'CIRCUNFLEXO',
   'TIU',
   'IGUAL',
   'ABRECHAVES',
   'FECHACHAVES',
   'ABREPARENTESES',
   'FECHAPARENTESES',
   'ABRECONCHETES',
   'FECHACONCHETES',
   'PONTOVIRGULA',
   'COMERCIAL',
   'COMPARACAO',
   'NUMERO',
   'EXPONENCIACAO',
   'INCREMENTO',
   'DECREMENTO',
   'DIFERENTE',
   'IGUALVALORETIPO',
   'IGUALVALOROUTIPO',
   'OU',
   'NEGACAO',
   'ECOMERCIAL',
   'IDENTIFICADOR',
   'STRING_ASPAS_SIMPLES',
   'STRING_ASPAS_DUPLAS'
]

# EXPRESÃO REGULAR PARA SIMBOLOS
t_SOMA = r'\+'
t_MENOS = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_PORCENTO = r'\%'
t_MENOR = r'\<'
t_MAIOR = r'\>'
t_MAIORIGUAL = r'\>\='
t_MENORIGUAL = r'\<\='
t_BARRA = r'\|'
t_CIRCUNFLEXO = r'\^'
t_TIU = r'~'
t_IGUAL = r'\='
t_ABRECHAVES = r'\{'
t_FECHACHAVES = r'\}'
t_ABREPARENTESES = r'\('
t_FECHAPARENTESES = r'\)'
t_ABRECONCHETES = r'\['
t_FECHACONCHETES = r'\]'
t_PONTOVIRGULA = r'\;'
t_COMERCIAL = r'\&\&'
t_COMPARACAO = r'\=\='
t_EXPONENCIACAO = r'\*\*'
t_INCREMENTO = r'\+\+'
t_DECREMENTO = r'\-\-'
t_DIFERENTE = r'\=\!'
t_IGUALVALORETIPO = r'\=\=\='
t_IGUALVALOROUTIPO = r'\!\=\='
t_OU = r'\|\|'
t_NEGACAO = r'\!'
t_ECOMERCIAL = r'\&'

#PALAVRAS RESERVADAS
palavras_reservadas = {
    'break' : 'BREAK',
    'class' : 'CLASS',
    'else' : 'ELSE',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'if' : 'IF',
    'import' : 'IMPORT',
    'instanceof' : 'INSTANCEOF',
    'new' : 'NEW',
    'null' : 'NULL',
    'return' : 'RETURN',
    'this' : 'THIS',
    'true' : 'TRUE',
    'var' : 'VAR',
    'void' : 'VOID',
    'while' : 'WHILE',
    'let' : 'LET',
    'package' : 'PACKAGE',
    'public' : 'PUBLIC',
    'static' : 'STATIC',
    'typeof' : 'TYPEOF',
    'boolean' : 'BOOLEAN',
    'number' : 'NUMBER',
    'string' : 'STRING',
    'construtor' : 'CONSTRUTOR',
    'from' : 'FROM',
    'get' : 'GET',
    'is' : 'IS',
    'module' : 'MODULE',
    'namespace' : 'NAMESPACE',
    'of' : 'OF',
    'set' : 'SET',
    'type' : 'TYPE',
    'in' : 'IN',
}

tokens = tokens + list(palavras_reservadas.values())

#DEFINIÇAO DE NUMERO
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    ##FAZER CONDIÇÃO PARA Nº INT, FLOAT ....
    t.value = int(t.value)
    return t

#DEFINAÇÃO DE COMENTÁRIO MULTILINHAS
def t_COMENTARIO(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    pass

#DEFINIÇÃO DE ESPAÇO EM BRANCO
def t_BRANCO(t):
    r'[ \t]'
    pass

#DEFINIÇÃO DE STRING ASPAS SIMPLE
def t_STRING_ASPAS_SIMPLES(t):
    r'\'.*\''
    return t

#DEFINIÇÃO DE STRING ASPAS DUPLAS
def t_STRING_ASPAS_DUPLAS(t):
    r'\".*\"'
    return t


def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = palavras_reservadas.get(t.value,'IDENTIFICADOR')    # Check for reserved words
    return t

def t_error(t):
    print(str(t.value) + 'Invalid token')


#INDETAÇÃO


#Testando

# # Give the lexer some input
# lexer = lex.lex()
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     print(tok)