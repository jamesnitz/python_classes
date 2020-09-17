from building import Building
from city import City

jtown = City('James Town', 'McCheese', '2020')

my_apt = Building('the shay', "9 City Place", 4, 'ya boi')
my_dads_house = Building('My Dads house', "Over there", 2, 'dat dude')

jtown.add_building(my_apt)
jtown.add_building(my_dads_house)

print(f"{jtown.name} established in {jtown.year_established} is made up of:")
for building in jtown.buildings:
  print(' ')
  print(building.building_name)
  print('-------------')
  print(f'{building.building_name} is owned by {building.owner} and has {building.stories} levels!')