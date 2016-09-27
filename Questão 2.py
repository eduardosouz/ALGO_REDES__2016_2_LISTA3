numeros = []
par = []
impar = []

for i in range (20):
    numero = int(input('Digite um numero Inteiro:'))
    numeros.append(numero)

    if numero %2 == 0:
       par.append(numero)
    else:
        impar.append(numero)

print ('Todos os Numeros Digitados: ',numeros)
print ('Numeros pares: ',par)
print ('Numeros impares: ',impar)
