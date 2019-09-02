
import matplotlib.pyplot as plt


squares = [1, 4, 9, 16, 25]
inputs = [1, 2, 3, 4, 5]

plt.plot(inputs, squares, linewidth=5)

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Square of value', fontsize=12)

plt.tick_params(axis='both', labelsize=14)

plt.show()