class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is", self.cpu, self.ram)

class Car:
    #class variable
    #class namespace
    wheels = 4

    def __init__(self, name, model):
        #instance variable
        #instance namespace
        self.name = name
        self.model = model

    @classmethod
    def wheel_info(cls):
        print("this method suggests that this is a class method")
        return cls.wheels
    
    @staticmethod
    def info():
        print("This is a static method")
        return "This is a car class"



c1 = Car("BMW", "X5")
c2 = Car("Audi", "A4")
c1.wheels = 24
Car.wheels = 5
print(c1.wheels)
print(c2.wheels)
print(Car.wheel_info())
print(Car.info())

# com1 = Computer('i5', 16)
# com2 = Computer('Ryzen 5', 8)

# com1.config()
# com2.config()