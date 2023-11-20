class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, '_name'):
            if isinstance(new_name, str) and len(new_name) >= 3:
                self._name = new_name
            else:
                raise Exception('')
        
    def orders(self):   
        return [ orders for orders in Order.all if orders.coffee == self]
    
    def customers(self):
        return list(set([orders.customer for orders in Order.all if orders.coffee == self])) # makes it unique 
    
    def num_orders(self):
       return len([ orders for orders in Order.all if orders.coffee == self])
    
    def average_price(self):
        price = [orders.price for orders in Order.all if orders.coffee == self]
        return sum(price ) / len(price)
    
class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15 :
            self._name = new_name
        else:
            print('')

    def orders(self):
        return [orders for orders in Order.all if orders.customer == self]
    
    def coffees(self):
        return list(set([orders.coffee for orders in Order.all if orders.customer == self]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price) # just recreate new order
        
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not hasattr(self, '_price'):
            if isinstance(new_price, float) and 1.0 <= (new_price) <= 10:
                self._price = new_price


            

   
   
    

