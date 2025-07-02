#ITERADORES
#son elementos que establecen un iterador, el iterador debe actuar sobre un objeto iterable 

my_list = [1,2,3,4]

#obtener el iterador 
my_iter = iter(my_list)

#usar el iterador 
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print(my_list)

# iterador en strs

text = "objeto iterador"
iter_obj = iter(text)

for character in iter_obj:
    print(character)

print(text)

# ejemplo de iterador en para que itere solo numeros pares

last_number = 34
list_numbers_iter = []

iter_element = iter(range(0,last_number+1,2))

for number in iter_element:
    list_numbers_iter.append(number)
    print(number)

print(list_numbers_iter)


# generador - es el que crea elementos a partir de la funcion generadora de elementos

def generador():
    yield 1
    yield 2
    yield 3
    yield 4

for value in generador():
    print(value)


#generador de la sucecion de fibonacci 

def gene_fibo(limit):
    value = 0
    step = 1 
    while value < limit:
        yield value
        value, step = step, value + step

for num in gene_fibo(10):
    print(num)



#generado para los numeros pares e impares
print ("numero pares")

def num_par(x):
    numbers = 0 
    while numbers < x:
        if numbers % 2 == 0:
            yield numbers
        numbers += 1

for num in num_par(50):
    print(num)

print ("numero impares")

def num_par(x):
    numbers = 0 
    while numbers < x:
        if numbers % 2 == 1:
            yield numbers
        numbers += 1

for num in num_par(50):
    print(num)