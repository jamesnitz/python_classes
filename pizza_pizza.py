class Pizza:
  def __init__(self):
    self.hand_tossed = False
    self.crust_size = ""
    self.style = ""
    self.toppings = []
    self.order_name = ""
  def add_toppings(self, topping):
    self.toppings.append(topping)

  def print_order(self):
    order = f'{self.order_name} would like a {self.crust_size}-inch{" hand-tossed" if self.hand_tossed else ""} {self.style} style pie wiff '
    for topping in self.toppings:
      order += f'{topping}, '
    else:
        order = order[slice(-2)] + f'.'
    print(order)

lil_sleazers = Pizza()
lil_sleazers.crust_size = 16
lil_sleazers.order_name = "James"
lil_sleazers.hand_tossed = True
lil_sleazers.style = 'ny'
lil_sleazers.add_toppings("banana peps")
lil_sleazers.add_toppings("red onion")
lil_sleazers.add_toppings("chicken")


lil_sleazers.print_order()