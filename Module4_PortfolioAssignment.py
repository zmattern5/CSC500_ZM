#Create Class
class ItemToPurchase:
    def __init__(self):
        self.item_name = 'None'
        self.item_price = float(0)
        self.item_quantity = 0

    def print_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        return item_cost

c1 =ItemToPurchase()
#Enter Info for Item 1
print('Item 1')
c1.item_name = input('Enter the Item Name:\n')
c1.item_price = float(input('Enter the Item Price:\n'))
c1.item_quantity = int(input('Enter the Item Quantity:\n'))

c2 =ItemToPurchase()
#Enter info for Item 2
print('Item 2')
c2.item_name = input('Enter the Item Name:\n')
c2.item_price = float(input('Enter the Item Price:\n'))
c2.item_quantity = int(input('Enter the Item Quantity:\n'))
total_cost = c1.print_item_cost() + c2.print_item_cost()

#Print Total Cost
print('TOTAL COST')
print(c1.item_name, c1.item_quantity,'@','${:,.2f}'.format(c1.item_price), '=','${:,.2f}'.format(c1.print_item_cost()))
print(c2.item_name, c2.item_quantity,'@','${:,.2f}'.format(c2.item_price), '=','${:,.2f}'.format(c2.print_item_cost()))
print('Total:','${:,.2f}'.format(total_cost))


