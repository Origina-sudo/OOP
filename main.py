class Item():
    def __init__(self,name,price,quantity ):
        self.name = name
        self.price = price
        self.quantity =quantity
    def calculator_total_price(self,x,y):
        return x * y

item1 = Item("Phone",100,5)
item1.price = 100
item1.quantity = 5

item2 = Item("Laptop",1000,3)
item2.price = 1000
item2.quantity = 3

print(item2.name)
print(item1.name)
print(item1.price)
print(item2.price)
print(item2.quantity)