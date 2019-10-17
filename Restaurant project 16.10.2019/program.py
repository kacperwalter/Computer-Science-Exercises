class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    """string representation"""
    def __repr__(self):
        return "{} menu is avalible from {} to {}".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):

        bill = 0

        for purchased_item in purchased_items:
            if purchased_item in self.items.keys():
                bill += self.items[purchased_item]

        return bill


class Franchise:
    def __init__(self, adress, menus):
        self.adress = adress
        self.menus = menus

    def __repr__(self):
        return "Adress of the franchise restaurant: {}".format(self.adress)

brunch_dishes = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
early_bird_dishes = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}
dinner_dishes = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}
kids_dishes = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

brunch = Menu("brunch", brunch_dishes, 11, 16)

early_bird = Menu("early bird", early_bird_dishes, 15, 18)

dinner = Menu("dinner", dinner_dishes, 17, 23)

kids = Menu("kids", kids_dishes, 11, 21)

"""this will print string representation method"""
# print(early_bird)

"""tests the calculate_bill method"""
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

""" Creating the restaurant franchises"""

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

