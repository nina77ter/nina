print("---------------- excercises 9-4 ------------------")
'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
'''


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name of the restaurant is : {self.restaurant_name}")
        print(f"This is {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"Welcome to {self.restaurant_name}! we are now Open!")

    def set_number_served(self, new_number_served):
        """
        Add a method called set_number_served() that lets you set the number of customers that have been served.
        """
        self.number_served = new_number_served

    def increment_number_served(self, num_served):
        """
        Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
        :param num_served: numbers that number_served to be incremented by
        :return:
        """
        self.number_served += num_served


# Make an instance called restaurant from your class.
restaurant1 = Restaurant("Brooklyn Pizza", 'Italian')

# Print the number of customers the restaurant has served
print(f"Number of customers restaurant served: {restaurant1.number_served}.")

# and then change this value and print it again
restaurant1.number_served = 15
print(f"Number of customers restaurant served: {restaurant1.number_served}.")

# Call this method with a new number and print the value again
restaurant1.set_number_served(20)
print(f"Number of customers restaurant served: {restaurant1.number_served}.")

# Call this method with any number you like that could represent how many customers were served in, say, a
# day of business.
restaurant1.increment_number_served(7)
print(f"Number of customers restaurant served: {restaurant1.number_served}.")

# H/W 9-5
# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166).
print('--------------- 9-5 -----------------\n')


class User:
    username = 'john'
    password = '$Today2023'

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age} y.o")
        print(f"Country: {self.country}")

    def greet_user(self):
        print(f"Welcome {self.first_name}, you are now logged in.\n")

    # Write a method called increment_
    # # login_attempts() that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        """number of login attempts will be incremented by 1"""
        self.login_attempts += 1

    # Write another method called reset_login_attempts() that resets the value of login_
    # # attempts to 0.
    def reset_login_attempts(self):
        """number of login attempts will be set to 0"""
        self.login_attempts = 0

    def login_to_website(self, username:str, password:str):
        if username.lower() == self.username and password == self.password:
            self.reset_login_attempts()
            print("You have logged in successfully. Welcome to your home page!")
        else:
            if self.login_attempts > 3:
                print("your account is blocked please try again later.")
            else:
                self.increment_login_attempts()
                print("your username or password was incorrect. Try again.")

# # Make an instance of the User class and call increment_login_attempts() several times.
user1 = User('Jessica', 'Lynn', 23, 'USA')
print(f"Welcome {user1.first_name} {user1.last_name} from {user1.country}.")
user1.increment_login_attempts()
print(f"Your login attempts = {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Your login attempts = {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Your login attempts = {user1.login_attempts}")

#  Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

user1.reset_login_attempts()
print(f"Your total login attempts set to: {user1.login_attempts}")
user1.login_to_website('john', 'as;ldfj')
print(f"1. Your total login attempts set to: {user1.login_attempts}")
user1.login_to_website('john', '$today2023')
print(f"2. Your total login attempts set to: {user1.login_attempts}")
user1.login_to_website('john', '$Today2023')
print(f"3. Your total login attempts set to: {user1.login_attempts}")
user1.login_to_website('John', '$Today2023')
print(f"4. Your total login attempts set to: {user1.login_attempts}")