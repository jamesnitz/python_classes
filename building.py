import datetime
# URBAN PLANNER 1
class Building:
  def __init__(self, name, address, stories, owner):
    self.building_name = name
    self.address = address
    self.stories = stories
    self.date_constructed = ""
    self.owner = owner

#   def purchase(self, owner):
#     self.owner = owner
  
#   def build(self):
#     self.date_constructed = datetime.datetime.now()
#   def report(self): 
#     print(f'{self.building_name} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.')
#     print()
# my_apt = Building('the shay', "9 City Place", 4)
# my_apt.purchase("Slim bankshot")
# my_apt.build()
# my_apt.report()
# runs_house = Building("church", "downtown", 2)
# runs_house.purchase("Ice Cole")
# runs_house.build()
# runs_house.report()