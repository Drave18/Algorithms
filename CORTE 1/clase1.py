'''Programa que almacena un diccionario de países y sus capitales  {'Francia': 'París', 'Alemania': 'Berlín', 'Italia': 'Roma'},
 luego pregunta al usuario por un país y muestra su capital o un mensaje de aviso si el país no está.​'''
paises = {
    "Francia": "Paris",
    "Alemania": "Berlin",
    "Italia": "Roma"
}

pais = input("Ingrese el pais: ")

if pais in paises:
    print(paises[pais])
else:
    print("El pais no esta")

'''Second Version'''
paises = {
    "Francia": "Paris",
    "Alemania": "Berlin",
    "Italia": "Roma"
}
pais = input("Ingrese el pais: ").title()
print(paises.get(pais, "El pais no esta"))

'''Programa que solicita al usuario información sobre un producto (nombre, precio, cantidad) y la almacena en un diccionario.
 Después debe mostrar el mensaje "El producto <nombre> tiene un precio de <precio> y hay <cantidad> unidades en stock".'''


nombre = input("Ingrese el nombre: ")
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

informacion = {
    "nombre":nombre,
    "precio":precio,
    "cantidad":cantidad
}
print(informacion)
print(f'El producto {informacion["nombre"]} tiene un precio de {informacion["precio"]} y hay {informacion["cantidad"]} unidades en stock')





'''Crear un programa que almacene en una lista el gasto diario de una persona. Pedir al usuario la cantidad de dias a registrar. Luego,
visualizar la cantidad gastada cada dia
y tu total de gastos'''
gastoDiario = []
dias = int(input("Ingrese la cantidad de dias: "))


for i in range(0, dias):
    cantidad = int(input("Ingrese la cantidad gastada:"))
    gastoDiario.append(cantidad)
for i in range(len(gastoDiario)):
    print(f"El gasto del dia {i+1} fue {gastoDiario[i]}")
print("Gasto total: "+str(sum(gastoDiario)))

