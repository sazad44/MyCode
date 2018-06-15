# Programming Exercise 10-8

import retailitem
import cashregister

# Constants to hold the options of purchase items
PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5

# define get user choice
def get_user_choice():
    print('Menu')
    print('---------------------------------')
    print('1. Pants')
    print('2. Shirt')
    print('3. Dress')
    print('4. Socks')
    print('5. Sweater')
    print()

    choice = int(input('Enter the menu number of the item ' + \
                       'you would like to purchase: '))
    print()

    while choice > SWEATER or choice < PANTS:

        choice = int(input('Please enter a valid item number: '))
        print()

    return(choice)


# main method
def main():

    # Create sale items.
    pants = retailitem.RetailItem('Pants', 10, 19.99)
    shirt = retailitem.RetailItem('Shirt', 15, 12.50)
    dress = retailitem.RetailItem('Dress', 3, 79.00)
    socks = retailitem.RetailItem('Socks', 50, 1.00)
    sweater = retailitem.RetailItem('Sweater', 5, 49.99)

    # Create dictionary of sale items.
    sale_items = {PANTS:pants, SHIRT:shirt,
                  DRESS:dress, SOCKS:socks,
                  SWEATER:sweater}

    # Create a cash register.
    register = cashregister.CashRegister()

    # Initialize loop test.
    checkout = 'N'

    # User wants to purchase more items:
    while checkout == 'N':

        user_choice = get_user_choice()
        item = sale_items[user_choice]
        '''
        #If the item's iventory is 0 type 'The item is out of stock.'
        Otherwise,  1) add the item to the register  
                    2) change the inventory number of the item in the sale_items dictionary
                    3) ask the user if they're ready to checkout Y/N and save that in the checkout var
        '''
        #Your code here
        if item.UnitsinInventory == 0:
            print("")
            print("The item is out of stock.")
            print("")
        else:
            item.UnitsinInventory -= 1
            register.Item_List = register.purchase_item(item)
            checkout = input("Are you ready to checkout (Y/N)? ")
            print("")
    print()
    print('Your purchase total is: ', \
          format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()


# Call the main function.
if __name__ == "__main__":
    main()

