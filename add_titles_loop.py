
titles = [] # список для заголовков



while True:
    title = input("Введите название заголовка(нажмите enter или введите слово 'стоп' для завершения): ") #ввод заголовков

    if (title == "стоп" or title== ""):         #проверка на слово завершения
        break                                   #остановка цикла при вводе 'стоп' либо при пустом вводе
    else:
        titles.append(title)                    #добавление заголовка в список


print("Зголовки заметки:")
                                                #вывод списка заголовков
for i in titles:
    print(i)