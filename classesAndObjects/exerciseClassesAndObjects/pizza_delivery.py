class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0
        self.ingredients[ingredient] += quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if self.ordered == True:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        if quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self):
        self.ordered = True
        prepared = [f'{key}: {value}' for key, value in self.ingredients.items()]
        return f"You've ordered pizza {self.name} prepared with {', '.join(prepared)} and the price will be {self.price}lv."

