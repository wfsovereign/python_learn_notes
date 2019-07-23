import os
import math
import decimal
import sys
import time


def getpi1(digit=6000):
  time1 = time.time()
  number = 10 + digit
  b = 10 ** number
  x1 = b * 4 // 5
  x2 = b // -239

  sum = x1 + x2

  number *= 2
  for i in range(3,number,2):

    x1 //= -25
    x2 //= -57121
    x = (x1+x2) // i
    sum += x

  pai = sum*4
  pai //= 10**10

  paistring=str(pai)
  result=paistring[0]+str('.')+paistring[1:len(paistring)]
  print('result, ', result)

  time2=time.time()
  print('总共耗时：' + str(time2 - time1) + 's')

print(getpi1())

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(0x100000)

# def getPi(pow) :
#   pi = decimal.Decimal(1)
#   index = 0
#   n = 2
#   a = 1
#   last = 1

#   end = math.pow(10, pow)
#   while a < end:
#     last = last + n
#     print('last ,', last)
#     if (a % 2 == 0):
#       print('index , 0', a)
#       pi = pi + decimal.Decimal((1 / last))
#     else:
#       print('index , 1', a)
#       pi = pi - decimal.Decimal((1 / last))
#     a += 1
#   return decimal.Decimal(pi * 4)    

# print('pi --> ', (getPi(4)))    

# def pi(acc=500):
#     def red(num, ac):
#         return num if ac == 0 else (num * num) / (6 + red(num + 2, ac - 1))
#     return 3 + red(1, acc)
# print(pi(math.pow(10, 3)))

# import numpy as np
# simpi = lambda num: len(filter(lambda pt: pt[0]*pt[0]+pt[1]*pt[1]<1, np.reshape(np.random.uniform(size=2*num), [num, 2])))/float(num)*4
# print(simpi(1000000))

# currentPath = os.path.dirname(os.path.abspath(__file__))
# print('path: , ', currentPath)
# print('working path ,', os.getcwd())

# print(os.path.join(currentPath, 'static/pi.txt'))
# print(os.path.join(currentPath, '/static/pi', 'ip'))

# print(currentPath.split('/'))

# with open(currentPath + '/static/pi.txt') as piFile:
#   pi = piFile.read()
#   print('pi :', pi)

#   lines = piFile.readlines()

#   for ll in lines:
#     print('ll , ', ll)
  
#   print('lines ,', lines)
#   for line in pi:
#     print('line ', line)


# print(' pi : ', 4 * math.atan(1))