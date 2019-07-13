

list = [1, 2, 3, 4, False, [0], 'hello', 'girls']

print(list)

print(list[2])
print(list[-1])

for i in list:
  print(str(i) + ' good morning')

list[4] = True
print(list)

list.append('like you')
print(list)

list.insert(1, 9)
print(list)

del list[1]
print(list)

lastItem = list.pop()

print('last item ', lastItem)

print('fifth item ,', list.pop(5))
print(list)

list.append(' very like')
list.append('just like this')
list.append(' very like')
print('append list', list)
list.remove(' very like')
print(list)

names = ['tidy', 'dobi', 'phonix']

for i in names: 
  print('I want to dinner with ' + i)

print('but ' + names[2] + " can't come with me")



print(names.sort())
print(names)

print(sorted(names, reverse = True))


