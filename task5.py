#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text5.txt', 'w') as file_obj:
    line = input('Введите числа через пробел;')
    file_obj.writelines(line)
with open('text5.txt', 'r') as file_obj:
    line = file_obj.read().rstrip().split()
    print('Сумма введенных чисел:', sum(map(int, line)))



