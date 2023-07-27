import uuid
import datetime
import json
import cmd

class Products(cmd.Cmd):
    prompt = "$"
    intro = "Welcome to the Products console!"

    pay_rate = 0.08
    origin = "Nairobi"
    destination = "Momabasa"

    def __init__(self):
        super().__init__()
        self.products = []

    def do_add_product(self, arg):
        'Add a new product'
        name, price, quantity, category, customers = arg.split(",")
        product = {
            "id": str(uuid.uuid4()),
            "date": str(datetime.datetime.now()),
            "name": name,
            "price": int(price),
            "quantity": int(quantity),
            "category": category,
            "customers": int(customers)
        }
        self.products.append(product)
        print("Product added successfully.")

    def do_list_products(self, arg):
        'List all products'
        for product in self.products:
            print(product)

    def do_total_revenue(self, arg):
        'Give total revenue'
        for product in self.products:
            revenue = product["price"] * product["quantity"]
            print(f"{product['name']} revenue: {revenue}")

    def do_discount_rate(self, arg):
        'Calculate discount rate'
        for product in self.products:
            discount_rate = product["price"] * self.pay_rate
            print(f"{product['name']} discount rate: {discount_rate}")

    def do_purchase_date(self, arg):
        'Give purchase date'
        for product in self.products:
            print(f"{product['name']} purchase date: {product['date']}")

    def do_origin(self, arg):
        'Print origin of the product'
        print(f"Products is from {self.origin}")

    def do_print_destination(self, arg):
        'Give the destination of product'
        print(f"The product will arrive in {self.destination}")

    def do_print_category(self, arg):
        'Give category'
        for product in self.products:
            print(f"{product['name']} category: {product['category']}")

    def do_num_buyers(self, arg):
        'Number of customers served'
        for product in self.products:
            print(f"{product['name']} customers: {product['customers']}")

    def do_get_json_data(self, arg):
        'Get data from JSON file'
        with open("Test.json", "r") as f:
            data = json.load(f)
            print(data)

    def do_exit(self, arg):
        'Exit the console'
        return True

if __name__ == "__main__":
    Products().cmdloop()

