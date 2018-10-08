import sys

# объявим где хранятся исходные данные
PATH_STOR = 'storage.csv'
PATH_SCHEME = sys.argv[1]

# объявим куда сохраним результат
PATH_RES = sys.argv[2]

# создаем словарь для хранения статистики
store = {}

# открываем файл на чтение в режиме текста
fl = open(PATH_STOR, 'rt', encoding='utf-8')

# считываем первую строчку - заголовок (она нам не нужна)
fl.readline()

# в цикле читаем строчки из файла
for line in fl:
    # разбиваем строчку на две строковые переменные
    numb, name = line.strip().split(',')
    numb = int(numb)
    # добавляем в словарь содержимые склада, где ключ - деталь, значение - количество
    store[name] = numb

# закрываем файл
fl.close()

# открываем файл на чтение в режиме текста
fl = open(PATH_SCHEME, 'rt', encoding='utf-8')

# считываем первую строчку - заголовок (она нам не нужна)
fl.readline()

# в цикле читаем строчки из файла
for line in fl:
    # разбиваем строчку на две строковые переменные
    numb, name = line.strip().split(',')
    numb = int(numb)
    if name in store:
    	# если на складе содержится достаточное количество деталей
    	if store[name] >= numb:
    		store[name] -= numb
    	else:
    		print(PATH_SCHEME + " содержит неприемлимый список для создания изделий")
    		fl.close()
    		exit()
    # если в списке схем содержится деталь, которой нет на складе
    else:
    	print(PATH_SCHEME + " содержит неприемлимый список для создания изделий")
    	fl.close()
    	exit()

# открываем файл на запись в режиме текста
out_fl = open(PATH_RES, 'wt', encoding='utf-8')

# записываем заголовок таблицы
out_fl.write('Количество, Название\n')

# запись оставшихся элементов в файл
for key, value in store.items():
	out_fl.write('%s,%s\n' % (value, key) )
# закрываем файлы
out_fl.close()
print("Ура, мы создали изделие!!!")