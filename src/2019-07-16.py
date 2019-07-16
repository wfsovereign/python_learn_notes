
johnSnow = {
  'firstName': 'Targaryen',
  'lastName': 'you know nothing',
  'age': '18',
  'city': 'winter fall'
}

print(johnSnow)
print('john snow age :', johnSnow['age'])


advanceLanguage = {
  'if': 'the judgement',
  'for': 'the iteration',
  'str': 'stringify something',
  'lower': 'transfer something to lower case character',
  'upper': 'transfer something to upper case character',
  'title': 'upper the first character',
  'strip': 'remove the space character',
  'lstrip': 'remove the space character'
}

for key, value in advanceLanguage.items():
  print(key + ': ' + value)

print(advanceLanguage.items())

for key in advanceLanguage.keys():
  print('key :', key)

print('----------------')

for key in sorted(advanceLanguage.keys()):
  print('key :', key)

print('another key ------- ')
for key in sorted(advanceLanguage.keys()):
  print('key :', key)

print('----------------')
for value in advanceLanguage.values():
  print('value: ', value)


print('----------------')
for value in set(advanceLanguage.values()):
  print('value: ', value)


greatFeature = ['if', 'for']

for key in sorted(advanceLanguage.keys()):
  if (key in greatFeature): 
    print('great feature :', key)
  else:
    print('nice feature :', key)
