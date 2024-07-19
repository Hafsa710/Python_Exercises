#Example 3: Order_list


class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
       return self.price>odr2.price

odr1=Order("chips",20)
odr2=Order("biscuit",40)

print(odr1>odr2)