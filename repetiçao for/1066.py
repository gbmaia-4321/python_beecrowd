#criando contadores para cada possibilidade 
par = 0
impar = 0
positivo = 0
negativo = 0

#bloco de codigo dentro do for vai rtodar 5 vezes
#atribuindo um valor diferente a x a cada run
for x in range(5):
  #pedindo valor ao usuario 
  valor = int(input())
#se valor mnood 2 tiver resto 0 
  if valor %2 == 0:
    #incrementar par
    par += 1
    #se nao se valor mood 2 tiver resto 1
  elif valor %2 == 1:
    #incrementar impar 
    impar += 1

  #se valor for maior igual a 0
  if valor > 0:
    #incrementar positivo
    positivo  += 1
    #se nao se valor menos que 0
  elif valor < 0:
    #incrementar negativo
    negativo += 1

print(f'{par} valor(es) par(es)''\n'
      f'{impar} valor(es) impar(es)''\n'
      f'{positivo} valor(es) positivo(s)''\n'
      f'{negativo} valor(es) negativo(s)') 

