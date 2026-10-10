import random
import matplotlib.pyplot as plt

numbers = [random.randint(1, 100) for _ in range(100)]

plt.hist(numbers, bins=10, edgecolor='black')
plt.title("Гистограмма 100 случайных чисел")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.show()
