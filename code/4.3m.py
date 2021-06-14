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

def insertionsort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1   
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1    
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return array

def flatten(some_list):
    #agoup the sublists
    new_list = []
    for sub_list in some_list:
        new_list += sub_list
    return new_list
 
def radix(some_list, idex=None, size=None):
    """
    Recursive radix sort
    Usage: radix([unsorted list])
    Output: [sorted list]
    """
    # Initialize variables not set in the initial call
    if size == None:
        largest_num = max(some_list)
        largest_num_str = str(largest_num)
        largest_num_len = len(largest_num_str)
        size = largest_num_len
 
    if idex == None:
        idex = size
 
    # Translate the index we're looking at into an array index.
    # e.g., looking at the 10's place for 100:
    # size: 3
    # idex: 2
    #    i: (3-2) == 1
    # str(123)[i] -> 2
    i = size - idex 
 
    # The recursive base case.
    # Hint: out of range indexing errors
    if i >= size:
        return some_list
 
    # Initialize the bins we will place numbers into
    bins = [[] for _ in range(10)]
 
    # Iterate over the list of numbers we are given
    for e in some_list:
        # The destination bin; e.g.,:
        #   size: 5
        #      e: 29
        #  num_s: '00029'
        #      i: 3
        # dest_c: '2'
        # dest_i: 2
        num_s  = str(e).zfill(size)
        dest_c = num_s[i]
        dest_i = int(dest_c) 
        bins[dest_i] += [e]
 
    result = []
    for b in bins:
        #If the bin is empty it skips the recursive call
        if b == []:
            continue
        # Make the recursive call
        # Sort each of the sub-lists in our bins
        
        #use or not use insertion sort
        if len(b)<=100:
            result.append(insertionsort(b))
            continue
        result.append(radix(b, idex-1, size))
 
    # Flatten our list
    # This is also called in our recursive call,
    # so we don't need flatten to be recursive.
    flattened_result = flatten(result)
 
    return flattened_result

a=5000
print("tamanho/tempo")
for i in range(10):
    vetor=criar_vetor(a)
    #vetor.sort(reverse=True)
    #vetor.sort()
    #vetor=baralha(vetor,0.05)
    inicio = time.time()
    radix(vetor)
    fim = time.time()
    res = (inicio-fim)*-1
    res_ = "%.4f" % res
    print(res_.replace(".",","))
    a = int(a*2)
