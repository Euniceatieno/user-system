class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
    def statement(self):
        return f"Your username is {self.username} and your password is {self.password}"
user=User(input("Enter email: "), input("Enter username: "), input("Enter password: "))
print(user.statement())

class Admin(User):
    def __init__(self, email, username, password):
        super().__init__(email, username, password)
        self.privilleges=["Can post", "Can delete post", "can ban user"]
    def show_privilleges(self):
        statement = " "
        return f"An admin can join {statement.join(self.privilleges)}"
admin=Admin(input("Enter email: "), input("Enter username: "), input("Enter password: "))
print(admin.show_privilleges())
print(admin.statement())

class Manager(User):
    def __init__(self, email, username, password):
        super().__init__(email, username, password)
        self.passcode = "qwerty0987"
    def checkPasscode(self):
            if len(self.passcode) <= 10:
                return "You probably are not the admin"
            else:
                return "You can access account now."
manager=Manager("maina@yahoo.com","MAina","maina0987")
print(manager.checkPasscode())


