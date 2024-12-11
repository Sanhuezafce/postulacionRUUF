# sol Rectangulo

# cuantosCaben: int int int int -> int
# Retorna cuantos rectangulos de medida a,b caben en un rectangulo de medidas x,y
# Ej: cuantosCaben(1,2,2,3) retorna 3
def cuantosCaben(a,b,x,y):
    # Casos bordes 
    
    # Algun lado mide 0
    if min(a,b,x,y)<1:
        return 0
    # Alguno de los lados del rect pequeno
    # es mayor que ambos lados del rect grande
    if (a>x and a>y) or (b>x and b>y):
        return 0

    #Ambos rectangulos son iguales
    if (a==x and b==y) or (a==y and b==x):
        return 1
        
    ancho1 = int(x/a)
    alto1 = int(y/a)
    ancho2 = int(x/b)
    alto2= int(y/b)
    
    #Chequeo para ver si cabe algun rectangulo pequeno en el grande
    if (ancho1 < 1) or (alto1 < 1):
        return 0
    else:
        #Se tesela el rect pequeno y se achica el grande
        forma1 = ancho1 + cuantosCaben(a,b,x,y-b)
        forma2 = alto1 + cuantosCaben(a,b,x-b,y)
        
    if (ancho2 < 1) or (alto2 < 1):
        return 0
    else:    
        #Mismo que para forma1, 2
        forma3 = ancho2 + cuantosCaben(a,b,x,y-a)
        forma4 = alto2 + cuantosCaben(a,b,x-a,y)
        
    return max(forma1,forma2,forma3,forma4)
#tests

#Tests provistos
assert cuantosCaben(1,2,2,4) == 4
assert cuantosCaben(1,2,3,5) == 7
assert cuantosCaben(2,2,1,10) == 0

#Tests casos bordes
assert cuantosCaben(0, 5, 10, 15) == 0
assert cuantosCaben(3, 5, 0, 10) == 0

#Tests rectangulos iguales
assert cuantosCaben(4, 6, 4, 6) == 1
assert cuantosCaben(3, 3, 3, 3) == 1
assert cuantosCaben(3, 5, 5, 3) == 1


# sol Isosceles

# cuantosCabenIso: int int int int -> int
# Retorna cuantos rectangulos x,y caben en un triangulo isosceles
# Ej: cuantosCabenIso(1,2,4,8) retorna 6
def cuantosCabenIso(x,y,h,b):
    sol = []
    #Voy armando un rect en cada altura posible del triangulo
    for i in range(h):
        # Busque la formula para el rectangulo inscrito y 
        # asi tengo las medidas para cada altura en el triangulo
        base_rectangulo = int(b * (1 - i/h))
        altura_rectangulo = i
        sol.append(cuantosCaben(x,y,base_rectangulo,altura_rectangulo))
    # Retorno el rect que permita agregar la mayor cant de rectangulos chicos
    return max(sol)

#Tests
#Caso borde
assert cuantosCabenIso(1,2,1,2) == 0

#Caso general
assert cuantosCabenIso(1,2,4,8) == 6


