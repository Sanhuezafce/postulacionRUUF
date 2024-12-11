# sol Rectangulo

# cuantosCaben: int int int int -> int
# Retorna cuantos rectangulos de medida a,b caben en un rectangulo de medidas x,y
# Ej: cuantosCaben(1,2,2,3) retorna 3
def cuantosCaben(a,b,x,y):
    #ver 2 casos y el max entre ellos
    #a en el x
    #b en el x
    ancho1 = int(x/a)
    alto1 = int(y/a)
    ancho2 = int(x/b)
    alto2= int(y/b)
    
    if (ancho1 or alto1) < 1: #chequeo las cond en este paso
        return 0
    else:
        #en cada llamado recursivo revisamos el trozo del rectangulo que sobro
        forma1= ancho1 + cuantosCaben(a,b,x,y-b) 
        
    if (ancho2 or alto2) < 1:
        return 0
    else:    
        forma2= alto2 + cuantosCaben(a,b,x,y-a)
    print("RectaGrande: ",x,y,"Forma1: ",forma1)
    print("RectaGrande: ",x,y,"Forma2: ",forma2)
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


