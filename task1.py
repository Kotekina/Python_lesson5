#1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_text_1 = []
while True:
    text = input('Введите ваш тект:')
    if text == '':
        print(my_text_1)
        break
    else:
        textstop = text + '\n'
        my_text_1.append(textstop)
    with open('text_1.txt', 'w') as file_obj:
        file_obj.writelines(my_text_1)









