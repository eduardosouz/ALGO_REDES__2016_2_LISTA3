numeros = []
soma = 0
multiplicacao = 1

for i in range (10):
    numero = int(input('Digite um numero Inteiro:'))
    numeros.append(numero)

    soma = soma + numero
    multiplicacao = multiplicacao * numero

print ('Todos os numeros digitados: ',numeros)
print ('Soma: ', soma)
print ('Multiplicação: ', multiplicacao)