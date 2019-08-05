
import os
import json
import numpy
import unittest

path = os.path

testArray = numpy.arange(9)


targetPath = path.join(path.abspath('./'), 'src/static/firstJsonFile.json')

with open(targetPath, 'w+') as fileObj:
  json.dump(testArray.tolist(), fileObj)

with open(targetPath, 'r+') as fileObj:
  print(json.load(fileObj))



def getUserLikedNumber():
  likedNumber = input('what is favorite number do you like ?\n')

  with open(targetPath, 'w') as fileObj:
    json.dump(likedNumber, fileObj)

  
def outputUserLikedNumber():
  likedNumber = None
  try:
    with open(targetPath, 'r') as fileObj:
      likedNumber = json.load(fileObj)
  except:
    print('open file failure!')
  
  return likedNumber


getUserLikedNumber()
print('your favorite number is ', outputUserLikedNumber())


class GetUserLikedNumberTest(unittest.TestCase):

  def testTheResultIsNumber(self):
    number = outputUserLikedNumber()
    print('number ', number)
    self.assertIsInstance(int(number), int)


unittest.main()