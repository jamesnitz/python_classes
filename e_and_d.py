import datetime

class Employee:
  def __init__(self, name, title):
    self.name = name
    self.title = title
    self.start_date = datetime.datetime.now

class Company:
  def __init__(self, name, address, industry_type):
    self.name = name
    self.address = address
    self.type = industry_type
    self.employees = []
  def hire_employee(self, employee):
    self.employees.append(employee)


james = Employee('james', 'typist')

copany = Company('co-pany' 'street', 'stuff')

copany.hire_employee(james)

