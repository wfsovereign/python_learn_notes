
'''
John Machin（https://en.wikipedia.org/wiki/John_Machin）

设
x = arctan A
tan x = A
tan 2x = (2 tan x) / (1 - tan^2 x)
tan 2x = (2A) / (1 - A^2)
2x = arctan ((2A) / (1 - A^2))
2 arctan A = arctan ((2A) / (1 - A^2))
4 arctan A = 2 arctan ((2A) / (1 - A^2))
A=1/5
4 arctan (1/5) = 2 arctan ((2/5) / (1 - 1/25))=2 arctan (5/12)
2 arctan (5/12) - arctan (1/239)
= arctan ((2*5/12) / (1 - 25/144)) - arctan (1/239)
= arctan (120/119) - arctan (1/239)
= arctan ((120/119 - 1/239) / (1 + 120/119 * 1/239)
= arctan (1.0042 / 1.0042)
= arctan (1)
= π/4

（https://zhidao.baidu.com/question/579341502.html）

'''
import time



def calculateCircumference(precision = 10):
  timeStart = time.time()
  extraPrecision = precision + 10
  resultPrecision = 10 ** extraPrecision

  x1 = resultPrecision * 4 // 5
  x2 = resultPrecision // -239

  sum = x1 + x2

  precision *= 2

  for i in range(3, precision, 2):
    x1 //= -25
    x2 //= -57121

    sum += (x1 + x2) // i

  pi = 4 * sum
  pi //= 10 ** 10
  pi = str(pi)

  print('result: ', pi)
  timeEnd = time.time()
  print('total time: ', str(timeEnd - timeStart), 's')


calculateCircumference(10 ** 2)

'''
result:  100001
total time:  10.339331150054932 s
'''