from toppings.topping_decorator import ToppingDecorator


class Olives(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Olives"

    def get_cost(self):
        return self._pizza.get_cost() + 1.0
