from toppings.topping_decorator import ToppingDecorator


class Cheese(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Cheese"

    def get_cost(self):
        return self._pizza.get_cost() + 2.0
