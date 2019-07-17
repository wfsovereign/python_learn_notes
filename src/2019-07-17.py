from modules.buildHandsomeProfile import buildHandsomeProfile


message = input('hello world, your name: ')

print(message)

questionnaires = []

while len(questionnaires) < 2:
  
  name = input("What's your name : ")
  place = input('If you could visit one place in the world, where would you go? ')

  questionnaires.append({'name': name, 'place': place})

print('the result ,', questionnaires)


def myPets(name, type):
  print('name : ', name, ' type : ', type)

myPets('duobi', 'dog')

myPets(type='dog', name='duobi')


def makePizze(*toppings):
  print('args ,', toppings)

makePizze('peperoni')  
makePizze('mushroom', 'extra cheese')

def buildProfile(name, **info): 
  person = {'name': name}

  for key, value in info.items():
    person[key] = value

  print(person)  
  return person

buildProfile('john', gender='male', age='21', career='princes')

F = buildHandsomeProfile('F君', gender='male', age='26', career='dreamer')

print(F)
