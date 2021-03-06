# encoding: utf-8

"""
Bozosort
Autor:
    Bozo
Colaborador:
    Karlisson Bezerra
Tipo:
    sorting
Descrição:
    Embaralha um vetor indefinidamente, até que os números estejam em ordem.
Complexidade:  
    O(infinito)
Dificuldade:
    facil
Referências:
    http://nerdson.com/blog/libbozo-01/
    http://pt.wikipedia.org/wiki/Bogosort
"""

from random import shuffle

def bozosort(seq):
    como_deve_ficar = sorted(seq)
    while seq != como_deve_ficar:
        shuffle(seq)
    return seq

print bozosort([2,4,9,1,0,-4,17,8,0,23,67,-1])
