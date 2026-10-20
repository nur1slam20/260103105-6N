from pizza.pizza import Pizza


class PlainPizza(Pizza):
    def get_description(self):
        return "Plain Dough & Sauce"

    def get_cost(self):
        return 5.0
