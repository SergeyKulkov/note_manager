username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки (Выполнена, Не выполнена): ")
created_date = input("Введите дату создания заметки (xx.xx.xxxx): ")
issue_date = input("Введите дату дедлайна заметки (xx.xx.xxxx): ")

print("Заметка пользователя: ", username)
print("Заголовок заметки: ", title)
print("Содержание заметки: ", content)
print("Статус заметки: ", status)
print("Дата создания заметки: ", created_date[:-5])
print("Дата дедлайна заметки: ", issue_date[:-5])
