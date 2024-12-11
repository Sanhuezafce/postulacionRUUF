# sol Rectangulo

# cuantosCaben: int int int int -> int
# Retorna cuantos rectangulos de medida x,y caben en un rectangulo de medidas a,b
# Ej: cuantosCaben(1,2,2,3) retorna 3
def cuantosCaben(x,y,a,b): 
    pass

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


