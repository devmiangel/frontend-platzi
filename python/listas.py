# comprehesion list
# son la manera de realizar lista de manera mas concisa e iterablemente dinamica#


# hallar los numero cuadrados de los numeros del 1 al 10

squares = [x**2 for x in range (1,11)]
print (squares)

c = [0,10,20,30,40]
f = [(x*9/5)*32 for x in c ]
print(f)

print("numeros pares")
pares = [x for x in range (1,100) if x%2==0]
print (pares)

print("numeros impares")
pares = [x for x in range (1,100) if x%2==1]
print (pares)

print("transpuesta de una matriz")
matrix = [[1,2,3],[4,5,6],[7,8,9]]

transposed = []

for index in range(len(matrix[0])):
    row_t = []
    for row in matrix:
        row_t.append(row[index])
    transposed.append(row_t)

print(transposed)

# matriz con conprehesion lists

new_transposed = [[row[index] for row in matrix] for index in range(len(matrix[0]))]

print(new_transposed)


# ejercicios de comprehesion list
# Doble de los Números
# Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el 
# doble de cada número usando una List Comprehension.

print("first exercise:")

numbers = [1, 2, 3, 4, 5]
new_list_doubel = [x*2 for x in numbers]
print (new_list_doubel)

# Filtrar y Transformar en un Solo Paso
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"]
# y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

print("second exercise:")

words = ["sol", "mar", "montaña", "rio", "estrella"]
new_words = [w.upper() for w in words if len(w) == 3]
print(new_words)


# Crear un Diccionario con List Comprehension
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] 
# y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.
print("thrid exercise:")
key = ["nombre", "edad", "ocupación"] 
value = ["Juan", 30, "Ingeniero"]

new_dictionary = {key[i]:value[i] for i in range(len(key))}
print (new_dictionary)

# pythonCopiar código
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Calcula la matriz traspuesta utilizando una List Comprehension anidada.
print("fourth exercise:")

matrix_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = [[row[index] for row in matrix] for index in range(len(matrix[0]))]
print ( transposed_matrix)

# Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:

# pythonCopiar código
# personas = [
#     {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#     {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
#     {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
#     {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
# ]
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

print("fiveth exercise:")

people = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

m_de_madrid = [espanoles["nombre"] for espanoles in people if espanoles["ciudad"] == "Madrid" and espanoles["edad"] > 30]
print(m_de_madrid)

# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

print("sixth exercise:")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [number*2 if number % 2 == 0 else number for number in numbers_list ]
print(new_numbers)

