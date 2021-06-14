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

def find_median(input_list,start,end):
    #retorna indice do valor da mediana
    a = input_list[((start+end)//2)-1]
    b = input_list[((start+end)//2)+1]
    c = input_list[(start+end)//2]
    indice = 0
    if a > b:
        if a < c:
            indice = ((start+end)//2)-1
        elif b > c:
            indice = ((start+end)//2)+1
        else:
            indice = (start+end)//2
    else:
        if a > c:
            indice = ((start+end)//2)-1
        elif b < c:
            indice = ((start+end)//2)+1
        else:
            indice = (start+end)//2
    return indice

def partition(vetor,low,high,median_index):
    i = (low-1)	# index of smaller element 
    pivot = vetor[median_index]	# pivot
    vetor[median_index],vetor[high] = vetor[high],vetor[median_index] 
    for j in range(low , high): 
        # If current element is smaller than or 
        # equal to pivot 
        if vetor[j] <= pivot:
            # increment index of smaller element 
            i = i+1
            vetor[i],vetor[j] = vetor[j],vetor[i] 
    vetor[i+1],vetor[high] = vetor[high],vetor[i+1] 
    return (i+1) 

def quicksort(vetor,start,end): 
    if start<end:
        median_index=find_median(vetor, start, end)
        pivot_index=partition(vetor,start,end,median_index)
        
        quicksort(vetor, start,pivot_index-1)
        quicksort(vetor, pivot_index+1, end)
               
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
    quicksort(vetor,0,a-1)
    fim = time.time()
    res = (inicio-fim)*-1
    res_ = "%.4f" % res
    print(res_.replace(".",","))
    a = a*2