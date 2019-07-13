

magicians = ['dragon', 'Li', 'david']

for magician in magicians:
  print(magician)

print('over.')


fruits = ['banana', 'grape', 'apple', 'mango', 'strawberry']

for fruit in fruits:
  print('I like ' + fruit)

print("It's very delicious")  


array = list(range(1, 21, 2))
print(array)

print(min(array))
print(max(array))
print(sum(array))

advanceArray = [value ** value for value in range(1, 11, 2)]
print('advance array ', advanceArray)


#4.3 4-3
print([val for val in range(1, 21)])

#4.3 4-4
print([val for val in range(1, 101)])

#4.3 4-5
million = list(range(1, 1000001))

if (min(million) == 1 and max(million) == 1000000):
  print(sum(million))


#4.3 4-7
odd = []
for val in range(3, 31):
  if (int(val % 3) == 0):
    odd.append(val)
print(odd)

#4.3 4-9
print([val ** 3 for val in range(1, 11)])


print(odd[2:6])


print('the first three items in the list are:')
print(odd[:3])

print('three items from middle of the list are:')
print(odd[4:7])

print('the last three items in the list are:')
print(odd[-3:])


friendFruits = fruits[:]

friendFruits.append('pear')

print('my fruits: ', fruits)
print('friends fruits: ', friendFruits)

referenceArray = [{'a': '2'}]

newArray = referenceArray[:]
newArray[0]['b'] = '3'
print('reference array ', referenceArray)
print('new array', newArray)