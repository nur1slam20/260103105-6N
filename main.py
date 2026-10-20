from pizza.plain_pizza import PlainPizza
from toppings.cheese import Cheese
from toppings.olives import Olives
from toppings.pineapple import Pineapple


pizza = Pineapple(Olives(Cheese(PlainPizza())))

print(f"Description: {pizza.get_description()}")
print(f"Total cost: ${pizza.get_cost():.2f}")
