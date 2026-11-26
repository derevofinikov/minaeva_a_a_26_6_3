print('Привет!')
while True:
    print('Выбери уровень: 1, 2, 3, 4 или 5 (или 0 для выхода)')

    try:
        level = int(input())
    except ValueError:
        print("Введи число!")
        continue

    if level == 0:
        print("Пока!")
        break

    elif level == 1:
        print(f"Описание уровня:\nМетод 1: upper() - делает все буквы заглавными\nМетод 2: lower() - делает все буквы строчными\nМетод 3: capitalize() - первая буква заглавная, остальные строчные\n")
        text1 = "пРиВет МИР!"
        print(f"Тест на строке '{text1}':\nupper(): {text1.upper()}\nlower(): {text1.lower()}\ncapitalize(): {text1.capitalize()}\n")
        met = int(input("Выбери метод: "))
        if met == 1:
            v1 = input("Введи строку: ")
            print("Результат: ", v1.upper())
        elif met == 2:
            v2 = input("Введи строку: ")
            print("Результат: ", v2.lower())
        elif met == 3:
            v3 = input("Введи строку: ")
            print("Результат: ", v3.capitalize())
        else:
            print("Ошибка")

    elif level == 2:
        print(f"Описание уровня:\nМетод 1: find() - первый индекс символа или слова\nМетод 2: replace() - заменяет один фрагмент на другой\nМетод 3: count() - считает количество вхождений\n")
        text2 = "Ботать это круто. Очень круто"
        print(f"Тест на строке '{text2}':\nfind('круто'): {text2.find('круто')}\nreplace('круто', '+'): {text2.replace('круто', '+')}\ncount('о'): {text2.count('о')}\n")
        met = int(input("Выбери метод: "))
        if met == 1:
            v1 = input("Введи строку: ")
            s1 = input("Введи символ или слово для поиска: ")
            print("Результат: ", v1.find(s1))
        elif met == 2:
            v2 = input("Введи строку: ")
            s2 = input("Что заменить: ")
            k2 = input("На что заменить: ")
            print("Результат: ", v2.replace(s2, k2))
        elif met == 3:
            v3 = input("Введи строку: ")
            s3 = input("Какой символ считать: ")
            print("Результат: ", v3.count(s3))
        else:
            print("Ошибка")

    elif level == 3:
        print(f"Описание уровня:\nМетод 1: split() - разбивает строку на список по разделителю\nМетод 2: join() - соединяет элементы списка в строку\n")
        text3 = "1,2,3,4"
        print(f"Тест на строке '{text3}':\nsplit(','): {text3.split(',')}\n' '.join(text3): {' '.join(text3)}\n")
        met = int(input("Выбери метод: "))
        if met == 1:
            v1 = input("Введи строку: ")
            s1 = input("Введи разделитель: ")
            print("Результат: ", v1.split(s1))
        elif met == 2:
            v2 = input("Введи строку: ")
            s2 = input("Введи разделитель для join: ")
            print("Результат: ", s2.join(v2))
        else:
            print("Ошибка")

    elif level == 4:
        print(f"Описание уровня:\nМетод 1: isdigit() - все ли символы цифры (True/False)\nМетод 2: isalpha() - все ли символы буквы (True/False)\nМетод 3: strip() - убирает пробелы и символы по краям\nМетод 4: format() - форматирование через {{}}\nМетод 5: f-string - форматирование через f'...{{x}}...'\n")
        text_4a = "1234*&%1$"
        text_4b = "--- abc 1234 ---"
        print(f"Тест '1234*&%1$':\nisdigit(): {text_4a.isdigit()}\nisalpha(): {text_4a.isalpha()}\n")
        print(f"Тест '--- abc 1234 ---':\nstrip('-'): '{text_4b.strip('-')}'\nformat(): '{'Результат: {}'.format(text_4b)}'\nf-string: '{f'Результат: {text_4b}'}'\n")
        met = int(input("Выбери метод: "))
        if met == 1:
            v1 = input("Введи строку: ")
            print("Результат: ", v1.isdigit())
        elif met == 2:
            v2 = input("Введи строку: ")
            print("Результат: ", v2.isalpha())
        elif met == 3:
            v3 = input("Введи строку: ")
            s3 = input("Символы для удаления (Enter - пробелы): ")
            if s3 == "":
                print("Результат: ", v3.strip())
            else:
                print("Результат: ", v3.strip(s3))
        elif met == 4:
            v4 = input("Введи строку: ")
            print("Результат: ", "Твоя строка: {}".format(v4))
        elif met == 5:
            v5 = input("Введи строку: ")
            print(f"Результат: Твоя строка: {v5}")
        else:
            print("Ошибка")

    elif level == 5:
        print(f"Описание уровня:\nЗдесь применяются все методы сразу:\nstrip(), split(), join(), replace(), title(), lower()\n")
        print(f"Исходная строка:\n'{text5}'\n")
        a = text5.strip(".-")
        print(f"1) strip('.-'): '{a}'")
        b = " ".join(a.split())
        print(f"2) ' '.join(split()): '{b}'")
        c = b.title()
        print(f"3) title(): '{c}'")
        d = c.replace(":", " -").replace("+", " + ")
        print(f"4) replace(':','+'): '{d}'")
        print(f"\nИтог: '{d}'")
        print("\nА теперь попробуй сам!")
        v = input("Введи свою строку: ")
        result = " ".join(v.strip(".-").split()).title()
        print(f"Результат: '{result}'")

    else:
        print("Такого уровня нет. Попробуй снова.")
