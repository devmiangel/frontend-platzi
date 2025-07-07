class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"hello my name is {self.name}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def greet(self):
        super().greet()
        print(f"and my Id is {self.student_id}")

student1 = Student("yo", 12 , "sdf124")
student1.greet()