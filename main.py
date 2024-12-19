import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 10000  # Количество образцов

data = np.random.normal(mean, std_dev, num_samples)

#plt.figure(figsize=(8, 6))
plt.hist(data, bins=50, edgecolor='black', alpha=0.7)
plt.title('Гистограмма')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()
