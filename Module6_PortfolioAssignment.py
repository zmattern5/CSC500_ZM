
import time
class ItemToPurchase:
    def __init__(self,item_name = 'None',item_price = float(0),item_quantity = 0,item_description = 'None'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        return item_cost

    def print_item_info(self):
        #create formating for item price info
        print(self.item_name,self.item_quantity, '@', '${:,.2f}'.format(self.item_price),'=','${:,.2f}'.format(self.print_item_cost()))
class ShoppingCart(ItemToPurchase):

    def __init__(self,name ='none',date = 'January 1, 2020'):
        self.customer_name = name
        self.current_date  = date
        self.cart_items = []


    def add_item(self,item):
        self.cart_items.append(item)
    def remove_item(self,item):
        counter = 0
        #Loop through items in cart if found remove item
        for cart_items in self.cart_items:
            if cart_items.item_name == item:
                self.cart_items.pop(counter)
            counter = counter + 1
        else:
            print('Item not found in cart. Nothing removed.')
    def modify_item(self,item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                #Check for Default values
                if not item.item_quantity == ItemToPurchase().item_quantity:
                    cart_item.item_quantity = item.item_quantity
                if not item.item_price == ItemToPurchase().item_price:
                    cart_item.item_price = item.item_price
                if not item.item_description == ItemToPurchase().item_description:
                    cart_item.item_description = item.item_description
                #break for loop if something is set
                break
        else:
            print('Item not found in cart. Nothing modified.')
    def get_num_items_in_cart(self):
        num_items = 0
        for cart_item in self.cart_items:
            num_items = int(cart_item.item_quantity) + num_items
        return num_items

    def get_cost_of_cart(self):
        cart_cost = 0
        for cart_item in self.cart_items:
            cart_cost = cart_item.print_item_cost() + cart_cost
        return cart_cost

    def print_total(self):
        #If length of cart is 0 no items exist
        if len(self.cart_items) == 0:
            print(f'Number of Items: {self.get_num_items_in_cart()}\n')
            print("SHOPPING CART IS EMPTY\n")
            print(f'Total: ${self.get_cost_of_cart()}')
        else:
            print(f'Number of Items: {self.get_num_items_in_cart()}')
            for cart_item in self.cart_items:
                cart_item.print_item_info()
            print(f'Total: ${self.get_cost_of_cart()}')
    def print_descriptions(self):
        print('Item Descriptions')
        for cart_item in self.cart_items:
            print(cart_item.item_name,':',cart_item.item_description)

def print_menu(cart):

    #cart = shopping_cart
    while True:
        print('MENU')
        print('a - Add Item to cart')
        print('r - Remove item from cart')
        print('c- Change item quantity')
        print('i - Output items description')
        print('o - Output shopping cart')
        print('q - Quit')
        input_options = input('Choose an option:\n')
        if input_options not in ['a', 'r', 'c', 'i', 'o', 'q']:
            print('Invalid option - Please retry request')
            time.sleep(1)
            continue
        if input_options == 'a':
            print('Add Item to cart')
            item = ItemToPurchase()
            item.item_name = input('Enter the Item Name:\n')
            item.item_price = float(input('Enter the Item Price:\n'))
            item.item_quantity = int(input('Enter the Item Quantity:\n'))
            item.item_description = input('Enter the Item Description\n')
            cart.add_item(item)
        if input_options == 'r':
            item_to_remove = input('Enter the Item to remove:')
            cart.remove_item(item_to_remove)
        if input_options == 'c':
            item_name = input('Enter the Item name:\n')
            quantity = int(input('Enter the new Quantity:\n'))
            new_item = ItemToPurchase()
            new_item.item_name = item_name
            new_item.item_quantity = quantity
            cart.modify_item(new_item)
            #print('Change item quantity')
        if input_options == 'i':
            print('OUTPUT SHOPPING CART')
            format_name = (cart.customer_name + "'s")
            format_name = format_name.replace(" ", "")
            print(format_name, " Shopping Cart - ", cart.current_date)
            #print('Item Descriptions')
            cart.print_descriptions()
        if input_options == 'o':
            print('OUTPUT SHOPPING CART')
            format_name = (cart.customer_name + "'s")
            format_name = format_name.replace(" ", "")
            print(format_name," Shopping Cart - ",cart.current_date)
            cart.print_total()
        if input_options == 'q':
            break
        time.sleep(1)
if __name__ == "__main__":
    name = input('Enter your name:')
    date = input('Enter the date:')
    shopping_cart = ShoppingCart(name,date)
    print_menu(shopping_cart)