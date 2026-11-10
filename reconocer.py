"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random


nombre = "Frida Kahlo"
print(type(nombre))
print(len(nombre))


edad = 25


if edad < 18:
   print("Eres menor de edad.")
elif edad == 18:
   print("Tienes 18 años.")
else:
   print("Eres mayor de edad.")


frutas = ["manzana", "pera", "fresa"]
print(frutas[0])
frutas[0] = "banana"
frutas.append("uva")
frutas.remove("pera")


dimensiones = (200, 50)
print(dimensiones[0])


persona = {
   "nombre": "Carlos",
   "edad": 30
}
print(persona["nombre"])
persona["edad"] = 31
persona["ciudad"] = "Santiago"
del persona["ciudad"]


for i in range(5):
   if i == 2:
       continue
   if i == 4:
       break
   print(i)


contador = 0
while contador < 3:
   print(f"while contador es: {contador}")
   contador += 1


def saludar_usuario(nombre):
   return f"Hola, {nombre}"


print(saludar_usuario("Francisca"))