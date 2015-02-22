# for  class objects, python requires self as an explicit argument.
# __init__ is a constructor and defines the blueprint of the object. Defines what pieces or attributes that are required.

# if you are  creating a class  in python and not inheriting from anything, object is a reserved word that represents the base in python.

class Car(object):
    condition = 'new'

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

# __str__ makes a human readable representation of the object
    def __str__(self):
        return 'Model: %s Color: %s MPG: %s' % (self.model, self.color, self.mpg)

    def display_car(self):
        return 'I have a %s %s that gets %s miles to the gallon.' % (self.color, self.model, self.mpg)

    def drive_car(self, test_drive=False):
        if not test_drive:
            self.condition = "used"
        return self.condition

my_car = Car("DeLorean", "silver", 88)  # instantiates or creates a new car object  with the supplied arguments/values
# Below to show explicitly how each argument are positional arguments.
his_car = Car(model="Honda", color= "blue", mpg= 26)
print my_car # __str__
print my_car.display_car()
print my_car.condition
print my_car.drive_car(test_drive=True)
print my_car.drive_car()

# Classes store objects with their own methods and variables.
# We use the word object in parenthese because we want our classes to inherit the object class.
# Creating instances of a class is using classes to create new objects.
# new_Object = ClassName()

# Electric car inherits from Car
class ElectricCar(Car):

    def __init__(self, model, color, mpg, battery_type):
        # super calls the init method on the class it inherits from.
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type

    def display_car(self):
        return self.battery_type

my_car = ElectricCar("Tesla", "blue", "56", "molten salt")
#print my_car.display_car()
