import numpy as np
import matplotlib.pyplot as plt

# Задание 1

mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 10000  # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data, bins=50, edgecolor='black', alpha=0.7)
plt.title('Гистограмма')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

# Задание 2

points = 50  # Количество точек
x = np.random.rand(points)  # X
y = np.random.rand(points)  # Y

plt.scatter(x, y, alpha=0.7, edgecolor='black')
plt.title('Диаграмма рассеяния')
plt.show()
