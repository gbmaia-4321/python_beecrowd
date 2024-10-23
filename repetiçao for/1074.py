#ler a quantidade de valores que serao lidos
qtd_entradas = int(input())

#for vai contar o numero de entradas fornecidos 
for x in range(qtd_entradas):
  num  = int(input())
# se num == 0 
  if num == 0:
    #nulo
    print('NULL')
#caso contrario
  else:
        #ele for par 
        if num % 2 == 0:
            #sera even     
            print('EVEN', end=' ') #o end impede que uma nova linha seja criada, entao o proximo print seguira a frente 
        else:
            print('ODD', end=' ')
        
        if num > 0:
            print('POSITIVE')
        else:
            print('NEGATIVE')
    

