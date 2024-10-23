#quantia = recebe 0
quantia = 0

#O bloco de codigo dentro do for vai se executado 6 vezes 
# A cada vez que rodar a var N recebera um valor diferente de 0 a 5
          #range cria uma seuqncia de numeros de 0 a 5 
for n in range(6):
    valor = float(input())

#se valor for maior que 0 
    if valor > 0:
        #incrementar 1 a quantia
        quantia += 1

print(f'{quantia} valores positivos')