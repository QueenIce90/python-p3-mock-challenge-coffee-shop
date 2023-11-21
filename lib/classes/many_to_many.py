class Coffee: 
  
    def __init__(self, name): #initialize 
        self.name = name        
    
    
    @property  #Getter Function to call the property 
    def name(self):
        return self._name
    
    @name.setter #Setter set the function or set the new value 
    def name(self, new_name):
        if not hasattr(self, '_name'):
            if isinstance(new_name, str) and len(new_name) >= 3:
                self._name = new_name # SET YOUR NAME TO THE NEW VALUE IN THIS CASE ITS NEW_NAME/////
            else:
                raise Exception('') #raise exception("cannnot change name of customer")
            #with raise Exception always place a warning messages to indentify that specific code. 
        
    def orders(self):    # return all the orders that has coffee 
        return [ orders for orders in Order.all if orders.coffee == self]
    
    def customers(self): # return orders and coffee by each customer  / # set make it unique 
        return list(set([orders.customer for orders in Order.all if orders.coffee == self])) # makes it unique 
    #  another way of doing it : return list(set([order.customer for orders in Order.all_orders == self))
    # lists & list comprehension (above)
    
    def num_orders(self):  
       return len(self.orders()) #another way of doing this:  return len([ orders for orders in Order.all if orders.coffee == self])
    
    def average_price(self): #gets the price of all orders 
        # create list of all prices for this coffee 
        price = [orders.price for orders in Order.all if orders.coffee == self] # this is making a list 
        #sum them up  ex: sum(price)
        #divide by number of orders  : len(price)  // divide : / < this means divide 
        return sum(price ) / len(price)
    
class Customer: #Customer is Initalized with a name *** example: def __init__()
    all = [] # another way: all_customer = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property    #GETTER / GET OUR PRIVATE VARIABLE 
    def name(self):
        return self._name
    
    @name.setter #SETTER  #ISINSTANCE IS USE TO VALIDATE THE NEW VALUE TO SEE IF ITS ACTUALLY A STRING
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15 : #IS NEW NAME A STRING / USING LENS TO SEE IF ITS BETWEEN 1 & 15 (LENGTH = LEN)
            self._name = new_name
        else:
            print('')

    def orders(self):
        return [orders for orders in Order.all if orders.customer == self]
    
    def coffees(self):
        return list(set([orders.coffee for orders in Order.all if orders.customer == self]))
    
    def create_order(self, coffee, price): #reconize what the order will consist of which is in the parameter 
        return Order(self, coffee, price) # just recreate new order]
    
    def total_spent_ob_coffee(self, coffee):
        return sum([order.price for order in Order.all if order.customer == self and order.coffee == coffee])
    
    # Bonus Classmethod
    def most_aficionado(cls, coffee):
        if not coffee.customers():
            return None
        else: 
            high_total = 0 
            for customer in Customer.all:
                customer_total = customer.total_spent_on_coffee(coffee)
                if customer_total > high_total:
                    high_total = customer_total 
                    big_spender = customer 
        #recieves a coffee object argument
        #Return the customer instance that has spent the most money on the coffee instanceprovided as argument.
        
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)
 
    @property #GETTTER
    def price(self):
        return self._price
    
    @price.setter #SETTER # SHOULD NOT BE ABLE TO CHANGE AFTER THE ORDER IS INSTANTIATED  #HINT: HASATTR()
    def price(self, new_price):
        if not hasattr(self, '_price'): # WE DONT HAVE THE PRICE YET
            if isinstance(new_price, float) and 1.0 <= (new_price) <= 10: #PRICE MUST BE OF TYPE FLOAT / PRICE MUST BE A NUMBER BETWEEN 1.0 AND 10.0, INCLUSIVE / 
                self._price = new_price
            else: 
                print('')


    #Return the customer object for  that order

    @property
    def customer(self):
        return self._customer 
    
    # Must be of type Customer 

    @customer.setter
    def customer(self, new_customer):
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else: 
            print("Not a customer GET OUTTTT")

    
    #Return the customer object for  that order

    @property
    def coffee(self):
        return self._coffee  
    
    # Must be of type Customer 

    @coffee.setter
    def coffee(self, new_coffee):
        if isinstance(new_coffee, Coffee):
            self._coffee = new_coffee
        else: 
            print("Not a customer GET OUTTTT")
        

#Customer

#Coffee

#Order - single source of truth 

#Customer --< Order >-- Coffee 

            

   
   
    

