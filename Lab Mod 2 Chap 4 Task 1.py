# Завдання 1
# Користувач вводить з клавіатури розмір сторони
# квадрата. Виведіть на екран заповнений квадрат. Розмір
# сторони дорівнює введеному розміру. Наприклад, якщо
# користувач ввів 3, на екрані буде виведено:
# ***
# ***
# ***

side=int(input('Enter the size of the side of the square: '))
for i in range(side):
    print('*' * side)