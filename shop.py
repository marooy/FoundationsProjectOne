####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Bear CafeShop"
signature_flavors = ["saltedCaramel", "Brainy" , "Wicked"]
order_list = []
in_menu = []


def print_menu():
    print()
    print('our menu:')
    for item in menu:
        print(("%s ( KD %s)") %(item,menu[item]))
    print()
    



def print_originals():
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for flav in original_flavors:
       print(flav)
    print()
      



def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    for flav in signature_flavors:
       print(flav)
    print()   
      



def is_valid_order(order):

    if(order in menu):
        return True
    elif(order in original_flavors):
        return True
    elif(order in signature_flavors):
        return True
    else:
        print('Order is not in the menue: ' + order)
        print('would you like to pick another or Exit?')
        return False 


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    order = ''
    print("what's your order?(Enter the exact spelling of the item you want. type 'Exit'): ")
    while order != 'Exit':
        order = input()
        if order != 'Exit':
            if( is_valid_order(order)):
                order_list.append(order)
       

    return order_list
   


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    print()
    print("That'll be KD %s" % str(total))
    print("this order is eligible for credit card payment")
    print("thank you for shopping at %s" % (cupcake_shop_name) )



def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    cost = []
    
    # your code goes here!
    for i in order_list:
        if(i in menu):
            cost.append(menu[i])
        elif(i in original_flavors):
            cost.append(menu["original cupcake"])
        elif(i in signature_flavors):
            cost.append(menu["signature cupcake"])
        else:
            cost.append(0)   
             
    for x in cost:
        total = total + x
    accept_credit_card(total)    


    return total
  


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    for i in order_list:
        print(i)
    # your code goes here!
    get_total_price(order_list)
