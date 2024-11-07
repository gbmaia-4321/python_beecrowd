
# # entrada t que determina a sequencia
# t = int(input())

# # var I vai assumir o valor de 0 a 999 que sao os indices de 0 a 1000
# for i in range(1000):
#     # o resto da divisao de I por T gera o valor desejado de 0 a T -1
#     print(f'N[{i}] = {i % t}')
    


    # entrada t que determina a sequencia
t = int(input())

# var I vai assumir o valor de 0 a 999 que sao os indices de 0 a 1000
for i in range(1000):
    # var J vai assumir o valor de T - 1 que sao 0 1 2
    for j in range(t):
        # vai printar os indices determinados
        print(f'N[{i}] = {j}')
    