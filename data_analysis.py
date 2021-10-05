# import matplotlib.pyplot as plt
#
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.style.use('bmh')
# fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
#
# # Назначение заголовка диаграммы и меток осей
# ax.set_title('Square Numbers', fontsize=24)
# ax.set_xlabel('Value', fontsize=14)
# ax.set_ylabel('Square of Value', fontsize=14)
#
# # Назначение размера шрифта делений на осях.
# ax.tick_params(axis='both', labelsize=14)
#
# plt.show()
# print(plt.style.available)

import matplotlib.pyplot as plt

x_values1 = list(range(1, 5001))
y_values1 = [x ** 2 for x in x_values1]

x_values2 = list(range(1, 5001))
y_values2 = [x ** 3 for x in x_values2]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_values1, y_values1, s=10)
ax.scatter(x_values2, y_values2, c='red', s=10)

# Назначение заголовка диаграммы и меток осей.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', which='major', labelsize=14)

# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

# сохранение в файле
# plt.savefig('squares_plog.png', bbox_inches='tight')

# Вызов
plt.show()
