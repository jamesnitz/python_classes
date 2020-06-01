class Employee:
  def __init__(self, name, title):
    self.name = name
    self.title = title
    self.start_date = ""

class Company:
  def __init__(self, name, address, industry_type):
    self.name = name
    self.address = address
    self.industry_type = industry_type
    self.employees = []

  def report(self):
    print(f'{self.name} is in the {self.industry_type} game and has the following employees:')
    for employee in self.employees:
      print(employee.name)


bad_company = Company('Bad Company', "over there", "industry")
ymcm = Company('Young Money Cash Money', "over here", "Money")

employee1 = Employee("slick rick", "Chief Slick Officer")
employee2 = Employee("my dad", "Father")

bad_company.employees.append(employee1)
bad_company.employees.append(employee2)

bad_company.report()
