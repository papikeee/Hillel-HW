number = int(input("Введіть 4-значне число: "))

# Витягуємо кожну цифру за допомогою ділення та залишку
first_digit = number // 1000           # Перша цифра
second_digit = (number // 100) % 10     # Друга цифра
third_digit = (number // 10) % 10       # Третя цифра
fourth_digit = number % 10              # Четверта цифра

# Виводимо цифри в стовпчик
print(first_digit)
print(second_digit)
print(third_digit)
print(fourth_digit)
