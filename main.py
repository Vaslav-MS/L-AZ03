import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

x = np.linspace(-100, 100, 100000)
y = x ** 64

plt.plot(x,y)
plt.title('График: y = x ** 2')
plt.grid(True)

plt.show()
