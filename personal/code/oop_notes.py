"""
4 pilar of OOP:
Encapsulation
Abstraction
Inheritance
Polymorphism
"""


# EXAMPLE 1
class PlayerCharacter:
    """
    Class Object Attribute
    This kind of attribute is static
    """
    membership = True

    def __init__(self, name, age):  # constructor function
        # attributes
        self.name = name
        self.age = age

    def shout(self):
        print(f'My name is {self.name} and I\'m {self.age} years old')


player1 = PlayerCharacter('Peter', 22)
player2 = PlayerCharacter('Noah', 29)

print(player1.shout())


# EXAMPLE 2
# parent class
class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('ATTACK!!!')


# child classes or subclasses
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):  # this method is called by the child class
        User.attack(self)  # this output is provided by the method defined in the parent class
        print(f'attacking with a power of {self.power}')  # this output is provided by the method defined in the
        # child class


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


# multiple inheritance
class HybridBoar(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


wizard1 = Wizard('Manuel', 100000000)
wizard1.sign_in()
wizard1.attack()

archer1 = Archer('Chico', 10)
archer1.sign_in()
archer1.attack()

hb1 = HybridBoar('jon', 10000, 5)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())