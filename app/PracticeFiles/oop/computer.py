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

    def __init__(self):
        #instance variable
        #instance namespace
        self.name = "BMW"
        self.model = "2020"


c1 = Car()
c2 = Car()
c1.wheels = 24
Car.wheels = 5
print(c1.wheels)
print(c2.wheels)


# com1 = Computer('i5', 16)
# com2 = Computer('Ryzen 5', 8)

# com1.config()
# com2.config()