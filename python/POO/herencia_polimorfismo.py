class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.buyable = True

    def sell(self):
        if self.buyable == True:
            self.buyable = False
            print(f"el carro {self.brand} {self.model} ha sido vendido")
        else:
            print(f"el carro {self.brand} {self.model} no esta disponible")
    
    def check_availability(self):
        return self.buyable

    def get_price(self):
        return self.price

class Customer:
    def __init__(self, name):
        self.name = name
        self.car_owned = []
    
    def buy_car(self,car):
        if car.check_availability():
            car.sell()
            self.car_owned.append(car)
        else:
            print(f"el carro {car.brand} {car.model} no esta disponible")
    
    def consulta(self,car):
        avaliable = "disponible" if car.buyable == True else "no disponible"
        print(f"el carro {car.brand} {car.model} cuesta {car.price} y está {avaliable}")
    
class Dealership:
    def __init__(self):
        self.costumers = []
        self.invetory = []
    
    def add_car(self, car):
        self.invetory.append(car)
        print(f"El carro {car.brand} {car.model} ha sido añadido al inventario")

    def register_costumer(self, costumer):
        self.costumers.append(costumer)
        print(f"el cliente {costumer.name} ha sido añadido")
    
    def show_allowed_cars(self):
        print("Carros disponibles")
        for car in self.invetory:
            if car.check_availability():
                print(f"-{car.brand} {car.model} por {car.get_price()}")

car1 = Car("Mazda", "Touring" , 21000)
car2 = Car("Ford", "Mustang" , 24000)
car3 = Car("Chevrolet", "Camaro" , 2000)

customer1 = Customer("tal")

dealership = Dealership()
# dealership.add_car(car1)
# dealership.add_car(car2)
# dealership.add_car(car3)

# dealership.register_costumer(customer1)
# dealership.show_allowed_cars()

# customer1.consulta(car1)
# customer1.buy_car(car1)

# dealership.show_allowed_cars()

# customer1.buy_car(car1)

#############################################################################
# herencia

class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"el vehiculo {self.brand} ha sido vendido")
        else:
            print(f"el vehiculo {self.brand} no esta disponible")

    def check_state(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
         

    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"el motor del carro {self.brand} esta arrancando"    
        else:
            return f"El carro {self.brand} no esta disponible"
        
    def start_engine(self):
        if self.is_available:
            return f"el motor del carro {self.brand} esta detenido"    
        else:
            return f"El carro {self.brand} no esta disponible"

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"la bicileta {self.brand} esta en marcha"    
        else:
            return f"la bicileta {self.brand} no esta disponible"
        
    def start_engine(self):
        if self.is_available:
            return f"la bicileta  {self.brand} esta detenida"    
        else:
            return f"la bicileta {self.brand} no esta disponible"

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"el camion {self.brand} esta en marcha"    
        else:
            return f"el camion {self.brand} no esta disponible"
        
    def start_engine(self):
        if self.is_available:
            return f"el camion {self.brand} esta detenida"    
        else:
            return f"el camion {self.brand} no esta disponible"
        
class Custo:
    def __init__(self, name):
        self.name = name
        self.car_owned = []
    
    def buy_car(self,car:Vehicle):
        if car.check_state():
            car.sell()
            self.car_owned.append(car)
        else:
            print(f"el carro {car.brand} {car.model} no esta disponible")
    
    def consulta(self,car):
        avaliable = "disponible" if car.is_available == True else "no disponible"
        print(f"el carro {car.brand} {car.model} cuesta {car.price} y está {avaliable}")

class Dealer:
    def __init__(self):
        self.costumers = []
        self.invetory = []
    
    def add_car(self, car:Vehicle):
        self.invetory.append(car)
        print(f"El carro {car.brand} {car.model} ha sido añadido al inventario")

    def register_costumer(self, costumer:Custo):
        self.costumers.append(costumer)
        print(f"el cliente {costumer.name} ha sido añadido")
    
    def show_allowed_cars(self):
        print("Carros disponibles")
        for car in self.invetory:
            if car.check_state():
                print(f"-{car.brand} {car.model} por {car.get_price()}")

car11 = Car("Toyota", "Corola", 20009)
bike1 = Bike("Yamaha", "Mt", 688)
truck1 = Truck("Volvo", "GW", 2000)

customer11 = Custo("Pepe")

deal = Dealer()
deal.add_car(car11)
deal.add_car(bike1)
deal.add_car(truck1)

deal.show_allowed_cars()

customer11.consulta(car11)

customer11.buy_car(car11)

customer11.consulta(car11)
