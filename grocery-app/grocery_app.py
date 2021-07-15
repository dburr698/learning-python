# You are responsible for creating an app that manages groceries. 
# Your groceries are characterized by Shopping Lists which can contain grocery items.
# Here are the features you need to implement:

shopping_list = []

class Store:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def add_item(self, item):
        self.items.append(item)

# A grocery item consists of a title, price, quantity.    
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

# Define a function to use when code is not written        
def incomplete_code():
    print("\nThis code is incomplete.")

def welcome():
    print("\nWelcome to your Grocery App!")
    
def farewell():
    print("\nThanks for using this Grocery App!")
    print("Have a nice day!\n")

def display_stores():
    print("\nStores in shopping list.") 
    for i in range(0, len(shopping_list)):
        print(f"{i + 1} - {shopping_list[i].name}")

def display_items():
    print("\nCurrent Shopping List:")
    for store in shopping_list:
        print(f"\n{store.name} located in {store.location}")
        for i in range(0, len(store.items)):
            print(f"{i + 1} - Item: {store.items[i].name} - Price: {store.items[i].price} - Quantity: {store.items[i].quantity}")


# You need to ask the user for the input.
# A user should be able to create a shopping list. 
# A shopping list consists of a title and address. 
# Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc

welcome()

while True:
    print("\nPress 1 to create a shopping list.")
    print("Press 2 to add items to your store lists.")
    print("Press 3 to display your lists.")
    print("Press 4 to delete a store from your list.")
    print("Press 5 to delete items from your store lists.")
    print("Press q to quit.")
    choice = input("\nSelect from the options above: ")
    # A user should be able to add multiple shoppings lists
    if choice == "1":
        while True:
            store = input("\nEnter the name of the store: ")
            location = input("Enter the location: ")
            new_store = Store(store, location)
            shopping_list.append(new_store)

            option = input("Would you like to create another list?(y/n): ")
            if option == "y":
                continue
            else:
                break

    
    # A user should be able to add a grocery items to a particular shopping list. 
    elif choice == "2":
        for i in range(0, len(shopping_list)):
            print(f"{i + 1} - {shopping_list[i].name}")
        
        while True:
            try:
                num = int(input("\nSelect the store number you would like to add items to: "))
            except ValueError:
                print("That was not a number!")
                break
            
            while True:
                name = input("\nEnter the item: ")
                price = float(input("Enter the item price: "))
                quantity = int(input("Enter quantity of items: "))
                # Create new class object based on input
                new_item = Item(name, price, quantity)
                # Add this new_item to items list in Store class
                shop_list = shopping_list[num - 1]
                shop_list.items.append(new_item)
                option = input("Would you like to add another item?(y/n): ")
                if option == "y":
                    continue
                else:
                    break
            break
    
    # Give user an option to display the list
    elif choice == "3":
        display_items()
    
    # User should be able to delete a store
    elif choice == "4":
        display_stores()
        num = int(input("\nEnter the number of the shopping list you would like to delete: "))
        for i in range(0, len(shopping_list)):
            if shopping_list[i] == shopping_list[num -1]:
                print(f"\nThe list for {shopping_list[i].name} has been deleted.")
                del shopping_list[i]
                break
        display_stores()

    # User should be able to delete an item from a particular store
    elif choice == "5":
        display_stores()
        store_num = int(input("\nEnter the number of the store you want to delete items from: "))
        store_list = shopping_list[store_num - 1]
        
        while True:
            for i in range(0, len(store_list.items)):
                print(f"{i + 1} - Item: {store_list.items[i].name} - Price: {store_list.items[i].price} - Quantity: {store_list.items[i].quantity}")
            item_num = int(input("Enter the number of the item you want to delete: "))
            for i in range(0, len(store_list.items)):
                if store_list.items[i] == store_list.items[item_num - 1]:
                    print(f"The item {store_list.items[i].name} has beed deleted.")
                    del store_list.items[i]

            delete_another = input("\nWould you like to delete another item?(y/n): ")
            if delete_another == "y":
                continue
            else:
                break


    elif choice == "q":
        farewell()
        break
    
    else:
        print("Invalid Option")



