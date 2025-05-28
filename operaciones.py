""" 
print("\nBienvenidos al Trabajo Integrador 2 de Matematica\n")


lista = [ "Integrantes:", "Fausto Gagliano", "Eugenia Demarchi", "Pablo de la Puente", "Hernan Dichiara", "Cintia Garcia"]
ancho_maximo= max(len(nombre) for nombre in lista)

for nombre in lista:
    print(nombre.center(ancho_maximo))


#A. Operaciones con DNIs:

print("\nOperaciones con DNIs:")
print("Se realiza el trabajo con pares de DNIs")



dnis=[]
contador=0

while contador<2:
    dni=input(f"Por favor ingrese numero de DNI {contador + 1}:")
    dnis.append(set(dni))
    contador+=1
#Generación automática de los conjuntos de dígitos únicos
print("\nGeneración automática de los conjuntos de dígitos únicos:")
for i, dni in enumerate(dnis,1):
     dni_conjunto=set(dni)

     print(f"DNI {i}: {dni_conjunto}")
    
#Operaciones de conjuntos: Cálculo y visualización de: unión, intersección, diferencias y diferencia simétrica.
union= dnis[0]|dnis[1]
print("\nLa Union de ambos DNIs es:", union,"\n")
interseccion= dnis[0]&dnis[1]
print("\nLa Interseccion de ambos DNIs es:", interseccion,"\n")
diferencia= dnis[0]-dnis[1]
print("\nLa diferencia de DNI 1 con DNI 2 es:", diferencia,"\n")
diferencia= dnis[1]-dnis[0]
print("\nLa diferencia de DNI 2 con DNI 1 es:", diferencia,"\n")
diferencia_simetrica=dnis[0]^dnis[1]
print("\nLa diferencia simetrica entre el DNI 1 y el DNI 2 es: ", diferencia_simetrica, "\n")


#  Conteo de frecuencia de cada dígito en cada DNI utilizando estructuras repetitivas.
#para poder contar cada digito que se repite debo cambiar la estructura, de set a list
print("\nFrecuencia de dígitos en cada DNI:")
for i, dni in enumerate(dnis, 1):
    print(f"\nDNI {i}: {dni}")
    for digito in sorted(set(dni)): #en este caso el uso de 'set' es para que no se repita bucle interno
        print(f"'{digito}': {dni.count(digito)} veces")          

# Suma total de los dígitos de cada DNI.
print("\nLa Suma de los digitos de cada DNI es:")
for i, dni in enumerate(dnis,1):
    suma_digitos =sum(int(d) for d in dni)

    print(f"DNI {i}: {suma_digitos}") """


print("\nBienvenidos al Trabajo Integrador 2 de Matematica\n")

lista = [ "Integrantes:", "Fausto Gagliano", "Eugenia Demarchi", "Pablo de la Puente", "Hernan Dichiara", "Cintia Garcia"]
ancho_maximo = max(len(nombre) for nombre in lista)

for nombre in lista:
    print(nombre.center(ancho_maximo))

# A. Operaciones con DNIs:

print("\nOperaciones con DNIs:")
print("Se realiza el trabajo con pares de DNIs")

dnis = []
contador = 0

while contador < 2:
    dni = input(f"Por favor ingrese número de DNI {contador + 1}: ")
    dnis.append(dni)  # Guardamos la cadena original
    contador += 1

# Generación automática de los conjuntos de dígitos únicos
print("\nGeneración automática de los conjuntos de dígitos únicos:")
for i, dni in enumerate(dnis, 1):
    dni_conjunto = set(dni) #debemos cambiar la estructura de cadena a set, ya que buscamos digitos que no se repitan
    print(f"DNI {i}: {dni_conjunto}")

# Operaciones de conjuntos
set1 = set(dnis[0])
set2 = set(dnis[1])

print("\nLa Unión de ambos DNIs es:", set1 | set2)
print("\nLa Intersección de ambos DNIs es:", set1 & set2)
print("\nLa diferencia de DNI 1 con DNI 2 es:", set1 - set2)
print("\nLa diferencia de DNI 2 con DNI 1 es:", set2 - set1)
print("\nLa diferencia simétrica entre el DNI 1 y el DNI 2 es:", set1 ^ set2)

# Conteo de frecuencia de cada dígito
print("\nFrecuencia de dígitos en cada DNI:")
for i, dni in enumerate(dnis, 1):
    print(f"\nDNI {i}: {dni}")
    for digito in sorted(set(dni)): #en este caso el uso de 'set' es para que no se repita el bucle interno
        print(f"'{digito}': {dni.count(digito)} veces")


# Suma total de los dígitos de cada DNI.
print("\nLa Suma de los digitos de cada DNI es:")
for i, dni in enumerate(dnis,1):
    suma_digitos =sum(int(d) for d in dni)

    print(f"DNI {i}: {suma_digitos}")

#·Evaluación de condiciones lógicas (condicionales), vinculadas con las expresiones escritas.
# 'Los elementos que están en E o F pero no en ambos: '

E = {3, 4, 9, 1, 8, 2}
F = {4, 6, 7, 2, 8, 1}
diferencia_simetrica = E.symmetric_difference(F)
print("E Δ F =", diferencia_simetrica)

#Los dígitos que aparecen en C, P y F a la vez.

C = {3, 2, 4, 9, 6, 5}
P = {2, 9, 5, 1}
F = {4, 6, 7, 2, 8, 1}
interseccion = C & P & F
print("C ∩ P ∩ F =", interseccion)

#Si hay más conjuntos con cantidad par de elementos que con cantidad impar, entonces se etiqueta como "grupo par".·    

E = {3, 4, 9, 1, 8, 2}
C = {3, 2, 4, 9, 6, 5}
H = {3, 7, 5, 9, 6, 4}
F = {4, 6, 7, 2, 8, 1}
P = {2, 9, 5, 1}

conjuntos = [("E", E), ("C", C), ("H", H), ("F", F), ("P", P)]

mayoria_pares = 0
mayoria_impares = 0

for nombre, conjunto in conjuntos:
    pares = sum(1 for n in conjunto if n % 2 == 0)
    impares = sum(1 for n in conjunto if n % 2 != 0)
    print(f"Conjunto {nombre}: {pares} pares, {impares} impares")

    if pares > impares:
        mayoria_pares += 1
    elif impares > pares:
        mayoria_impares += 1

if mayoria_pares > mayoria_impares:
    print("Grupo par")
elif mayoria_impares > mayoria_pares:
    print("Grupo impar")
else:
    print("Igual cantidad de conjuntos con mayoría de pares e impares")
