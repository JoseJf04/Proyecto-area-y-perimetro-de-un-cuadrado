#Funcion Calcular el area del cuadrado
def calcular_area(long_lad):
    area = long_lad ** 2
    return area

#Funciom Calcular perimetro del lado
def calcular_perimetro(long_lad):
    perimetro = long_lad * 4
    return perimetro

# solicitar la longitud del lado
longitud_lado = float(input("Ingresa la longitud de un lado del cuadrado en cm: "))

#Calcular area del cuadrado
area_cuadrado = calcular_area(longitud_lado)

#Calucular perimetro del cuadrtado
perimetro_del_cuadrado = calcular_perimetro(longitud_lado)

#Mostrar resultado

print(f"El area del cuadrado con lado {longitud_lado} es:{area_cuadrado} y su perimetro es:{perimetro_del_cuadrado}")