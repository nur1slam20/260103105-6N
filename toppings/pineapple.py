from toppings.topping_decorator import ToppingDecorator


class Pineapple(ToppingDecorator):
    def get_description(self):
        return f"{self._pizza.get_description()}, Pineapple"

    def get_cost(self):
        return self._pizza.get_cost() + 1.5
