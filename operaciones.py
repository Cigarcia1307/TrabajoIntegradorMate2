from datetime import datetime

print("\n" + "="*50)
print("Bienvenidos al Trabajo Integrador 2 de Matematica".center(40))
print("="*50 + "\n")

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
dif_simetrica=set()
for elemento in E:
  if elemento not in F:
      dif_simetrica.add(elemento)

for elemento in F:
  if elemento not in E:
      dif_simetrica.add(elemento)

print("E Δ F =", dif_simetrica)

#Los dígitos que aparecen en C, P y F a la vez.
comunes=set()

C = {3, 2, 4, 9, 6, 5}
P = {2, 9, 5, 1}
F = {4, 6, 7, 2, 8, 1}

for elemento in C:
   if elemento in P:
      if elemento in F:
         comunes.add(elemento)

print("C ∩ P ∩ F =", comunes)

#Si hay más conjuntos con cantidad par de elementos que con cantidad impar, entonces se etiqueta como "grupo par".·    


E = {3, 4, 9, 1, 8, 2}
C = {3, 2, 4, 9, 6, 5}
H = {3, 7, 5, 9, 6, 4}
F = {4, 6, 7, 2, 8, 1}
P = {2, 9, 5, 1}

conjuntos = [("E", E), ("C", C), ("H", H), ("F", F), ("P", P)] #lista de tuplas (investigacion extra)

mayoria_pares = 0
mayoria_impares = 0

for nombre, conjunto in conjuntos: #nombre: 'E/ C/ H/ F/ P' , conjunto: {3,4,9,1,8,2}
    pares = sum(1 for n in conjunto if n % 2 == 0) # sum: funcion nativa que suma 1 cada vez que encuentra un numero par e itera sobre el conjunto
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


# Función que verifica si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def hay_anio_bisiesto(lista_anios):
    for anio in lista_anios:
        if es_bisiesto(anio):
            return True
    return False

# Ingreso de los años de nacimiento de los hombres del grupo
print("\nIngreso de años de nacimiento (solo los hombres del grupo):")
nombres_hombres = ["Fausto Gagliano", "Hernán Dichiara", "Pablo de la Puente"]
anios_nacimiento = []

for nombre in nombres_hombres:
    while True:
        anio_str = input(f"Ingresar el año de nacimiento de {nombre}: ")
        if not anio_str.isdigit():
            print("Debe ingresar un número entero positivo.")
            continue
        anio = int(anio_str)
        if anio < 1900 or anio > datetime.now().year:
            print("Por favor ingrese un año válido.")
        else:
            anios_nacimiento.append(anio)
            break

# Función que cuenta pares e impares de una lista de números
def contar_pares_impares(lista_numeros):
    pares = 0
    impares = 0
    for num in lista_numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


print("\n" + "="*40)
print("Análisis de Años de Nacimiento".center(40))
print("="*40)
pares, impares = contar_pares_impares(anios_nacimiento)
print(f"Años pares  : {pares}")
print(f"Años impares: {impares}")


# Función que Verifica si todos nacieron después del 2000
def es_grupo_z(anios):
    for anio in anios:
        if anio <= 2000:
            return False
    return True

if es_grupo_z(anios_nacimiento):
    print("Grupo Z")

# Verificación de año bisiesto
if hay_anio_bisiesto(anios_nacimiento):
    print("Tenemos un año especial")

# Calculo de edades actuales
anio_actual = datetime.now().year
edades = [anio_actual - anio for anio in anios_nacimiento]

# Producto cartesiano entre años y edades
print("\n" + "="*40)
print("Producto cartesiano entre años y edades".center(40))
print("="*40)
for anio in anios_nacimiento:
    for edad in edades:
        print(f"  ({anio}, {edad})")
  


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

# Suma total de los dígitos de cada DNI.
print("\nLa Suma de los digitos de cada DNI es:")
for i, dni in enumerate(dnis,1):
    suma_digitos =sum(int(d) for d in dni)

    print(f"DNI {i}: {suma_digitos}")


