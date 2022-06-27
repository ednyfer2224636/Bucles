pa=3500000
pb=5000000
ta=0.07
tb=0.05
año = 1980


while pa < pb:
    pa = pa + (pa * ta)
    pb = pb + (pb * tb)
    año = año + 1
    
print("Teniendo en cuenta la tasa de habitantes el año en que la poblacion A supera a la poblacion B es: ", año)