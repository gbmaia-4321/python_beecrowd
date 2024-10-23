#pdeir valores ao usuario
x = int(input())
y = int(input())
#inicializar var de contagem
soma = 0

#se x for maior que y
if x > y:
  #inverter o valor para que x sempre seja menor que y
  aux = x
  x = y
  y = aux

             #for vai contar os numeros 1 apos o x e ate  y
for n in range(x + 1, y):
    #se n mood 2 for diferente de zero 
    if n %2 != 0:
     # incrementar a var soma 
      soma += n

      print(soma)


