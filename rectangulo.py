# sol Rectangulo

# cuantosCaben: int int int int -> int
# Retorna cuantos rectangulos de medida a,b caben en un rectangulo de medidas x,y
# Ej: cuantosCaben(1,2,2,3) retorna 3
def cuantosCaben(a,b,x,y):
    # Check area 
    # Chequeo si cabe horz o vert
    if (a*b > x*y) or (a>x and a>y) or (b>x and b>y):
        return 0
    #ver 2 casos y el max entre ellos
    #a por el eje x
    #b por el eje x
    ancho_ocupado = int(x/a) #usamos int para truncar y no tener decimales
    alto_ocupado = int(x/b)
    forma1= ancho_ocupado + cuantosCaben(a,b,x,y-b)
    forma2= alto_ocupado + cuantosCaben(a,b,x,y-a)
    return max(forma1,forma2)
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
    pass

#Tests
#Caso borde
assert cuantosCabenIso(1,2,1,2) == 0

#Caso general
assert cuantosCabenIso(1,2,4,8) == 6


