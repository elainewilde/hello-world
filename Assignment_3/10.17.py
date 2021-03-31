#Elaine Wilde 1671617

class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        price = self.item_price * self.item_quantity
        return price


if __name__ == "__main__":

    print('Item 1')
    name_food = input('Enter the item name:\n')
    price_item = float(input('Enter the item price:\n'))
    quantity_item = int(input('Enter the item quantity:\n'))
    print()
    print('Item 2')
    name_food2 = input('Enter the item name:\n')
    price_item2 = float(input('Enter the item price:\n'))
    quantity_item2 = int(input('Enter the item quantity:\n'))
    print()
    Item1 = ItemToPurchase(name_food, price_item, quantity_item)
    Item2 = ItemToPurchase(name_food2, price_item2, quantity_item2)

    print("TOTAL COST")
    print(Item1.item_name,Item1.item_quantity, "@ $"+str(int(Item1.item_price)), "= $" + str(int(Item1.print_item_cost())))
    print(Item2.item_name,Item2.item_quantity, "@ $"+str(int(Item2.item_price)), "= $"+ str(int(Item2.print_item_cost())))
    print("\nTotal: $" + str(int(Item1.print_item_cost()) + int(Item2.print_item_cost())))




