#Conceptos de programacion funcional

#1. Funciones son ciudadanos de primer orden: Parametros. retornos, asignar variables

from functools import reduce

import math

def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    if b != 0:
        return a/b

val1 = int(input("Ingrese el primer valor: "))
val2 = int(input("Ingrese el segundo valor: "))
opt = int(input("Ingrese la operacion: 1. Suma 2. Resta 3. Multiplicacion 4. Division"))

if opt == 1:
    operacion = suma
elif opt == 2:
    operacion = resta
elif opt == 3:
    operacion = multiplicacion
elif opt == 4:
    operacion = division
else:
    print("Operacion no valida")

print(f"El resultado es: {operacion(val1, val2)}")

#2. Funciones puras: Solo usan parametros para recibir valores, no tocan variables globales
# con las mismas entradas, producen mismos resultados (como ejemplo las operaciones de arriba)
# Si toca variables globales o modifica los valores de entrada (generar nuevos datos), la funcion no es pura

#3. Funciones anonimas (lambda): Una funcion en terminos genericos
# lambda x: x % 2 == 0, recibe un parametro y retorna la evaluacion, tiene las mismas caracteristicas
# de una funcion

num = int(input("Ingrese un numero cualquiera: "))
es_par = lambda x: x % 2 == 0
print(f" {num} es par?: {es_par(num)}")

#4. Funciones de orden superior:
# Son funciones que reciben como parametros otras funciones
# a. Funcion MAP: Normalizar un conjunto de datos map(funcion, coleccion de datos) genera una nueva lista
#                 mapeando cada uno de los elementos de la lista
# b. Funcion FILTER:
# c. Funcion REDUCE:

#Forma larga:
#Es una funcion pura?
# Si es pura porque no toca variables, globales y los datos de entrada no son modificados para nada
# Solo se crea una copia

ciudades = ["Cali", "medellin", "BOGOTA", "bArrAnQuillA"]

def normalizar_datos(lista_nombres):
    datos_norm = []
    for nombre in lista_nombres:
        datos_norm.append(nombre.capitalize())
    return datos_norm

ciudades_norm = normalizar_datos(ciudades)
print(f"Ciudades sin normalizar: {ciudades}")
print(f"Ciudades normalizadas: {ciudades_norm}")

# Ejemplo con la funcion map, sin funcion lambda
def capitalizar(palabra):
    return palabra.capitalize() #capitalize es para retornar la palabra con la inicial en mayuscula

ciudades_norm2 = list(map(capitalizar, ciudades))
print(f"Datos normalizados: {ciudades_norm2}")

#Ejemplo con la funcion map, usando lambda
ciudades_norm3 = list(map(lambda n: n.capitalize(), ciudades))
print(f"Datos normalizados: {ciudades_norm3}")

#map: aplicar una funcion a coleccion de obj   filter: filtra una lista aplicando una funcion   reduce: consolida los valores de una lista

def aplicar_operacion(operacion, operando1, operando2):
    return operacion(operando1, operando2)

print(f"el resultado es :{operacion(val1, val2)}")
#usando la funcion de orden superior

edades = [12, 14, 18, 19, 24, 25, 28]
personas = [{"nombre":"diego","edad":"15"},
            {"nombre":"caroliana","edad":"10"},
            {"nombre":"diana","edad":"14"},
            {"nombre":"sebastian","edad":"24"}
            ]

print(personas[0]["nombre"])
print(f"\nnombres sin filtrar:{personas}")

#la funcion de filtro debe ser una funcion booleana:
def filtrar_mayores_edad(edad):
    return edad >= 18

def filtrar_personas_mayores(persona):
    return int(persona["edad"]) >= 18

personas_mayores = list(filter(filtrar_personas_mayores, personas))
print(f"personas mayores de edad:{personas_mayores}")

mayores_edad = list( filter( filtrar_mayores_edad, edades))
print(f"Mayores de edad:{mayores_edad}")

#generar una lista de numeros del 1 a 100:
numeros = list(range(1,101))

#sumarlos con un iterador
sum = 0
for i in numeros:
    sum = sum + i

print(sum)

#sumar con reduce y una funcion lambda:
suma = reduce(lambda a,b:a+b, numeros)
print(suma)

n = int(input("ingrese el numero de terminos"))
nums = list(range(1,n+1))
print(nums)

def fun_map(n):
    pass

def fun_redux(a,b):
    pass

aprox = reduce(fun_redux, list(map(fun_map, nums)))
print(f"valor aproximado para euler")

