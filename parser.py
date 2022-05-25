import ply.yacc as yacc
from lexico import *

def p_typescriptProgram(p) : 
  ''' programa : secao_importacao corpo '''
  pass

def p_secao_importacao(p) :
  ''' secao_importacao : IMPORT ABRECHAVES IDENTIFICADOR FECHACHAVES STRING'''
  pass

def p_corpo(p) :
  ''' corpo : definicao_classe 
            | comando 
            | definicao_classe corpo  
            | comando corpo '''
  pass

def p_definicao_classe(p) :
  ''' definicao_classe : CLASS IDENTIFICADOR ABRECHAVES corpo_classe FECHACHAVES '''
  pass

def p_corpo_classe(p) :
  ''' corpo_classe : definicao_variavel 
                   | definicao_funcao
                   | definicao_variavel corpo_classe 
                   | definicao_funcao corpo_classe '''
  pass

def p_definicao_variavel(p) :
  ''' definicao_variavel : IDENTIFICADOR DOISPONTOS tipo PONTOVIRGULA
                         | IDENTIFICADOR DOISPONTOS tipo PONTOVIRGULA IGUAL expressao '''
  pass

def p_definicao_funcao(p) :
  ''' definicao_funcao : IDENTIFICADOR ABREPARENTESES argumentos FECHAPARENTESES ABRECHAVES comandos FECHACHAVES '''
  pass

def p_argumentos(p) :
  ''' argumentos : IDENTIFICADOR DOISPONTOS tipo 
                 | IDENTIFICADOR DOISPONTOS tipo VIRGULA argumentos  '''
  pass

def p_tipo(p):
    '''tipo : NUMBER
            | STRING
            | BOOLEAN'''
    pass
  
def p_comandos(p) :
  ''' comandos : comando
               | comando comandos '''
  pass

def p_comando(p) :
  ''' comando : IF ABREPARENTESES expressao FECHAPARENTESES ABRECHAVES comando FECHACHAVES comando ELSE ABRECHAVES comando FECHACHAVES comando
              | IF ABREPARENTESES expressao FECHAPARENTESES comando ELSE comandos
              | IF ABREPARENTESES expressao FECHAPARENTESES comando ELSE ABRECHAVES  comando FECHACHAVES
              | IF ABREPARENTESES expressao FECHAPARENTESES ABRECHAVES comando FECHACHAVES IF ELSE comando
              | atribuicao
              | comando_for 
              | comando_while 
              | chamada_de_funcao 
              | comando_break 
              | comando_return 
              | comando_namespace 
              | comando_var 
              | comando_let 
              | comando_this 
              | comando_get 
              | comando_set 
              | FOR ABREPARENTESES tipo atribuicao PONTOVIRGULA expressao PONTOVIRGULA expressao FECHAPARENTESES ABRECHAVES comando2 FECHACHAVES'''
  pass

def p_comando2(p) : 
  ''' comando2 : IF ABREPARENTESES expressao FECHAPARENTESES comandos
               | IF ABREPARENTESES expressao FECHAPARENTESES ABRECHAVES comandos FECHACHAVES
               | IF ABREPARENTESES expressao FECHAPARENTESES comando ELSE comando2 
               | IF ABREPARENTESES expressao FECHAPARENTESES ABRECHAVES comando FECHACHAVES IF ELSE comando2
               | comando_for'''
  pass

def p_comando_for(p) :
  ''' comando_for : FOR ABREPARENTESES expressao PONTOVIRGULA expressao PONTOVIRGULA expressao FECHAPARENTESES ABRECHAVES comandos FECHACHAVES'''
  pass

def p_atribuicao(p) :
  '''atribuicao : tipo IDENTIFICADOR IGUAL expressao'''
  pass

def p_chamada_de_funcao(p) :
  ''' chamada_de_funcao : IDENTIFICADOR ABREPARENTESES argumentos FECHAPARENTESES '''
  pass

def p_expressao(p) :
  ''' expressao : expressao1 '''
  pass

def p_expressao6(p) :
  ''' expressao6 : expressao6 decremento expressao7
                 | expressao6 incremento expressao7 
                 | expressao7 '''
  pass

def p_expressao5(p) :
  ''' expressao5 : expressao5 MULTIPLICACAO expressao6 
                 | expressao5 DIVISAO expressao6 
                 | expressao6 '''
  pass

def p_expressao4(p) :
  ''' expressao4 : expressao4 SOMA expressao5
                 | expressao4 MENOS expressao5 
                 | expressao5  '''
  pass

def p_expressao3(p) :
  ''' expressao3 : expressao3 MENORIGUAL expressao4 
                 | expressao3 MAIORIGUAL expressao4 
                 | expressao3 MENOR expressao4 
                 | expressao3 MAIOR expressao4 
                 | expressao4 '''
  pass

def p_expressao2(p) :
  ''' expressao2 : expressao2 DIFERENTE expressao3 
                 | expressao2 IGUAL expressao3 
                 | expressao2 IGUALVALORETIPO expressao3 
                 | expressao2 IGUALVALOROUTIPO expressao3 
                 | expressao3 '''
  pass

def p_expressao1(p) :
  ''' expressao1 : IDENTIFICADOR IGUAL expressao2 
                 | expressao2 '''
  pass

def p_expressao7(p) :
  ''' expressao7 : NUMBER 
                 | IDENTIFICADOR  
                 | STRING  '''
  pass

def p_incremento(p) :
  '''incremento : expressao INCREMENTO'''
  pass

def p_decremento(p) :
  '''decremento : expressao DECREMENTO'''
  pass

def p_comando_return(p) :
  ''' comando_return : RETURN expressao '''
  pass

def p_comando_while(p) :
  ''' comando_while : WHILE ABREPARENTESES expressao FECHAPARENTESES  ABRECHAVES comando FECHACHAVES '''
  pass

def p_comando_break(p) :
  ''' comando_break : BREAK '''
  pass

def p_comando_var(p) :
  ''' comando_var : VAR IDENTIFICADOR '''
  pass

def p_comando_this(p) :
  ''' comando_this : THIS PONTO IDENTIFICADOR '''
  pass

def p_comando_let(p) :
  ''' comando_let : LET IDENTIFICADOR '''
  pass

def p_comando_set(p) :
  ''' comando_set : SET IDENTIFICADOR ABREPARENTESES argumentos  FECHAPARENTESES  ABRECHAVES comando FECHACHAVES '''
  pass

def p_comando_get(p) :
  ''' comando_get : GET IDENTIFICADOR ABREPARENTESES FECHAPARENTESES  ABRECHAVES comando FECHACHAVES '''
  pass

def p_comando_namespace(p) :
  ''' comando_namespace : NAMESPACE IDENTIFICADOR ABRECHAVES comando FECHACHAVES '''
  pass