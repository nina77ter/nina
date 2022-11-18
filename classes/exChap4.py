'''' \
'9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment

the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a

day of business.'
'''

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Name of the restuarant is: {self.restaurant_name}')
        print(f'This is: {self.cuisine_type} restaurant')

    def open_restaurant(self):
        print("Welcome everyone!we are open")

    def set_number_served(selfs):
        print()


restaurant1 = Restaurant("Brooklyn Pizza", "Italian")

print(f'Number of the restaurant is : {self.restaurant_number_served}')
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
