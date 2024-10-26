x = int(input())
y = int(input())

# se x for maior que y
if x > y:
    # inverter os valores
    aux = x
    x = y
    y = aux

for n in range(x + 1, y): #o range vai fazer contar 1 num apos o x ate y
    
    if n % 5 == 2 or n % 5 == 3:
        print(n)