from dataclasses import dataclass


class Cat():
    name = None
    color = None
    isHappy = None
    #Function to more comfortable use of this class
    def set_data(self, name, color, isHappy):
        self.name = name
        self.color = color
        self.isHappy = isHappy

    def get_data(self):
        return self.name, self.color, self.isHappy

#Without using function set_data
cat = Cat()
cat.name = 'Barsik'
cat.color = 'grey'
cat.isHappy = True
print(cat.name)

#With using set_data
kitten = Cat()
kitten.set_data('Mursik', 'brown ', True)
print(kitten.name)
print(kitten.get_data())
#And now I kmow how to create and use class

#Now I'm going to learn constructors

class human():
    def __init__(self, name = None, age = None, isHappy = None): #Constructor
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.get_data()
    def get_data(self):
        print(self.name, self.age, self.isHappy)

Ars = human('Ars', '19', True)
Smallgirl = human('Smallgirl', '15', True)
#And now I know contsructors


