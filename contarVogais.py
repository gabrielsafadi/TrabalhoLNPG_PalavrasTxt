from contarPalavras import *
from maioresPalavras import *

def vogaisContadas(arquivotxt):
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in arquivotxt:
            result[i] = arquivotxt.count(i)
    return result

print(vogaisContadas(dadosPalavras))
