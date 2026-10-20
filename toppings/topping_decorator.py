from pizza.pizza import Pizza


class ToppingDecorator(Pizza):
    """Base wrapper that delegates to the pizza it decorates."""

    def __init__(self, pizza):
        self._pizza = pizza
