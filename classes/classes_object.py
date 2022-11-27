# Chapter 9 : classes and objects

# PEP8: guidelines
# use combinations of lower case letters and underscores for:
# package, folder, file, variable (object of class), functions names
# use combinations of title case for:
# classes - attributes (variables), behaviour (functions)
# self keyword - shows that functions or variable belong in the current class ('this' keyword in java)
#

msg = 'wouf wouf'
breed = 'General'


def run():
    print(f'Nobody is running')


class Dog:
    """
    Model of dogs, template for dogs.
    """
    # attribute (description) - variables, instance variables
    name = 'a'
    # breed = 'no breed', no use because of __init__(self, name, breed, color)
    # color = '' , no use because of __init__(self, name, breed, color)
    # size = 'medium', no use because of __init__(self, name, breed, color, size='medium')
    age = '2'

    #   CONSTRUCTOR (of the class when you instantiate)
    # default functions to make required arguments
    # executed automatically everytime when you create an object (instance)
    def __init__(self, name, breed, color, size='medium'):
        self.name = name
        self.breed = breed
        self.color = color
        self.size = size

    # behaviour (actions) - functions
    def eat(self):
        # breed = ''
        print(f'{self.name} is eating ....')
        print(f'{self.name} wants more...')
        print(f'{self.name} done eating.')
        print(f"{self.breed}    {msg}")
        print(f"{self.breed}    {breed}")

    def run(self):
        miles = 5
        print(f'{self.name} is running {miles} miles')

    def get_description(self):
        # run()  # outside of the class
        # self.run()  # within the class
        print(f"Name of the dog: {self.name}")
        print(f"Breed of the dog: {self.breed}")
        print(f"Color of the dog: {self.color}")
        print(f"Size of the dog: {self.size}")
        print(f"Age of the dog: {self.age}")

# get_description()

# instantiation - creating instance of the class - creating object
# dog1, dog2 are the object

print("-------- dog1 ------------------------")
# dog1 = Dog()  # copying everything from the model to a new object
dog1 = Dog('chubby', 'chow chow', 'brown')  # copying everything from the model to a new object
print('name of the dog before: ', dog1.name)
dog1.name = 'trex'  # assigning the value to the attributes
print('name of the dog, after assigning new name: ', dog1.name)
dog1.eat()
dog1.breed = 'chow chow'
print('dog1 breed', dog1.breed)
dog1.size = 'small'
dog1.get_description()

print("-------- dog2 ------------------------")

dog2 = Dog('max', 'german sheppard', 'black', 'large')
print(dog2.name)
print(dog2.breed)
dog2.get_description()

