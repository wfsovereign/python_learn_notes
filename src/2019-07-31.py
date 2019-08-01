import numpy as np
import os
import re

path = os.path

a = np.zeros((2, 9))

print('a, ', a)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

print('b , ', b)

colC1 = a[:, 1]
colC2 = a[:, 2]
print('col ,', colC1)
print(colC1.shape)
print('col 2,', colC2)
print(colC2.shape)

rowR1 = a[0, :]
rowR2 = a[1, :]
print('row ,', rowR1)
print(rowR1.shape)
print('row 2, ', rowR2)
print(rowR2.shape)

b = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])

print('b , ', b)

print('arange ,', np.arange(4))

c = np.array([0, 2, 0, 1])

print('c range', b[np.arange(4), c])
d = b[np.arange(4), c]
d += 10
print('c range', d)

a = np.array([[1,2], [3, 4], [5, 6]])
b = [[1,2], [3, 4], [5, 6]]
print(' a, ', a)
print(' b ,', b)
boolIndex = (a > 2)
print(boolIndex)
try: 
  boolIndex = (b > 2)
  print(boolIndex)
except Exception as e:
  print('error==== ,', e)

novelDirection = path.join(path.abspath('./'), '../NoteCrawler/resource/《圣墟》.txt')

try:

  with open(novelDirection) as novelFile:
    contents = novelFile.read()
except FileNotFoundError as e:
  print('open file error', e)  

else:
  words = contents.split()
  pattern = re.compile(r'([\u4e00-\u9fa5])')
  # chars = pattern.split(contents)
  # print('chart ,', len(chars))
  print('re split ', len(re.split(r'', contents)))
  # print('words ,', words)
  print('totol words: ', len(words))
  print('content :', len(contents))


a = 'hello world'

print(a.split(' '))
print(re.split('', a))