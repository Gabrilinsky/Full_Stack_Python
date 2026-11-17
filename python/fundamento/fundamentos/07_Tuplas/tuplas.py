# Tuplas
# 🎯 Objetivos
# Reconocer la sintaxis de las tuplas en Python

# Aprender cómo crear y consultar tuplas

# Entender cuándo puede utilizarse una tupla

# En el capítulo pasado aprendimos sobre listas, una estructura de datos que permite almacenar datos en base a un índice, hoy aprenderemos sobre tuplas. Las tuplas tienen el mismo funcionamiento que la lista, ambas nos permiten almacenar un conjunto de valores. La diferencia radica en que las tuplas son inmutables, es decir que no pueden ser modificadas. Crear una tupla es tan sencillo como declarar distintos valores separados por comas; opcionalmente podemos ponerlos entre los paréntesis ().

tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"
# Las tuplas agrupan un conjunto de elementos que pueden contener cualquier tipo de dato.

gato = ("Miu", 5, "persa", False)
# Las tuplas son útiles para representar lo que en otros lenguajes de programación se conocen como records o registros, ya que nos permiten unir información relacionada y utilizarla como una sola entidad.

# Para consultar la información de una tupla lo hacemos a través de su índice, tal como lo hacíamos con las listas.

print(gato[0]) #Imprime: Miu
# Recuerda que las tuplas son inmutables, por lo que al intentar cambiar el valor de algún índice obtendremos un TypeError:

gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assignment
# A pesar de esto, podemos agregar elementos a las tuplas o hacer slicing.

gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')
# 🛠️ Funciones integradas
#En el capítulo anterior mencionamos algunas funciones integradas para secuencias. Estas funciones podrán utilizarse para las tuplas también. Las más comunes son:

# len(secuencia): devuelve la longitud (cantidad de elementos) de una secuencia.
# max(secuencia): devuelve el valor más alto en una secuencia.
# min(secuencia): devuelve el valor más bajo en una secuencia.
# sorted(secuencia): devuelve una secuencia ordenada.
# sum(secuencia): devuelve la suma de los valores de la secuencia.
# Encuentra más funciones integradas para las secuencias aquí.

# 🧮 Tupla como valores return
# En los próximos capítulos aprenderás sobre funciones, a través de ellas podemos devolver un valor. Pero habrá ocasiones en que necesitemos devolver más de un valor, para esto podemos utilizar una tupla. Esta va a permitir agrupar más de un valor y devolverlos juntos. Por ejemplo, imaginemos que necesitamos una función que te regrese la sumatoria y la multiplicación de dos números:

def suma_multiplicacion(x, y):
   suma = x + y
   multiplicacion = x * y
   return (suma, multiplicacion)
# ❓ ¿Por qué usar tuplas?
# Inicialmente, las tuplas pueden parecer más complicadas para la manipulación de información, entonces ¿por qué utilizaría una tupla y no una lista?

# Las tuplas pueden almacenar información y al ser inmutables garantizan que otros desarrolladores que utilicen tu código no puedan modificar los conjuntos de datos que necesites que permanezcan constantes.