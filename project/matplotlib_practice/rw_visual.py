import matplotlib.pyplot as plt

from random_walk import RandonWalk


while True:

  rw = RandonWalk()

  rw.fill_walk()

  plt.scatter(rw.x_values, rw.y_values, s=10)
  plt.show()


  keep_running = input("Make another walk? (y/n): ")
   
  if keep_running == 'n':
    break