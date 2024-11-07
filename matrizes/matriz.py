
# O problema pede para criar um vetor N[1000] e preencher suas posições com valores de 0 até 
# 𝑇
# −
# 1
# T−1, repetindo esses valores conforme o índice. O valor de 
# 𝑇
# T será dado na entrada (e será um número entre 2 e 50). Vamos entender a lógica do programa e como resolvê-lo.

# Passos do algoritmo
# Entrada: O programa começa lendo o valor inteiro 
# 𝑇
# T, que é o limite máximo dos valores que serão repetidos no vetor.
# Preenchimento do vetor: O vetor N terá 1000 posições. Para cada posição i do vetor N, o valor a ser armazenado será o resto da divisão de 
# 𝑖
# i por 
# 𝑇
# T, ou seja, N[i] = i % T. Isso garante que os valores se repetem de 0 até 
# 𝑇
# −
# 1
# T−1.
# Saída: O programa deve imprimir cada valor do vetor N, com o formato N[i] = x, onde i é o índice da posição e x é o valor correspondente.


t = int(input())

for i in range(1000):
    print(f'"N [{i}] = {i % t}')