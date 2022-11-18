#Chapter 9: Working with classes and intances
#OOPs concepts - class, object, child classes
# - hiding from the object, child classes


class Car:
    #attribute - required, optional (default)
    # behaviour - CRUD -> set, get, other
    def __init__(self, make, model, year):
        self.make =make
        self.model = model
        self.year = int(year)
        self.__mileage = 0   # hiding from the object, child classes - encapsulation

    def get_description(self):
        '''gets details of the car'''
        print(f'Car details: \nManufacturer: {self.make}\tModel:{self.model}\tYear{self.year}')
        print(f"Current Mileage: {self.__mileage}")

    def set_mileage(self, new_mileage):
# '''sets the mileage to not less than current mileage'''

        if new_mileage > self.__mileage:
           self.__mileage = new_mileage
        else:
            print('mileage was less than current mileage, cannot be done')

    def add_to_mileage(self, miles):

        self.__mileage = self.__mileage + miles

        print((f'{miles} miles were added to your milleagr'))



    #

car1 = Car('bmw', 'x5', '2022')
print(car1.make, car1.year)

print('## GETTER functions')
car1.get_description()
print('SETTERS -apdating the value of attributes')
car1.model = 'x5 M'
#car1.__mileage = 50 # setting a value
car1.set_mileage(50)
car1.get_description()
car1.set_mileage(10)
car1.get_description()
car1.add_to_mileage(100)
car1.get_description()




print('00000000000---------------=======================')

"""9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment

the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a

day of business."""