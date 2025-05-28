
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


