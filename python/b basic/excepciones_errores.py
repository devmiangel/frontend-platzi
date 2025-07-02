# MANEJO DE ERRORES 
# cada try debe tener por lo almenos un except

try:
    divisior = int(input("div"))
    res = 100/divisior
    print(res)
except ZeroDivisionError:
    print("Error: El divisor no puede ser cero")
except ValueError:
    print ("error: introduce un numero crack")

# las excepcines tienen gerarquia y se pueden establecer los errores desde la clase padre

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)