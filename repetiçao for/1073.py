#ler o valor n
n = int(input())

#for percorre os numeros de 1 ate N incluindo ele msm
for x in range(1, n + 1):
    #se x que é atribuido a cada indice for par 
    if x % 2 == 0:
        #imprimira o quadrado dos numeros seria exponenciando por 2
        print(f'{x}^2 = {x ** 2}')