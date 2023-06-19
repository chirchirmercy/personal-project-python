class Farmer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()

    def add_product_to_cart(self, product):
        return self.shopping_cart.add_product(product)

    def remove_product_from_cart(self, product):
        return self.shopping_cart.remove_product(product)

    def view_cart(self):
        return self.shopping_cart.view_cart()

    def process_orders(self):
        return self.shopping_cart.process_orders()

class Customer:
    def __init__(self, name, email, location, phoneNumber):
        self.name = name
        self.email = email
        self.location = location
        self.phoneNumber = phoneNumber
        self.total_purchase = 0

    def add_purchase(self, amount):
        self.total_purchase += amount

    def remove_purchase(self, amount):
        if self.total_purchase >= amount:
            self.total_purchase -= amount
        else:
            print("Error: The amount to remove exceeds the total purchase.")

    def discount(self):
        if self.total_purchase >= 100:
            return 0.1
        return 0.0

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_details(self):
        return f"Product: {self.name}\nPrice: {self.price} Ksh"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        return f"{product.name} added to the farmer's shopping cart."

    def remove_product(self, product):
        self.products.remove(product)
        return f"{product.name} removed from the farmer's shopping cart."

    def view_cart(self):
        if self.products:
            cart_details = "\n".join([product.display_details() for product in self.products])
            return f"Farmer's Shopping Cart:\n{cart_details}"
        else:
            return "The farmer's shopping cart is empty."

    def process_orders(self):
        if self.products:
            order_details = "\n".join([product.display_details() for product in self.products])
            self.products = []
            return f"The farmer has processed the following orders:\n{order_details}"
        else:
            return "No orders to process."

# Example usage
farmer = Farmer("John")

product_name = "Tomatoes"
price = 50.0

product = Product(product_name, price)
print(farmer.add_product_to_cart(product))
print(farmer.view_cart())

print(farmer.remove_product_from_cart(product))
print(farmer.view_cart())

print(farmer.process_orders())


def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(1998, 9, 3)

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def display_product_details(self):
        return f"Buy {self.name} today with only {self.price} Ksh with {self.description}."


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    while True:
        choice = input("Enter your choice (1-5): ")
       
        if choice == "1":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = add(num1, num2)
            print("Result:", result)
        elif choice == "2":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == "3":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == "4":
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = divide(num1, num2)
            print("Result:", result)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    calculator()

product = Product("widget",50.0,"high quality")
print(product.display_product_details())


# Test the methods
customer1 = Customer("Mwangi", "mwangi@gmail.com", "Kasarani", "5234-456-987")

customer1.add_purchase(120)
print(customer1.total_purchase)  

customer1.remove_purchase(50)
print(customer1.total_purchase)  

customer1.remove_purchase(100)
print(customer1.total_purchase)  

print(customer1.discount()) 
