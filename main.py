class Item():
    def __init__(self,name:str,price:float,quantity =0 ):
        #Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal toZero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to  Zero!"

        #Assign to Self Object
        self.name = name
        self.price = price
        self.quantity =quantity

    def calculator_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone",100,1)
#item1.price = 100
#item1.quantity = 5

item2 = Item("Laptop",1000 ,3)
#item2.price = 1000
#item2.quantity = 3

print(item1.calculator_total_price())
print(item2.calculator_total_price())