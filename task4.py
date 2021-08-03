#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
rus = {"One": 'Один',
       "Two": 'Два',
       "Three": 'Три',
       "Four": 'Четыре'}
file_new = []
with open('task4', 'r') as file_odj:
    lines = file_odj.readlines()
    for line in lines:
        line = line.split(' ', 1)
        file_new.append(rus[line[0]] + ' ' +line[1])
    print(file_new)
with open('task4_new.txt', 'w') as file_odj_new:
    file_odj_new.writelines(file_new)

