Neste projeto implementamos vários algoritmos de ordenamento estudados em Algoritmos e Estruturas de Dados com foco na: 
(1) programação dos algoritmos; 
(2) vantagens e desvantagens de cada uma, nomeadamente no que diz respeito a complexidade temporal e espacial;
(3) análise teórica e empírica da complexidade temporal.

Os diferentes tipos de sequências a testar serão os seguintes:
1) sequência aleatória.
2) sequência ordenada de forma decrescente.
3) sequência quase ordenada, com 1% ou 5% de desordenamento

Os algoritmos implementados foram os seguintes:
- Shell Sort , com incremento n=n/2 e sequência de Ciura
- Insertion Sort
- Quicksort
- Quicksort + Insertion Sort(n=10,30,60,100)
- Radix Sort LSD + MSD
- Radix Sort MSD + Insertion Sort(100)

Conclusões

	O algoritmo mais efetivo é o radixsort MSD, apesar de que para sequências pequenas o algoritmo RS LSD
apresentar tempos mais baixos e utilizar menos memória do computador, uma vez o MSD faz chamadas recursivas e usa  
mais memória para fazer os arrays auxiliares. Ainda assim considero MSD o mais efetivo uma vez que também 
conseguimos implementar uma solução utilizando várias threads e para um alfabeto maior seria uma grande vantagem.
	O insertionsort é um excelente algoritmo. Quando combinado com outros algoritmos para realizar ordenamentos de
sequências quase ordenadas ou arrays pequenos (<100+-), melhora significativamente os resultados obtidos.
O quicksort tem também um grande desempenho, quando conseguimos fazer bem a escolha da partição do array 
principal através da mediana dos 3 valores do meio, o ideal será partir o array em dois sub-arrays com igual tamanho.
	
	Para todos estes problemas não há apenas uma solução correta e dependem sempre dos recursos que dispomos. 
