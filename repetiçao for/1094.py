# entrada que define quantas vezes o cod vai rodar
n = int(input())

# iniciando contadores
total_c = 0
total_r = 0
total_s = 0


for caso in range(n):
  qtd, tipo = input().split()
  qtd = int(qtd)
 

  if tipo == 'C':
    total_c += qtd

  elif tipo == 'R':
    total_r += qtd

  elif tipo == 'S':
    total_s += qtd

total = total_c + total_r + total_s

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {total_c}')
print(f'Total de ratos: {total_r}')
print(f'Total de sapos: {total_s}')
print(f'Percentual de coelhos: {((total_c/total)*100):.2f} %')
print(f'Percentual de ratos: {((total_r/total)*100):.2f} %')
print(f'Percentual de sapos: {((total_s/total)*100):.2f} %')
