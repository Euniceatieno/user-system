class Customer:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.login_attempts = 2
    def increment_attempts(self):
        self.login_attempts += 1  #  modifying attributes
        self.login_attempts = 0
        return self.login_attempts
customer = Customer(input("Enter name: "), input("Enter password: "))
print(customer.increment_attempts())
print(customer.reset_attempts())


