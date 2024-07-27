from normalChef import Chef

class ChineseChef(Chef):
    def make_fried_rice(self):
        print("The chef makes fried rice")
    def make_coffee(self):
        print("The chef makes Latte")
    def make_Special_Dish(self):
        print("The chef makes Chinese Ribs with Extra Masala")

Oder1 = Chef()
Oder1.make_Special_Dish()
Oder1.make_Chicken()
Oder1.make_Salad()
Oder1.make_desert()

Oder2 = ChineseChef()
Oder2.make_coffee()
Oder2.make_Special_Dish()
Oder2.make_Salad() #ingeritance
Oder2.make_desert() #inheritance