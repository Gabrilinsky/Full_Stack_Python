# mayor_edad = True
# tiene_bigote = False
# print(mayor_edad)
# print(tiene_bigote)
# print({type(mayor_edad)})
# print({type(tiene_bigote)})
# mayoria_edad = 18
# altura = 1.72
# print(mayoria_edad)
# print(altura)

# rase = "Anita lava la tina"
# print(frase)

lista_vacia = [] # --> Arreglo o Lista
gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) #Imprime: Silvestre
gatos[1] = "Tom"  # Modificar el valor
gatos.append("Felix") # Añade un nuevo valor al final
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']
gatos.pop() #Elimina un elemento valor de la lista
print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']
gatos.pop(1)
print(gatos) #Imprime: ['Garfield', 'Hello Kitty']

# Tuplas: Tipo de datos inmutable (que no se puede modificar) y contiene un conjunto de distintos valores. Pueden contener distintos tipos de datos.
perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
print(perro[0]) #Imprime: Scooby Doo
perro[2] = "comida de perro" #ERROR: Las tuplas no pueden ser modificadas 
# perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
# print(perro[0]) #Imprime: Scooby Doo


# diccionario_vacio = {}
# persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}
# persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente
# persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# Agrega esa clave-valor si no existía previamente
# print(persona)

# Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}
# altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor
# print(altura)    # Imprime: 1.71
# print(persona) 

# salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 

# print(type(3.1416)) #Imprime: <class 'float'>
# print(type(persona)) #Imprime <class 'dict'>

# print(len(persona)) #Imprime: 4 (la cantidad de pares de clave-valor)
# print(len("Me encanta programar")) #Imprime: 20

# type
# print(type(1.1)) #Imprime: <class 'float'>
# print(type(615)) #Imprime: <class 'int'>
# print(type(2j)) #Imprime: <class 'complex'>

# Conversión
# entero_a_decimal = float(123)
# decimal_a_entero = int(22.5)
# entero_a_complejo = complex(35)
# print(entero_a_decimal) #Imprime: 123.0
# print(decimal_a_entero) #Imprime: 22
# print(entero_a_complejo) #Imprime: (35+0j)

# Numero Aleatorio
# import random
# num_aleatorio = random.randint(5, 10) #Genera un número aleatorio entre 5 y 10
# print(num_aleatorio) #Imprime el número aleatorio generado