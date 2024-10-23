#qtd recebe = 0
qtd = 0


for x in range(5):
  valor = int(input())

#se valor mood 2 tiver resto 0
  if valor % 2 == 0:
    #incrementar 1 em qtd
    qtd += 1

print(f'{qtd} valores pares')  
