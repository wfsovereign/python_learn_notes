import matplotlib.pyplot as plt

from random_walk import RandonWalk


while True:

  rw = RandonWalk(5000)

  rw.fill_walk()
  # plt.figure(figsize=(10, 6), dpi=220)
  plt.figure(figsize=(10, 6))

  point_numbsers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbsers, cmap=plt.cm.Blues, edgecolor='none', s=1)
  # plt.plot(rw.x_values, rw.y_values, linewidth=10)


  plt.scatter(0, 0, c='green', edgecolors='none', s=100)
  plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)

  
  plt.show()

  keep_running = input("Make another walk? (y/n): ")
   
  if keep_running == 'n':
    break