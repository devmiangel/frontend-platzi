class Student:
    def __init__(self, name, age, career):
        self.name = name
        self.age = age
        self.career = career
        self.grades = []
        self.approve = False

    def add_grade (self):
        note = float(input("Ingresa la nota: "))
        self.grades.append(note)
        print(f"se añadion la nota {note} a tu registro de calificaciones")
    
    def average(self):
        sum_grades = 0
        elements_in_grades = 0
        for grade in self.grades:
            elements_in_grades += 1 
            sum_grades += grade
        
        print(f"el promedio de tus notas es:{sum_grades/elements_in_grades}")
    
    def show_info(self):
        print(f"El nombre del estudiante es: {self.name}")
        print(f"La edad del estudiante es: {self.age}")
        print(f"El estudiante practica: {self.career}")
        print(f"Las notas del estudiante son:{self.grades}")
        self.average()
    
    def greet(self):
        print(f"Hola mi nombre es {self.name}, y ahora estoy en linea")

student1 = Student("Miguel", 21, "astronomia")


student1.greet()

student1.add_grade()
student1.add_grade()
student1.add_grade()

student1.show_info()



