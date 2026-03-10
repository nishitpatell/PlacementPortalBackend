class Student:

    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.addr = self.Address(city, country)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        self.addr.display_address()

    
    class Address:

        def __init__(self, city, country):
            self.city = city
            self.country = country

        def display_address(self):
            print("City:", self.city)
            print("Country:", self.country)


s1 = Student("Nikhil", 22, "Pune", "India")
s1.display()