# Custom Pizza Builder — Decorator Pattern

A small Python example of the Decorator pattern. Each topping wraps a `Pizza`,
so toppings can be combined at runtime without changing the base pizza class.

## Run

```bash
python3 main.py
```

Expected output:

```text
Description: Plain Dough & Sauce, Cheese, Olives, Pineapple
Total cost: $9.50
```

The example stacks all three toppings: Cheese ($2.00), Olives ($1.00), and
Pineapple ($1.50) on a $5.00 PlainPizza. Topping composition uses nested
constructors and contains no `if`/`else` branching.
