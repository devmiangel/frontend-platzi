# un decorado añade funcionalidad a una funcion 

""" def long_transaction(func):
    def wrapper():
        print('Log de la transaccion')
        func()
        print('Log terminado...')
    return wrapper

@long_transaction

def porcess_payment():
    print('Procesando el pago ...')

porcess_payment() """

# eje dos



def check_access(func):
    def acceso(employee):
        # comporbar si el empletado tiene rol admin
        if employee.get('rol') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO')
    return acceso

def platform_acces(func):
    def platform_element(employee):
        with open('platform_activity.txt', 'a') as file:
            file.write(func(employee))
    return platform_element


@platform_acces
def platform_historic(user):
    return f"el usuario {user['name']} ha ingresado al sitio"


@check_access
def delete_employee(employee):
    print(f"El impleado {employee['name']} ha sido eliminado")





admin = {'name': 'Carlos', 'rol': 'admin'}
employee = {'name': 'ana', 'rol': 'employee'}

# delete_employee(admin)
platform_historic(admin)



