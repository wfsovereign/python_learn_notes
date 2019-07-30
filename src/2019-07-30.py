import os

path = os.path
print('----->', path.abspath(''))

target = path.join(path.abspath(''), 'src/static/pi.txt')
piFileList = []

with open(target) as piFile:
  # pi = piFile.read()
 
  # print('all file: ', pi)
  lines = piFile.readlines()

  print('lines ', lines)
  for line in lines:
    print('line: ', line)
    piFileList.append(line)

print('pi list file: ', piFileList)

for item in piFileList:
  print(item.replace('2', '🐶'))



with open(target, 'w') as piFile:
  piFile.write('3.141592653589793238462643383279')
  print('write fisrt success!')

with open(target, 'a') as piFile:
  piFile.write('5028841971693993751058209749445923078164062862089986280348253421170679')
  print('write second success')



with open(path.join(path.abspath(''), 'src/static/whyLikeProgram.txt'), 'a') as reasonFile:

  while(True):
    print('press q for stop the answer...')
    userInput = input('why do you like program ?')
    
    if (userInput == 'q'):
      break
    else:
      reasonFile.write(userInput + '\n')

