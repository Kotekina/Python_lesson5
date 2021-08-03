#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
total = 0
with open ('text3.txt', 'r') as file_obj:
    workers = file_obj.readlines()
    for worker in workers:
        surname, salary = worker.split()
        total += int(salary)
        if int(salary) < 20000:
            print(surname, '-оклад менее 20000')

    print('Средний доход сторудника:', total/len(workers))
