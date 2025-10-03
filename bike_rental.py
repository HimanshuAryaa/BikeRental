


class BikeRentalSystem:
    def __init__(self, stock = 200, price = 100):
        self.stock = stock
        self.price = price
    def available_bike(self):
        print(f'''
        Available Stoke is {self.stock}''')
    def request_bike(self):
        print(f'''
        Available Stoke is {self.stock}''')
        try:
            a = int(input('''
            Enter the Qty you would like to rent:- 
            '''))
        except ValueError:
            print("\nInvalid input! Please enter a number.")
            return
        if a <= 0:
            print('''
            Enter the positive value or greater then zero
            ''')
        elif a > self.stock:
            print('''
            Quantity exceeded available Stocks
            ''')
        elif a <= self.stock:
            total_price = self.price * a
            print(f'''
            Qty = {a} 
            Price = {self.price}
            _________________ 
            Total price = {total_price}''')
            final_input = input('''
            Would you like to confirm your purchase? (Y/N) 
            ''').upper()
            if final_input == "Y":
                self.stock -= a
                print(f'''
                Thank You for purchasing
                Available Stoke is {self.stock}
                ''')
            elif final_input == "N":
                print('''
                Please come back again
                ''')

obj = BikeRentalSystem(200,10)
while True:
    try:
        first_input = int(input('''
            1. Display Available Stocks
            2. Request for Renting bikes (Price - Rs100 per bike)
            3. Exit
            Enter your choice: '''))
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        continue

    if first_input == 1:
        obj.available_bike()
    elif first_input == 2:
        obj.request_bike()
    elif first_input == 3:
        print("\nExiting the system. Goodbye!")
        break
    else:
        print("\nInvalid choice. Please try again.\n")


