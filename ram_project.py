
class Product:
    def __init__(self, name, brand, price, quality):
        self.name = name
        self.brand = brand
        self.price = price
        self.quality = quality

    def __str__(self):
        return f"Name: {self.name}\nBrand: {self.brand}\nPrice: {self.price}\nQuality: {self.quality}"


class Customer:
    def __init__(self, name, contact, address, date, time):
        self.name = name
        self.contact = contact
        self.address = address
        self.date = date
        self.time = time

    def __str__(self):
        return f"Name: {self.name}\nContact: {self.contact}\nAddress: {self.address}\nDate: {self.date}\Time: {self.time}"


class Order:
    def __init__(self, product, customer, purchused_date, purchused_time):
        self.product = product
        self.customer = customer
        self.purchused_date = purchused_date
        self.purchused_time = purchused_time
        
    def __str__(self):
        return f"Product:\n{self.product}\nCustomer:\n{self.customer}\nPurchused_Date:{self.purchused_date}\nPurchused_Time:{self.purchused_time}"


class OnlineShoppingStore:
    def __init__(self):
        self.product = []
        self.customer = []
        self.order = []

    def add_product(self, product):
        self.product.append(product)
        print("Product Details Added Successfully. \n**Please click the 2nd option Booking your order**")

    def add_customer(self, customer):
        self.customer.append(customer)
        print("Your Order Booked Successfully. \n**Please click on 3rd option**")

    def order_purchused(self, product_name, customer_name, purchused_date, purchused_time):
        product = next((p for p in self.product if p.name == product_name), None)
        customer = next((c for c in self.customer if c.name == customer_name), None)

        if product and customer:
            order = Order(product, customer, purchused_date, purchused_time)
            self.order.append(order)
            print("Your Order Delivered on successfully. \n**Thank you!** \n**please click on 4th option viewing your order lists**")
        else:
            print("Product or customer not found. Please check the names.")

    def list_order(self):
        if self.order:
            for index,order in enumerate(self.order, start=1):
                
                print(f"\nOrder {index}:\n{order}")
        else:
            print("No orders purchused.")

def main():
    online_shopping = OnlineShoppingStore()
    
    while True:
        print('\n',"Rambo online shopping store:")
        print("Enter 1 Add Product Details")
        print("Enter 2 Customer Details and Order Booking")
        print("Enter 3 Purchusing Orders")
        print("Enter 4 List Of Orders")
        print("Enter 5 Exit")
        choice = input("Choose any Options: ")

        if choice == "1":
            print("Enter your Product and put in the Details:")
            name = input("Enter Product name: ")
            brand = input("Enter Brand name: ")
            price = input("Enter product price: ")
            quality = input("Enter type of Quality: ")
            product = Product(name, brand, price, quality)
            online_shopping.add_product(product)
        elif choice == "2":
            print("Booking Order and Customer Details:") 
            name = input("Enter customer name: ")
            contact = input("Enter customer's contact: ")
            address = input("Enter customer's Address: ")
            date=input("Enter order Delivery date: ")
            time=input("Enter order Delivery time: ")
            customer = Customer(name, contact, address, date, time)
            online_shopping.add_customer(customer)
        elif choice == "3":
            print("Delivering your Order Details:") 
            product_name = input("Enter product's name: ")
            customer_name = input("Enter customer's name: ")
            purchused_date = input("Enter order purchused date: ")
            purchused_time = input("Enter order purchused time: ")
            online_shopping.order_purchused(product_name, customer_name, purchused_date, purchused_time)
        elif choice == "4":
            print("Orders List:")
            online_shopping.list_order()
        elif choice == "5":
            print("Exiting Online Shopping Products.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


     
    


# In[ ]:




