# RECURSIVIDAD - elementos que se llaman a si mismos 
# factorial de un numeo 

# SERIE DE FIBONACCI 
def fibonacci(pos):
    if pos == 0:
        return  0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)
# print(fibonacci(9))


# SUMATORIA DE NUMEROS NATURALES

def suma_naturales(num):
    if num <= 1:
        return num
    else:
        return num + suma_naturales(num-1)

# print(suma_naturales(5))

# CONTAR LOS DIGITOS DE UN NUMERO

def digit(numero):
    if numero <= 9:
        return 1
    else:
        return 1 + digit(numero//10)

# print(digit(1234567890))

# CONVERTIR UN NUMERO DE DECIMAL A BINARIO

def decimal(num):
    if num <= 1 :
        return str(num)
    else:
        return decimal(num//2) + str(num%2)

# print(decimal(512))

# suma de los digit de un numero
def sum_digit(number):
    if number <= 9:
        return number
    else:
        return sum_digit(number//10) + number % 10
        
        #

print(sum_digit(8575696))