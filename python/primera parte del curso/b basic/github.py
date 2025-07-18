# funciones son bloques de codigo que cumplen un obj especifico
# partes de la funcion  declaracion (aqui tambien se ponen parametros en caso de ser necesarios), igualdad de la funcion, implementacion
# los parametros de una funcion son datos que le ingresamos a la funcion para que trabaje con ellos

def suma(num1, num2):
    print(f"la suma de los elementos es: {num1+num2}")

def resta(num1, num2):
    print(f"la resta de los elementos es: {num1-num2}")

def mutl(num1,num2):
    print(f"la multiplicacion de los elementos es: {num1*num2}")

def divi(num1, num2):

    while num2 == 0:
        num2 = int(input("jmmmmm, por cero no se puede crack:"))
    print(f"la division de los elementos es: {num1/num2}")


def calc():
    numero1 = int(input("Ingresa por favor el primer numero para la operacion:"))
    numero2 = int(input("Ingresa por favor el segundo numero para la operacion:"))


    print("1. suma")
    print("2. Resta")
    print("3. Multi")
    print("4. Divi")


    opc = int(input("escribe el numero de la operacion que deseas:"))
    if opc == 1:
        suma(numero1,numero2)
    elif opc == 2: 
        resta(numero1, numero2)
    elif opc == 3:
        mutl(numero1, numero2)
    elif opc == 4:
        divi(numero1,numero2)


print("Bienvenido a la calculadora de Miguel")
# calc()


print("Calculadora de Mariana")
# calc()


mult_por_dos  = lambda x: x*2
print(mult_por_dos(34))

def mult2 (x):
    print(x*2)

mult2(34)

