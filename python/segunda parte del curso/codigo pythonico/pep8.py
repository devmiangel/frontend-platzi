""" 
3 principios importantes
el primero es la simplicidad - soluciones simples y  directas
Claridad - cualquier persona puede ser capaz de leer el codigo
eficiencia - crear las mejores solucione s

"""

""" 
Comentarios y docstrings 
docstrings son para metodos o funciones dando las caracterisitcas del metodo o funcion , los datos de entrada, salida y lo que se a descriptivo

mientras que los comentarios se usan para el funcionamiento de una linea de codigo

"""

""" 
las variable locales estan dentro de metodos clases o funciones

las variables globales pueden ser accedidas desde cualquier parte de codigo
    para acceder a variables globales desde una funcion se pone la palabra reservada global

nonlocal es una variable que no es ni local ni global 
    se usa en el caso de tener una variable local dentro de  una funcion, y se quiere acceder a esta desde una funcion anidada

"""

""" 

Anotaciones 
para variables - texto:str = "hola"
para funciones y metodos def name(name:str, age:int) -> str:
para clases
    class employee:
        name: str
        age: int
        salary: int
    
        def __init__(self, name, age, salary):
            self.name = name 
            self.age = age
            self.salary = salary
        
        def intro(self) -> str:
"""

""" 

Validacion de tipos en metodos 
para el retorno de la informacion en la generacion del mensaje es mejor poner un raise que tiene que ver con el error en si


def divide(a: int, b: int) -> float:
    # validar que los dos parametros sean enteros

    if not isinstance(a, int) or not is instance(b, int):
        raise TypeError('error: ambos parametros deben ser enteros o flotantes')

    
    if b == 0:
        print('Error: El divisor no puede ser cero')
        Return None
    
        return a/b

try:
    res = divide(10,'2')

except ValueError, TypeError as e:
    print(f'error: {e}')

"""