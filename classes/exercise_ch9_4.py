# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
#
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
#
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Name of the restuarant is: {self.restaurant_name}')
        print(f'This is: {self.cuisine_type} restaurant')

    def open_restaurant(self):
        print("Welcome everyone!we are open")


restaurant1 = Restaurant("Brooklyn Pizza", "Italian")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print('======--9-2--=======')
'''
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
'''
restaurant2 = Restaurant('Pyramyda', 'Egypt')
print(restaurant2.restaurant_name)
print(restaurant2.cuisine_type)
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Chapotly', 'Mexican')
print(restaurant3.restaurant_name)
print(restaurant3.cuisine_type)
restaurant3.describe_restaurant()

print('==========   9-3 ===========')
'''9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.'''

class User:
    def __init__(self, first_name, last_name, date_of_birth, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.address = address

    def describe_users(self):
        print(f'The user  first name is {self.first_name}')
        print(f'The user last name is {self.last_name}')
        print(f'The user day of birth is {self.date_of_birth}')
        print(f'The user phone number is {self.phone_number}')
        print(f'The user address is {self.address}')

    def greeting_to_the_user(self):
        print(f'Hello, {self.first_name}! Welcome!')

User1 = User ('Michael', 'Fisher', '10.11.1091', '731-112233', 'Brooklyn')
print(User1.first_name, User1.last_name, User1.date_of_birth, User1.phone_number, User1.address)
User1.describe_users()
User1.greeting_to_the_user()

User2 = User ('Sergii', 'Sokol', '08.15.1981', '731-192288', 'Jackson')
print(User2.first_name, User1.last_name, User1.date_of_birth, User1.phone_number, User1.address)
User2.describe_users()
User2.greeting_to_the_user()

print('********======== 9-4 ========================')
'''9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment

the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a

day of business.'''
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Name of the restuarant is: {self.restaurant_name}')
        print(f'This is: {self.cuisine_type} restaurant')

    def open_restaurant(self):
        print("Welcome everyone!we are open")

    def set_number_served(self, new_num_served):
        self.number_served = new_num_served
    def increment_number_served(self, num_served):
        self.number_served += num_served

restaurant1 = Restaurant("Brooklyn", "italian")

print(f"Number of  customers restuarant served: {restaurant1.number_served}")

restaurant1.number_served = 15
print(f"Number of customers resturant served: {restaurant1.number_served}")

restaurant1.set_number_served(20)
print(f"Number of customers restaurant served: {restaurant1.number_served}")

restaurant1.increment_number_served(7)
print(f"Number of customers restaurant served: {restaurant1.number_served}")

print('********======== 9-5 ========================')
'''9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.'''

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0


    def increment_login_attempts  (self, login_attempts):
        self.login_attempts += 1


    def reset_login_attempts(self, reset):

        self.reset_login_attempts = reset



    # def describe_users(self):
    #     print(f'The user  first name is {self.first_name}')
    #     print(f'The user last name is {self.last_name}')
    #
    #
    # def greeting_to_the_user(self):
    #     print(f'Hello, {self.first_name}! Welcome!')

User1 = User ('Michael', 'Fisher')
print(User1.first_name, User1.last_name)
# User1.describe_users()
# User1.greeting_to_the_user()

# User2 = User ('Sergii', 'Sokol')
# print(User2.first_name, User1.last_name)
# User2.describe_users()
# User2.greeting_to_the_user()
User1.increment_login_attempts(4)
print(f'Your attempt is: {User1.login_attempts}')

User1.reset_login_attempts(0)
print('Your attempts are reset')


# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.