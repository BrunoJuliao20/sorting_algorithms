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

def shellsort(vetor, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = vetor[i]
            j = i
            while j >= interval and vetor[j - interval] > temp:
                vetor[j] = vetor[j - interval]
                j -= interval
            vetor[j] = temp
        interval = interval // 2
    return vetor

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
    vetor.sort(reverse=True)
    #vetor.sort()
    #baralha(vetor,0.05)
    inicio = time.time()
    shellsort(vetor,a)
    fim = time.time()
    res = (inicio-fim)*-1
    res_ = "%.4f" % res
    print(res_.replace(".",","))
    a = a*2
