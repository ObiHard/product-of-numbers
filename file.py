n = int(input("Введите целое число: "))

while n > 9:
    product = 1
    for digit in str(n):
        product *= int(digit)
    n = product

print("Результат:", n)
