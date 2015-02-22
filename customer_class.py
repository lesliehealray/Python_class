# creating the blueprint Customer. We haven't created the object - Just the blueprint.
# When you instatiate the Customer class, you created the object.


class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

# __str__ makes a human readable representation of the object
    def __str__(self):
        return 'Customer Name: %s Beginning Balance: %d ' % (self.name, self.balance)

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

# Creating the objects. Instatiating
my_name = Customer(name='Leslie', balance=340)
print my_name.deposit(45)
print my_name.withdraw(56)
his_car = Customer("David", 567)
print his_car
