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

def countingsort(array, place):
    size = len(array)
    #inicialize output with original size
    output = [0] * size
    #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = [0] * 10
    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    # Modify the count array such that each element at each index 
    #stores the sum of previous counts.
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        #start in last element
        index = array[i] // place
        #ording from least SD
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
    #copy values from the auxiliar array to original
    for i in range(0, size):
        array[i] = output[i]

def radixsort(array):
    # Get maximum element
    max_element = max(array)
    # Apply counting sort to sort elements based on place value.
    place = 1
    #each one of the 6 digits
    while max_element // place > 0:
        countingsort(array, place)
        place *= 10
    
a=5000
print("tamanho/tempo")
for i in range(12):
    vetor=criar_vetor(a)
    #vetor.sort(reverse=True)
    #vetor.sort()
    #vetor=baralha(vetor,0.05)
    inicio = time.time()
    radixsort(vetor)
    fim = time.time()
    res = (inicio-fim)*-1
    res_ = "%.4f" % res
    print(res_.replace(".",","),a)
    a = a*2
