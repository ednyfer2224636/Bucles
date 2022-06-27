"""16"""
h=float(input("Digite la altura desde la que cae la pelota: "))

q=h/5
n=0

while h > q:
    h=(h-(0.10*h))
    n = n + 1
    print("Rebote #", n, "altura ", h)
print("Número de rebote en el que no alcanza la quinta parte de la altura", n) 