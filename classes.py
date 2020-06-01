# CLASSES
class Book:
  def __init__(self):
    self.title = ""
    self.author = ""
    self.current_page = 1
    self.currently_reading = False

  def start_reading(self):
    self.currently_reading = True
    print(f'You start reading {self.title} at page {self.current_page}')

  def stop_reading(self, page):
    self.current_page = page

infinite_Jest = Book()
infinite_Jest.title = "Infinite Jest"
infinite_Jest.author = 'David Foster Wallace'
# 
for prop, value in infinite_Jest.__dict__.items():
  print(f'{prop}: {value}\n')

print()
print()
print("----------------------------")
print()

print(infinite_Jest.currently_reading)
infinite_Jest.start_reading()
print(infinite_Jest.currently_reading)
infinite_Jest.stop_reading(450)
infinite_Jest.start_reading()