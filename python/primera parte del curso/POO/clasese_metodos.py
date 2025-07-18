# objetos son instancias de las clases 
 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sal(self):
        print(f"Hola mi name es: {self.name} y tengo {self.age} años")

person1 = Person("ella","tantos")

# person1.sal()

# ejemplo de cuenta de banco 
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance 
        self.is_active = True
    
    # realizar un deposito

    def dep(self, amount):
        if self.is_active == True:
            self.balance += amount
            print(f"se ha depositado {amount}, el saldo acutal es: {self.balance}")
        else:
            print("Cuenta inactive")
    
    # sacar plata
        
    def withdraw(self, amount):
        if self.is_active == True:
            if amount <= self.balance:
                self.balance -= amount
                print(f"se ha sacadi {amount}$, el saldo acutal es: {self.balance}")
            else:
                print("monto superior a dinero en la cuenta")
        else:
            print("Cuenta inactiva")
    
    def deactivate_account(self):
        self.is_active = False
        print(f"Cuenta ha sido desactivada")
    
    def activate_account(self):
        self.is_active = True
        print(f"Cuenta ha sido activada")

account_me = BankAccount("Diego", 500)

account_me.deactivate_account()
account_me.dep(200)