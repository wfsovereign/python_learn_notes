import matplotlib.pyplot as plt

from random_walk import RandonWalk

rw = RandonWalk()

rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=10)
plt.show()