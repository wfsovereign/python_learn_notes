import matplotlib.pyplot as plt

from random_walk import RandonWalk


while True:

  rw = RandonWalk()

  rw.fill_walk()

  point_numbsers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbsers, cmap=plt.cm.Blues, edgecolor='none', s=15)

  plt.show()

  keep_running = input("Make another walk? (y/n): ")
   
  if keep_running == 'n':
    break