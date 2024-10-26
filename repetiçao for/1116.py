# definindo quantas vezes o cod vai rodar
n = int(input())

for x in range(n):
  # map diz qual o tipo de entrada o usuariuo vai inserir
  a, b = map(int, input().split())
  
  # se b = 0 divisao impossivel
  if b == 0:
        print('divisao impossivel')
        # caso contrario a / b com uma casa decimal
  else:
        print(f'{(a/b):.1f}')
  