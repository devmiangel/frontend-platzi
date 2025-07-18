# def nombre parametros

def greet(name):
    print ("hola mundo", "hola"+name)

# greet("Migue")

# en caso de que se desee poner un parametro por defecto es necesario establecer la igualdad

def area(base, altura = 2):
    print(base * altura)

# area (4,4)
# area (4)

# calculadora

def add(num1,num2):
    return num1 + num2

def sus(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

def calc():
       
    while True:
        print("Opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        option = int(input("Ingresa la opcion que deseas (1,2,3,4,5):"))
        if option == 5:
            print("Saliendo de la calculadora")
            break
        if option in [1,2,3,4]:
            num1 = float(input("Ingresa el numeo 1:"))
            num2 = float(input("Ingresa el numeo 2:"))
            if option == 1 :
                print("la operación es igual a:",add(num1, num2))
            if option == 2:
                print("la operación es igual a:",sus(num1, num2))
            if option == 3:
                print("la operación es igual a:",mul(num1, num2))
            if option == 4:
                print("la operación es igual a:",div(num1, num2))

# calc()

# funciones anonimas - lambda

add = lambda a,b: a + b
# print(add(12,4))

# ahora aplicado a arrays
# cuadrado de cada numero

numbers = range(11)
numbers_square = list(map(lambda x: x**2, numbers))
# print(numbers_square)

# seleccionar elementos si cumplen condicion filter

# numeros pares

event_number = list(filter(lambda x: x % 2 == 0, numbers))
# print(event_number)


# RECURSIVIDAD - elementos que se llaman a si mismos 
# factorial de un numeo 

def factorial(num):

    if num == 0:
        return 1 
    else:
        return num * factorial(num-1)

# print(factorial(30))

# SERIE DE FIBONACCI 

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num-2)

number = 35
# print(fibo(number))

# SUMATORIA DE NUMEROS NATURALES

def sumatoria(num):
    if num == 0:
        return 0 
    else:
        return num + sumatoria(num-1)

# print(sumatoria(5))

# INVERTIR UNA CADENA DE TEXTO

def invertir(text):
    if len(text) <= 1:
        return text
    else:
        return invertir(text[1:]) + text[0]

# print(invertir("1234"))

# PALINDROMO
def palin(text):
    if len(text) <= 1:
        return True
    else:
        palindro = palin(text[1:]) + text[0]
        if  palindro == text:
            return True
        else:
            return False
    

# print(palin("asd")

# POTENCIA DE UN NUMERO

def poten(num, pot):
    if pot <= 1:
        return num
    else:
        return  poten(num, pot-1) * num
    
# print(poten(2,5))

# CONTAR LOS DIGITOS DE UN NUMERO

def conteo(num):
    if num < 10:
        return 1
    else:
        return 1 + conteo(num//10)

# print(conteo(1233544752))


# SUMAR LOS DIGITOS DE UN NUMERO 

def digit(num):
    if num < 10:
        return num
    else:
        return num%10 + digit(num//10)
    
print(digit(12345))


# CONVERTIR UN NUMERO DE DECIMAL A BINARIO

def binary(num):
    if num <= 1:
        return str(num)
    else:
        return binary(num//2) + str(num%2)
    
print(binary(10))

# BUSQUEDA DE ELEMENTOS EN UNA LISTA

def busq(arr, ele):
    if len(arr) < 1:
        return False
    elif arr[0] == ele:
        return True
    else:
        return busq(arr[1:], ele)
        
    
print(busq([1,2,3,4,5,6,7],5))


# Conteo elemeentos en una lista

def contador(lista, canti):
    
    if len(lista) < 1: 
        return 0
    elif lista[0] == canti:
        return 1 + contador(lista[1:],canti) 
    else:
        return contador(lista[1:],canti)
    
print(contador([1,1,1,2],1))
        


# SUMAR ELEMENTOS DE UNA LISTA

def suma (lista):
    if len(lista) < 1:
        return 0
    else:
        return lista[0] + suma(lista[1:])

li = [1,2,3,4,5]
print(suma(li))