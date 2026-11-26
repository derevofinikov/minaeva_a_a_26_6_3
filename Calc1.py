a = int(input("Введи первое число"))
b = int(input("Введи второе число"))
c = str(input("Введи знак, сударь"))

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/' and b != 0:
    print(a / b)
elif c == '//' and b != 0:
    print(a // b)
elif c == '%' and b != 0:
    print(a % b)
elif c == '**':
    print(a ** b)
else:
    print('Ошибка формата ввода данных')
