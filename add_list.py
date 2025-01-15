username = input("Пожалуйста, введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
title1 = input("Введите заголовок №2: ")
title2 = input("Введите заголовок №3: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки (Выполнена, Не выполнена): ")
created_date = input("Введите дату создания заметки (В формате: xx.xx.xxxx): ")
issue_date = input("Введите дату дедлайна заметки (В формате: xx.xx.xxxx): ")

titles = [title, title1, title2]





print("Заметка пользователя: ", username)
print("Заголовок заметки(Допольнительные заголовки, подзаголовки): ", titles)
print("Содержание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_date[:-5])
print("Дата дедлайна заметки: ", issue_date[:-5])
