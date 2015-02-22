#!/usr/bin/python
import csv

OMNIVORE = 'omnivore'
CARNIVORE = 'carnivore'
HERBIVORE = 'herbivore'

MEAT = 'meat'
GRASS = 'grass'

EATS = {
    OMNIVORE: [MEAT, GRASS],
    CARNIVORE: [MEAT],
    HERBIVORE: [GRASS]
}

# defines the attributes of the object and their defaults
class Animal(object):
    def __init__(self, name, color, age=0, diet=):    # Constructor of the class
        self.name = name
        self.age = age
        self.color = color
        self.diet = diet or OMNIVORE

    def feed(self, food):
        if food in EATS[self.diet]:
            # {0} is a string format function. the numbers refer to the index
            print '{0} loved the {1}!!'.format(self.name, food)
        else:
            print '{0} does not eat {1} since it is a {2}.'.format(
                self.name, food, self.diet
            )



def __main__():
    animals = []
    with open('/home/lhealray/python_class/animals.csv', 'r') as f:
        data = csv.DictReader(f)
        for row in data:
            obj = Animal(
                name=row['name'],
                color=row['color'],
                age=row['age'],
                diet=row['diet'],
            )
            animals.append(obj)
    for animal in animals:
        print 'Feeding {0} the {1}.'.format(
                animal.name, animal.diet
            )
        animal.feed('meat')
        animal.feed('grass')
        print '\n'

if __name__ == "__main__":
    __main__()
