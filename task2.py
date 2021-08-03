#2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
my_text = ['One 1\n', 'Two 22\n', 'Three 333\n', 'Four 4444\n', 'Five 55555\n', 'Six 666666\n']
with open('text2.txt', 'w+') as file_obj:
    file_obj.writelines(my_text)
my_text = open('text2.txt', 'r')
lines = len(my_text.readlines())
print('Кол-во строк:', lines)

my_text = open('text2.txt', 'r')
text = my_text.readline()

word = 0
i = 0
for word in text:
    word = text.split()
    i +=1
    print('на строчке №', {i}, 'количество слов;', {len(word)})


