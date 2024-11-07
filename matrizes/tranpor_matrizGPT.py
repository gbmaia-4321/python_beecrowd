# CHAT GPT APENAS PARA ESTUDO

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


matriz_transposta = list(zip(*matriz))
# O operador * é usado para "desempacotar" os elementos de uma lista.
# No seu caso, ele pega a matriz e passa cada sublista (linha) como um argumento separado para a função zip().
# Ou seja, em vez de passar a matriz inteira para o zip(), o * pega cada uma das sublistas dentro de matriz
# e as passa como parâmetros separados:
# zip([1, 2, 3], [4, 5, 6], [7, 8, 9])

matriz_transposta = [list(linha) for linha in matriz_transposta]
# Aqui, você está usando uma list comprehension para converter cada tupla em uma lista. Por exemplo:
# A tupla (1, 4, 7) se transforma na lista [1, 4, 7].
# A tupla (2, 5, 8) se transforma na lista [2, 5, 8].
# A tupla (3, 6, 9) se transforma na lista [3, 6, 9].

print(matriz_transposta)



# Exemplo de matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transpor a matriz
matriz_transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print(matriz_transposta)

