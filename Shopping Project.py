
#This is an empty dictionary
#{key:value} e.g. {"oranges" : 5, "mangoes" : 4}
#+= to add adjustments to your value
#Author: Daniel Adike

Shopping_Basket = {}
print ("""
Shopping Basket Options
_________________
1: Add Item
2: Remove Item
3: View Item
0: Exit Program

""")
if (type(2) == 'int'):
    print(2)
try:
    option = int(input("Hello Please enter an option: "))
except:
    print('error')
    option = 0

while option != 0:
    if option == 1:
        reet = "y"
        while reet =="y":
            item = input("enter an item: ")

            if item in Shopping_Basket:
                print("Item already exists in your cart")
                qnty = int(input("Enter the quantity: "))
                Shopping_Basket[item] = Shopping_Basket[item] + qnty
            elif( item.isnumeric() ):
                print("Numeric value not allowed")
            else:
                qnty = int(input("Enter the quantity: "))
                Shopping_Basket[item] = qnty
            reet = input("Do you wish to add more items?   (y/n)")

    elif option == 2:
        item = input("Enter an item: ")
        del(Shopping_Basket[item])

    elif option == 3:
        for item in Shopping_Basket:
            print(item,":",Shopping_Basket[item])

    elif option != 0:
        print("Sorry You did not enter a valid number. ")
        
    option = int(input("\n\nEnter an option: "))

else:
    print("Shopping basket program closed.")
