#Elaine Wilde 1671617

class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_description(self):
        print(self.item_name + str(": ") + self.item_description)

    def print_item_cost(self):
        price = self.item_price * self.item_quantity
        return price

class ShoppingCart:
    def __init__(self, customer_name="name", current_date="January 1, 2016", cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self. cart_items = cart_items
        # flag = True
        # while flag == True:
        #     flag = self.print_menu()
        print("Customer name: " + customer_name)
        print("Today's date: " + current_date+"\n")

    def add_item(self,new_item):
        self.cart_items.append(new_item)


    def remove_item(self, name):
        for ind, i in enumerate(self.cart_items):
            if i.item_name==name:
                del self.cart_items[ind]

    def modify_item(self,name):
        for ind, i in enumerate(self.cart_items):
            if i.item_name==name:
                quantity = int(input())
                self.cart_items[ind].item_quantity=quantity #nested object

    def get_num_items_in_cart(self):
        total=0
        for ind, i in enumerate(self.cart_items):
            total += float(self.cart_items[ind].item_quantity)
        return total

    def get_cost_of_cart(self):
        total = 0
        for ind, i in enumerate(self.cart_items):
            total += self.cart_items[ind].item_quantity * self.cart_items[ind].item_price
        return total

    def print_total(self):
        print("Number of Items: " + str(self.get_num_items_in_cart()))
        total = 0
        for ind, i in enumerate(self.cart_items):
            total += self.cart_items[ind].print_item_cost()
            print(self.cart_items[ind].item_name,self.cart_items[ind].item_quantity, "@ $"+ str(self.cart_items[ind].item_price), "=",self.cart_items[ind].print_item_cost()) #become a loop?
        print()
        print("Total: $"+ str(total))

    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date + "\n")
        print("Item Descriptions")
        for ind, i in enumerate(self.cart_items):
            self.cart_items[ind].print_item_description()

    def menu_prompt(self):
        print("MENU")
        print(
            "a - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit\n")

    def print_menu(self):

        self.menu_prompt()

        valid=['a','r','c','i','o','q']
        choice = input("Choose an option:\n")
        while choice not in valid:
            choice = input("Choose an option:\n")
        # if choice != ('a')

        if choice == 'a':
            print("ADD ITEM TO CART")
            item_name = input("Enter the item name:")
            item_description = input("Enter the item description")
            item_price = float(input("Enter the item price:"))
            item_quantity = float(input("Enter the item quantity"))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            self.add_item(new_item)
            return True
        if choice == 'r':
            print("REMOVE ITEM FROM CART")
            remove_item = input("Enter name of item to remove:")
            for ind, i in enumerate(self.cart_items):
                if self.cart_items[ind].item_name == remove_item:
                    del self.cart_items[ind] #at the index location
            return True
        if choice == 'c':
            print("CHANGE ITEM QUANTITY")
            item_name = input("Enter the item name:")
            quant = input("Enter the new item quantity:")
            for ind, i in enumerate(self.cart_items):
                if self.cart_items[ind].item_name == item_name:
                    self.cart_items[ind].item_quantity = quant
            return True
        if choice == 'i':
            print("OUTPUT ITEM DESCRIPTIONS")
            self.print_total()
            print()
            return True
        if choice == 'o':
            print("OUTPUT SHOPPING CART")
            print(self.customer_name + "'s Shopping Cart - " + self.current_date + "\n")
            if len(self.cart_items) == 0:
                print("SHOPPING CART IS EMPTY\n\nTotal: $"+str(self.get_cost_of_cart()))

            return True
        if choice == 'q':
            return False
        else:
            print("Choose an option:")
            return True


if __name__ == '__main__':

    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print()

    cart1 = ShoppingCart(customer_name, current_date)
    cart1.print_menu()



