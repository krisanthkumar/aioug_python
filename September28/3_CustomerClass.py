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
    def currentBalance(self):
        return self.balance


#Creating an object
kumar = Customer('S. Krisanth Kumar')
hari = Customer('V. Hariharputhran')

#Call the function inside the class
kumar.deposit(100)
hari.deposit(20000)
kumar.deposit(200)

kumar.withdraw(500)

kumar.currentBalance()
hari.currentBalance()

kumar.withdraw(100)
