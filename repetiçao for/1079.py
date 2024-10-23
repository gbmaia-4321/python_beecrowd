#informar quatas medias serao feitas
n = int(input())
#iniciar contador externo
soma = 0

#repetiçao controlada por n
for x in range(n):
    a, b, c = map(float,input().split())
    a *= 2 #multiplicar media pelo seu pese
    b *= 3 #multiplicar media pelo seu pese
    c *= 5 #multiplicar media pelo seu pese

    peso = 10 #peso total das medias

# imprimir o resultado que sera somado dentro do print
# a soma das medias dividida pelo peso total
    print(f'{((a + b + c) / peso):.1f}')
