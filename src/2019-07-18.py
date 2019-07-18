from modules.userController import User, Admin
from collections import OrderedDict
from random import randint


f = User('君', 'F')

f.greetMorning()
f.personalProfile()

f.increaseLoginCount()
f.increaseLoginCount()

f.personalProfile()



root = Admin('君', 'f')
root.showPrivileges()


programLanguage = OrderedDict({'j': 'python', 'a': 'c++', 'b': 'Javascript'})

for name, language in programLanguage.items():
  print('name: ', name, ' like ', language)


class Die():

  def __init__(self, sides=6): 
    self.sides = sides

  def rollDie(self):
    side = randint(1, self.sides)
    print('total sides ', self.sides,  ' current side : ', side)


die = Die()

die.rollDie()

die = Die(10)
die.rollDie()