class User:  # defining a class called user using the class keyword
    def __init__(self, username, email):  # setting an initializer block
        self.username = username
        self.email = email
        self.age = 20
    def welcome(self):
        print(f"Your username is {self.username}")

user=User(input("Enter username: "),input("Enter email: "))  # creating an object from class user
user.welcome()  # calling the method welcome inside class User.
print(user.age)
print(user.email)  # accessing the attribute email of the object user.
user2 = User(input("Enter username: "), input("Enter email: "))  # creating another class user2 from class User
user2.welcome()
print(user2.email)



