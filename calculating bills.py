class parent() :
    
    def __init__ (self):
        print("This is parent class")
        
    def menu(dish):
        if dish == "burger" :
            print("You can add following toppings")
            print("More cheese | Jalapeno")
        elif dish == "iced_americano" :
            print("You can add following toppings")
            print("Chocolate flavour | Caramel flavour")
        else:
            print("Please enter valid dish")

def final_amount(dish, add_ons):
    if dish == "burger" and add_ons == "cheese":
        print("You need to pay 250 USD")
    elif dish == "burger" and add_ons =="jalapeno":
        print("You need to pay 350 USD")
    elif dish == "iced_americano" and add_ons =="chocolate":
        print("You need to pay 250 USD")
    elif dish == "iced_americano" and add_ons =="caramel":
        print("You need to pay 450 USD")
        
class child1(parent):
    
    def __init__(self,dish):
        self.new_dish = dish
        
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,self.add_ons)
        
child1_object = child1("burger")
child1_object.get_menu

child2_object = child2("burger", "jalapeno")
child2_object.get_final_amount()