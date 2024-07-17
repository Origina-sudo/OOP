class Item():
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name:str,price:float,quantity =0 ):
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal toZero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to  Zero!"

        #Assign to Self Object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculator_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})"



"""item1 = Item("Phone",100,1)
#item1.price = 100
#item1.quantity = 5

item2 = Item("Laptop",1000 ,3)
item2.pay_rate =0.7
item2.apply_discount()
print(item2.price)
#item2.price = 1000
#item2.quantity = 3

item1.apply_discount()
print(item1.price)"""

item1 = Item("Phone",100,1)
item2 = Item("Laptop",1000,3)
item3 = Item("Cable",10,5)
item4 = Item("Mouse",50,5)
item5 = Item("Keyboard",75,5)


print(Item.all)