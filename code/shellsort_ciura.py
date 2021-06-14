import random
import time
import sys

def ler_input(a):
    vetor = []
    for i in range(a):
        vetor.append(int(sys.stdin.readline()))
    return vetor

def criar_vetor(tam):
    vetor=[]
    for i in range(tam):
        x=random.randint(0,1000001)
        vetor.append(x)
    return vetor

def shellsort(collection):
    """Pure implementation of shell sort algorithm in Python
    :param collection:  Some mutable ordered collection with heterogeneous
    comparable items inside
    :return:  the same collection ordered by ascending
 
    >>> shell_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
 
    >>> shell_sort([])
    []
 
    >>> shell_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    # Marcin Ciura's gap sequence
    gaps = [510774, 227011, 100894, 44842,19930, 8858, 3937, 1750 ,701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(collection)):
            j = i
            while j >= gap and collection[j] < collection[j - gap]:
                collection[j], collection[j - gap] = collection[j - gap], collection[j]
                j -= gap
    return collection

def imprime_vetor(vetor):
    for i in vetor:
        print(i)

def baralha(vetor,perc):
    num_elem = int(len(vetor) * perc)
    for i in range(num_elem):
        a=random.randint(0, len(vetor)-1)
        b=random.randint(0, len(vetor)-1)
        vetor[a], vetor[b] = vetor[b], vetor[a]
    return vetor        

a=5000
print("tamanho/tempo")
for i in range(10):
    vetor=criar_vetor(a)
    #vetor.sort(reverse=True)
    vetor.sort()
    baralha(vetor,0.05)
    inicio = time.time()
    aux=shellsort(vetor)
    fim = time.time()
    res = (inicio-fim)*-1
    res_ = "%.4f" % res
    print(res_.replace(".",","))
    a = int(a*2)
