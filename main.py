#class file
from tkinter.font import names


class student:
    first_name = 'John'
    last_name = 'Doe'
    gender = 'Male'
    age = 24

class person: #functions within a class are called methods
    def __init__(self, name, gender, marital_status,occupation):
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation

    def salutation(self):
        print(f"Good morning {self.name}, you are {self.gender}, and {self.marital_status}")

    def display_name(self):
        print(f"Good morning, I am {self.name} ")



#CREAT A VEHICLE CLASS AND IMPLEMENT 3 INSTANCES FROM IT
class dream_car:
    def __init__(self, type, model, year_of_manufacturing,engine_size):
        self.type = type
        self.model = model
        self.year_of_manufacturing = year_of_manufacturing
        self.engine_size = engine_size









