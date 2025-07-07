# concecionario de vehiculos en donde se puede hacer la compra y venta de vehiculos, tambien se gestionara los vehiculos y usuarios, el ususario puede hacer la consulta del vehiculo, con su precio, que vehiculos estan disponibles y podra tambien comprar uno 

# EJEMPLO A ARREGLAR

class Client:
    def __init__(self, name, money):
        self.name  = name
        self.money = money

    def consulta (self, car):
        print(f"modelo: {car.model}")
        print(f"percio: {car.price}")
        print(f"kilometraje: {car.kilometer}")

class Vehicle:
    def __init__(self, price, model, kilometer, ouner, mark):
        self.mark = mark
        self.price = price
        self.model = model
        self.kilometer = kilometer
        self. ouner = ouner

class Concesionary:
    def __init__(self):
        self.vehicle_avaliable = []
        self.clients = []
    
    def sale(self, vehicle, client):
        if vehicle in self.vehicle_avaliable:
            if client.money >= vehicle.price:
                print(f"El vehiculo {vehicle.model} ha sido comprado por {client}")    
                self.vehicle_avaliable.remove(vehicle.model)
            else:
                print(f"no tienes los fondos suficientes para comprar este vehiculo {client}")
        else:
            print(f"el vehiculo {vehicle} no estra en nuestra lista de vehiculos")
    
    def buy (self, vehicle, price):
        if vehicle.ouner != "concecionario":
            print(f"Se realizo la compra del vehiculo {vehicle} a {vehicle.ouner} por el precio de ${price}")
        else:
            print(f"el vehiculo ya have parte del concecionario")

    def add_client(self,client):
        self.clients.append(client)
        print("cliente agregado")
    
    def add_car(self,car):
        self.vehicle_avaliable.append(car)
        print("vehiculo agregado")

    def show_vehicles(self):
        for cars in self.vehicle_avaliable:
            print(cars)


person1 = Client("yotas", 1000)
home = Client("concecionario", 2000000)

car1 = Vehicle(200, "Mazda 3", 0, person1, "Mazda")
car2 = Vehicle(200, "Mazda 2", 10, home, "Mazda")

consecionary = Concesionary.add_car(car2)


