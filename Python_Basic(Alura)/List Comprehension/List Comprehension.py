##inteiros = [1,3,4,5,7,8,9]
#pares = []
#for numero in inteiros:
#if numero % 2 == 0:
#pares.append(numero)

#Pesquise como o podemos usar o List Comprehension para fazer o mesmo que o código acima.

inteiros = [1,3,4,5,7,8]
pares  = [n for n in inteiros if n%2==0 ]
print(pares)