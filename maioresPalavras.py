#pega as palavras separadas, ordena elas da maior para a menor e para na 5a palavra
from contarPalavras import *
nPalavras.sort (key=len, reverse =True)
print ("As 5 maiores palavras sao: " , nPalavras[:5])