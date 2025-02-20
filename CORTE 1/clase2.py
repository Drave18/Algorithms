#ARRAYS Y VECTORES
"""------------------------------------------------------------------------------------------------"""
import random

#Genera una lista de 10 pacientes con urgencia aleatorias entre 1 y 10

vector_pacientes = []
contador = 0
while contador <10:
    vector_pacientes.append(random.randint(1,10))
    contador +=1

print("Lista inicial de pacientes con urgencias aleatorias: ", vector_pacientes)

#Ordenar segun prioridad de urgencia
#Mayor urgencia = mayor numero

vector_pacientes.sort(reverse=True)
print("Pacientes ordenados por urgencia: ", vector_pacientes)
#Atender pacientes uno a uno
print("Atendiendo pacientes: ")
while len(vector_pacientes)>0:
    #pop removes
    paciente_atendido = vector_pacientes.pop(0)
    print(f"Atendiendo paciente con urgencia {paciente_atendido}...")
print("Todos los pacientes han sido atendidos. Vector de pacientes: ", vector_pacientes)

"""------------------------------------------------------------------------------------------------"""


# import numpy as np
# vector1 = np.array([1,2,3,4,5])
# print(vector1)

# vector2 = np.zeros(5)
# for i in range(len(vector2)):
#     vector2[i]= input("Ingresa un numero en la posicion {i}: ")
# print(vector2)    

#Una tienda quiere analizar sus ventas diarias de la semana y calcular la venta total, promedio, venta mas alta y venta mas alta

# import numpy as np
# ventas = np.zeros(7)

# for i in range(len(ventas)):
#   ventas[i]=float(input(f"Ingrese la venta del dia {i+1} : "))

# total_ventas = np.sum(ventas)
# venta_promedio = np.mean(ventas)
# venta_maxima = np.max(ventas)
# venta_minima = np.min(ventas)

# print("Reporte de Ventas semanales: ")
# print(f"Total de ventas: ${total_ventas:.2f}")
# print(f"Venta mas baja: ${venta_minima:.2f}")
# print(f"Venta mas alta: ${venta_maxima:.2f}")
# print(f"Venta promedio: ${venta_promedio:.2f}")


#Realice un programa que llene un array de numeros ingresados por el usuario
#Invierta el orden y duplique el vector invertido
#Imprime el array original, invertido y duplicado

import numpy as np 
numeros = np.zeros(int(input("Ingrese la cantidad numeros: ")))

for i in range(len(numeros)):
  numeros[i] = float(input(f"Ingrese el numero {i+1}: "))

numerosInvertidos = numeros[::-1] #flip() also can be used
numerosDuplicados = np.tile(numeros, 2)
#Manual way tile to get duplicates
"""import numpy as np

# Original 3D array
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Number of repetitions along each axis
reps = (2, 2, 2)

# Manually tiling the array
tiled_array = np.concatenate([np.concatenate([np.concatenate([array] * reps[2], axis=2)] * reps[1], axis=1)] * reps[0], axis=0)

print(tiled_array)
"""

print(f"El array original es: {numeros}, el array invertido es : {numerosInvertidos}, el array duplicado es {numerosDuplicados}")
