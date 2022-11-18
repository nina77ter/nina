# Chapter 9: Working with Classes and Instances

# OOPs concepts - class, object, encapsulation, inheritance, function overriding
# encapsulation - hiding from the object, child classes
class Car:
    # attribute - required, optional (default)
    # behaviour - CRUD -> set (create, update, delete), get(read), other functions (create, delete)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.__mileage = 0  # hiding from the object, child classes - encapsulation

    def get_description(self):
        """gets details of the car."""
        print(f"Car details: \tManufacturer: {self.make}\tModel: {self.model}\tYear: {self.year}")
        print(f"Current Mileage: {self.__mileage}")

    def set_mileage(self, new_mileage):
        """sets the mileage to not less than current mileage"""
        if new_mileage > self.__mileage:
            print("setting the new value a mileage")
            self.__mileage = new_mileage
        else:
            print("mileage was less than current mileage, mileage not updated.")

    def add_to_mileage(self, miles):
        """increments the mileage with given miles."""
        if miles > 0:
            self.__mileage = self.__mileage + miles
            # self.__mileage += miles  # does the same thing as line above
            print(f"{miles} miles were added to your car mileage")
        else:
            print("you can not give negative number to increment mileage, cheating ha")

    def fill_tank(self):
        print("Filling the tank with gas...")
        print("Done! It is ready to hit the road.")


class Bike:
    pass

# make = input("enter the make of the car: ")
# model = input("enter the model of the car: ")
# year = input("enter the year of the car: ")
# car2 = Car(make, model, year)

# COMMENTED LINES DUE TO IMPORT IN CLASS_INHERITANCE.PY MODULE (FILE)
# car1 = Car('bmw', 'x5', '2022')
# print(car1.make, car1.year + 1)
# print("## GETTER functions")
# car1.get_description()
# print("## SETTERs - updating the values of attributes")
# car1.model = 'X5 M'
# # car1.__mileage = 50 # since mileage is hidden from the object, now we cannot update the value
# car1.set_mileage(50)
# car1.get_description()
# # car1.__mileage = 10
# car1.set_mileage(10)
# car1.get_description()
# # input: 100, -15
# car1.add_to_mileage(100)
# car1.get_description()
# car1.add_to_mileage(-15)
# car1.get_description()