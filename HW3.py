number = int(input("Enter five digits number"))

first_digit = number % 10
second_digit = (number // 10) % 10
third_digit = (number // 100) % 10
fourth_digit = (number // 1000) % 10
fifth_digit = (number // 10000) % 10

print(first_digit,second_digit,third_digit,fourth_digit,fifth_digit)

