username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
title1 = input("Введите подзаголовок(Дополнительный заголовок): ")
title2 = input("Введите подзаголовок(Дополнительный заголовок): ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки (Выполнена, Не выполнена): ")
created_date = input("Введите дату создания заметки (В формате: xx.xx.xxxx): ")
issue_date = input("Введите дату дедлайна заметки (В формате: xx.xx.xxxx): ")

titles = [title, title1, title2]
note = [
    username,              # Имя пользователя
[title, title1, title2],   # Список заголовков
    content,               # Содержимое заметки
    status,                # Статус заметки
    created_date[:-5],     # Дата создания заметки
    issue_date[:-5]        # Дата дедлайна заметки
]

print(note)




