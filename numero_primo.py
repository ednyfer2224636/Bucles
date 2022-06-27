"""x=int(input("Digite un número: "))"""
m=int(2);
band="V";
numero=int(input("Favor ingresar el número: "));
while((band =="V")and(m<numero)):
      if((numero%m)==0):
            band="F";
      else:
            m=m+1;
if(band=="V"):
      print("El número leido es primo");
else:
      print("El número leido NO es primo");