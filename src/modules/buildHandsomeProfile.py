def buildHandsomeProfile(name, **info): 
  person = {'name': name}

  for key, value in info.items():
    person[key] = value

  return person

