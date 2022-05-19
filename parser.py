import ply.yacc as yacc
from lexico import *

def p_typescriptProgram(p) : 
  ''' secao_importacao corpo '''
  pass

def p_secao_importacao(p) :
  ''' IMPORT ABRECHAVE IDENTIFICADOR FECHACHAVE STRING_LITERAL '''
  pass

def p_corpo(p) :
  ''' corpo : definicao_classe 
            | comando 
            | definicao_classe corpo  
            | comando corpo '''
  pass

def p_definicao_classe(p) :
  ''' CLASS IDENTIFICADOR ABRECHAVE corpo_classe FECHACHAVE '''
  pass

def p_corpo_classe(p) :
  ''' corpo_classe : definicao_variavel 
                   | definicao_funcao
                   | definicao_variavel corpo_classe 
                   | definicao_funcao corpo_classe '''
  pass

def p_definicao_variavel(p) :
  ''' definicao_variavel : IDENTIFICADOR DOISPONTOS tipo PONTO_VIRGULA
                         | IDENTIFICADOR DOISPONTOS tipo PONTO_VIRGULA IGUAL expressao '''
  pass

def p_definicao_funcao(p) :
  ''' IDENTIFICADOR ABREPAREN argumentos FECHAPAREN ABRECHAVE comandos FECHA_CHAVE '''
  pass

def p_argumentos(p) :
  ''' argumentos : IDENTIFICADOR DOISPONTOS TIPO 
                 | IDENTIFICADOR DOISPONTOS TIPO VIRGULA argumentos  '''
  pass

def p_comandos(p) :
  ''' comandos : comando
               | comando comandos '''
  pass

def p_comando(p) :
  ''' comando : IF ABREPARENTESE expressao FECHARPARENTESE ABRECHAVES comando FECHACHAVES comando ELSE ABRECHAVES comando FECHACHAVES comando
              | IF ABREPARENTESE expressao FECHARPARENTESE comando ELSE comandos
              | IF ABREPARENTESE expressao FECHARPARENTESE comando ELSE ABRECHAVES  comando FECHACHAVES
              | IF ABREPARENTESE expressao FECHARPARENTESE ABRECHAVES comando FECHACHAVES IF ELSE comando
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
              | comando_set '''
  pass

def p_comando2(p) : 
  ''' comando2 : IF ABREPARENTESE expressao FECHARPARENTESE comandos
               | IF ABREPARENTESE expressao FECHARPARENTESE ABRECHAVES comandos FECHACHAVES
               | IF ABREPARENTESE expressao FECHARPARENTESE comando ELSE comando_2 
               | IF ABREPARENTESE expressao FECHARPARENTESE ABRECHAVES comando FECHACHAVES IF ELSE comando_2 '''
  pass

def p_comando_for(p) :
  ''' comando_for : for ABREPARENTESE TIPO ATRIBUICAO PONTOEVIRGULA expressao PONTOEVIRGULA expressao FECHARPARENTESE ABRECHAVES comandos FECHACHAVES
                  | for ABREPARENTESE TIPO ATRIBUICAO PONTOEVIRGULA expressao PONTOEVIRGULA expressao FECHARPARENTESE ABRECHAVES comandos FECHACHAVES '''
  pass

def p_chamada_de_funcao(p) :
  ''' IDENTIFICADOR ABREPARENTESE argumentos FECHARPARENTESE '''
  pass

def p_expressao(p) :
  ''' expressao1 '''
  pass

def p_expressao1(p) :
  ''' expressao1 : expressao decremento expressao2
                 | expressao incremento expressao2 
                 | expressao2 '''
  pass

def p_expressao2(p) :
  ''' expressao2 : expressao2 VEZES expressao3 
                 | expressao2 DIVISÃO expressao3 
                 | expressao3 '''
  pass

def p_expressao3(p) :
  ''' expressao3 : expressao3 MAIS expressao4 
                 | expressao3 MENOS expressao4 
                 | expressao4  '''
  pass

def p_expressao4(p) :
  ''' expressao4 : expressao4 MENORIGUAL expressao5 
                 | expressao4 MAIORIGUAL expressao5 
                 | expressao4 MENOR expressao5 
                 | expressao4 MAIOR expressao5 
                 | expressao5 '''
  pass

def p_expressao5(p) :
  ''' expressao5 : expressao5 DIFERENTE expressao6 
                 | expressao5 IGUAL expressao6 
                 | expressao5 IGUALVALORETIPO expressao6 
                 | expressao5 IGUALVALOROUTIPO expressao6 
                 | expressao6 '''
  pass

def p_expressao6(p) :
  ''' expressao7 : IDENTIFICADOR IGUAL expressao7 
                 | expressao7 '''
  pass

def p_expressao7(p) :
  ''' expressao7 : NUMERO 
                 | IDENTIFICADOR  
                 | STRING_ASPAS_SIMPLES 
                 | STRING_ASPAS_DUPLA '''
  pass

def p_comando_return(p) :
  ''' RETURN expressao '''
  pass

def p_comando_while(p) :
  ''' WHILE ABREPARENTESE expressao FECHARPARENTESE  ABRECHAVES comando FECHACHAVES '''
  pass

def p_comando_break(p) :
  ''' BREAK '''
  pass

def p_comando_var(p) :
  ''' VAR IDENTIFICADOR '''
  pass

def p_comando_this(p) :
  ''' THIS PONTO IDENTIFICADOR '''
  pass

def p_comando_let(p) :
  ''' LET IDENTIFICADOR '''
  pass

def p_comando_set(p) :
  ''' SET IDENTIFICADOR ABREPARENTESE argumentos  FECHARPARENTESE  ABRECHAVES comando FECHACHAVES '''
  pass

def p_comando_get(p) :
  ''' GET IDENTIFICADOR ABREPARENTESE FECHARPARENTESE  ABRECHAVES comando FECHACHAVES '''
  pass

def p_comando_namespace(p) :
  ''' NAMESPACE IDENTIFICADOR ABRECHAVES comando FECHACHAVES '''
  pass