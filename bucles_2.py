from stringprep import c6_set


c=float(input("Ingrese el capital: "))

n = 0
b=2*c

while (c<b):
    c=1.05*c
    n=n+1

print("El capital se duplicará en ", str(n), " meses")
