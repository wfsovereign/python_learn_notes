
class User():

  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.loginCount = 0

  def increaseLoginCount(self):
    self.loginCount += 1

  def resetLoginCount(self):
    self.loginCount = 0

  def personalProfile(self):

    print('My name is ', self.lastName + ' ' +self.firstName, 'my login count: ', self.loginCount)


  def greetMorning(self):
    print('Good moring ', self.firstName)


class Admin(User):

  def __init__(self, firstName, lastName):
    super().__init__(firstName, lastName)
    self.privileges = ['delete', 'add', 'update', 'view']

  def showPrivileges(self):
    print(self.privileges)

