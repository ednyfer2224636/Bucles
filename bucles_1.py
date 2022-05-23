N=int(input("Digite el valor de N: "))

i = 1
suma = 0

while (i <= N):
    suma = suma + i
    i = i + 1

print("La suma de los " + str(N) + " primeros valores es " + str(suma))