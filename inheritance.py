class Order:
    def __init__(self, product, order_number, day):
        self.product = product
        self.order_number = order_number
        self.day = day
    def compile_data(self):
        order_details = {}
        order_details['product'] = self.product
        order_details['order_number'] = self.order_number
        order_details['day'] = self.day
        return order_details
    def statement(self):
        return f"Your order number for {self.product},order made on {self.day} is {self.order_number}"

order = Order("Micellar water", "1234nivea", "Monday")
print(order.compile_data())
print(order.statement())

class Purchase(Order): # Class purchase inheriting from class order
    def __init__(self, product, order_number, day):
        super().__init__(product, order_number, day)  # super function allows you to call a method fom the parent class.
    def  check_day(self):
        if self.day == "Sunday" or "Saturday":
            return "We will look at your order on Monday"
        else:
            return "Processing your order before the day ends."
purchase=Purchase("Blender", "1234Blender", "Sunday")
print(purchase.compile_data())
print(purchase.statement())
print(purchase.check_day())

class Confirm(Purchase):  #  class Confirm is inheriting from Purchase
    def __init__(self, product, order_number, day):
        super().__init__(product, order_number, day)
        self.confirmation_code = "123confirmed" #defining an attribute for the child class
    def confirm_message(self):  #  defining a method for a child class
        return f"Your confirmation code for order number {self.order_number} is {self.confirmation_code}"
    def check_day(self): #  overriding the method check_day in the parent class
        if self.day == "Friday":
            return "We cannot process your order today"
        else:
            return "Order shall be confirmed in a few"
confirm=Confirm("Fridge", "123Fridge", "Saturday")
print(confirm.compile_data())
print(confirm.statement())
print(confirm.check_day())
print(confirm.confirm_message())

class Delivery(Confirm):
    def __init__(self, product, order_number, day):
        super().__init__(product, order_number, day)
        self.delivery_fee = 200
    def delivery_message(self):
        return f"For {self.product},order number {self.order_number} the delivery fee is {self.delivery_fee}"
delivery=Delivery("micellar Water","123MIcellar","Sunday")
print(delivery.delivery_message())