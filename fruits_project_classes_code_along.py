class Fruit():
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = float(price)
    
    #Custom method to print info
    def fruit_info(self):
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        The fruit is: {self.name}. 
        The color is: {self.color}. 
        The price is {self.price}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)

    #Custom method to calculate and print sales tax
    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
        #######################
        Total cost is: {total}
        #######################
        """)

#Creating different fruit Objects      
apple = Fruit("Apple", "Red", "23.00")
kiwi = Fruit ("Kiwi", "Green", "5.00")
pear = Fruit("Pear", "Yellow", "1.50")
banana = Fruit("Banana", "Yellow", "2.25")

#Using our custom methods
banana.fruit_info()
banana.calc_sales_tax(.04)

#<------------------------------------Regular Function to show students how we can use both ------------------------------------->
#implementing a fruit dict to map the text inputs to the corresponding objects
fruit_dict = {
    "apple": apple,
    "kiwi": kiwi,
    "pear": pear,
    "banana": banana
}

#Implementing a standalone function instead of method, because this is involving a comparison of 2 different class Fruit() objects. Using inputs and dicts in for this.
def compare_price():
    fruit_select_1 = input("Select the first fruit to compare: Apple | Kiwi | Pear | Banana ").lower()
    fruit_select_2 = input("Select the second fruit to compare: Apple | Kiwi | Pear | Banana ").lower()
    print(f"""
    ;;;;;;;;;;;;;;;;;;;;;;;;
    Fruit Analysis Tool:
    {fruit_dict[fruit_select_1].name} costs {fruit_dict[fruit_select_1].price}
    {fruit_dict[fruit_select_2].name} costs {fruit_dict[fruit_select_2].price}
    ;;;;;;;;;;;;;;;;;;;;;;;;
    """)
    
compare_price()