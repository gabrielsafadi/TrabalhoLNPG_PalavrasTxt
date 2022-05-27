from maioresPalavras import *
from contarVogais import *

arquivo1 = open("meu_arquivo.txt", "r")
frase = 'ção'
a = 0
b = 0
# percorrendo as linhas
for line in arquivo1:  
    b += 1 
    # checando a presença da sentença
    if frase in line:
      flag = 1
      break 
# condição para a presença da sentença nas linhas
# retornará sua linha ou sua não existência
if a == 0: 
   print(frase , 'não existe') 
else: 
   print('achamos', frase, 'pela primeira vez na linha', b)
    
arquivo1.close() 