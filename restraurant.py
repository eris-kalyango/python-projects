from datetime import datetime

def display_menu():
    print("==================== MENU ====================")
    print("==============================================")
    Menu = {
        "1. Burger": 10000,
        "2. Chicken": 15000,
        "3. Chips": 5000,
        "4. Pizza": 20000,
        "5. Soda": 2000

    }
    for i in Menu:
       print(i)



def make_order():
    item_number = int(input("Enter item number: "))
    Quantity = int(input("Enter item quantity:  "))
    print(f"{item_number} x{Quantity} added to your!")
    print("Do you want to make another Order!")
            





option = ""
while True:
    print("===================================================")
    print("             RESTAURANT SYSTEM                      ")
    print("\n==================================================\n")
    print("1. View Menu")
    print("2. Place Order")
    print("3. Calculate Bill")
    print("4. Generate Receipt")
    print("5. View Current Order")
    print("6. Save Order")
    print("7. Exit")

    option = int(input("Enter your choice please: "))

    if option == 1:
        display_menu()
    elif option == 2:
        make_order()
    
