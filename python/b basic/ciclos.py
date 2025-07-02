# el ciclo while
# continue break

# examen = True
# operacion_contador = 0

# while examen:

#     resultado = 0

#     operacion = int(input("elige la operacion (1 - suma 2 - resta 3 - multi 4 - divi 5 - salir):"))


#     if operacion == 5:
#         examen = False
#     else:
#         numero1 = int(input("Ingresa el numero 1:"))
#         numero2 = int(input("Ingresa el numero 2:"))
#         if operacion == 1:
#             resultado = numero1 + numero2
#         elif operacion == 2:
#             resultado = numero1 - numero2
#         elif operacion == 3:
#             resultado = numero1 * numero2
#         elif operacion == 4:
#             if numero2 != 0:
#                 resultado = numero1 / numero2
#             else:
#                 print("error")
#                 resultado = "resultado por divi cero no existe"
#         else:
#             print("opcion invalida intentalo de nuevo")
        
#         print("El resultado de la operacion es:", resultado)
#         operacion_contador += 1

# print(f"saliste de la calculadora y realizaste {operacion_contador} operaciones")

# for

fruits = ["manzana", "banana", "uva"]
for fruit in fruits:
    print(fruit)

for number in [1,2,5,534]:
    print(number)

text = "hola"
for letter in text:
    print(letter)


edades = [1,2,3,4,5,6,7]

mayor_edad = [18-edad for edad in edades]
print(mayor_edad)
