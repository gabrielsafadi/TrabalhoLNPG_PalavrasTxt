#abrindo o arquivo txt, lendo o arquivo e separando as palavras
#após isso, as palavras serão somadas
import re
from collections import Counter

contPalavras = 0
  
with open(r'meu_arquivo.txt','r') as arquivo:

        dadosPalavras = arquivo.read()
        nPalavras = dadosPalavras.split()
        contPalavras += len(nPalavras)
#printa o valor da soma das palavras 
print(contPalavras)
#pega as palavras separadas, ordena elas da maior para a menor e para na 5a palavra



 

