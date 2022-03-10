# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# DAlbano,3.8.22,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products'  name
        product_price: (float) with the products' standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DAlbano,3.8.22,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self,product_name: str, product_price: float):
        # 	   -- Attributes --
        self.__product_name = str(product_name)
        self.__product_price = float(product_price)

    # -- Properties --
    # product_name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value:str):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    # product price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric():
            self.__product_price = value
        else:
            raise Exception("Prices must be numbers")

    # -- Methods --
    def to_string(self):
        return self.__str__()

    def __str__(self):
        return self.product_name + ',' + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DAlano,3.8.22,Modified code to complete assignment 8
    """
    @staticmethod
    def read_data_from_file(file_name:str):
        list_of_product_rows = []
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = Product(data[0], data[1])
            list_of_product_rows.append(row)
        file.close()
        return list_of_product_rows

    @staticmethod
    def save_data_to_file(file_name:str, list_of_product_objects:list):
        file = open(file_name, "w")
        for product in list_of_product_objects:
            file.write(product.__str__() + "\n")
        file.close()

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """Performs Input and Output tasks:

    methods:
    show_menu():

    get_user_choice():
    # strChoice = ""

    show_current_data(list_of_rows):

    add_new_items()

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DAlano,3.8.22,Modified code to complete assignment 8
    """

    @staticmethod
    def show_menu():
        print('''
        Menu of Options
        1) Show current data
        2) Add new item
        3) Save data to file
        4) Exit program
        ''')
        print()

    @staticmethod
    def get_user_choice():
        strChoice = str(input("Which option would you like to perform [1 to 4]: ").strip())
        print()
        return strChoice

    @staticmethod
    def show_current_data(list_of_rows:list):
        print("The current products are:")
        for row in list_of_rows:
            print(row.product_name + ' (' + str(row.product_price) + ')')
            print()

    @staticmethod
    def add_new_item():
        name = str(input("What is the product name?  ").strip())
        price = float(input("What is the product price?  ").strip())
        print()
        p = Product(product_name=name, product_price=price)
        return p

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #

try:
    listOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        IO.show_menu()
        strChoice = IO.get_user_choice()

        if strChoice == '1':
            IO.show_current_data(listOfProductObjects)
            continue

        elif strChoice == '2':
            lstOfProductObjects.append(IO.add_new_item())
            continue

        elif strChoice == '3':
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue

        elif strChoice == '4':
            print("Goodbye")
        break

except Exception as e:
    print("Text file must exist before running this script")
    print(e, e.__doc__, type(e), sep='\n')
