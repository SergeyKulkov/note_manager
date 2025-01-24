notes = []          

while True:
    print("\nВведите данные для новой заметки (или введите 'стоп' для завершения):")
    name = input("Имя: ")
    if name.lower() == 'стоп':
        break
    title = input("Заголовок: ")
    description = input("Описание: ")
    status = input("Статус (например, 'выполнено', 'в процессе', 'отложено'): ")
    creation_date = input("Дата создания (в формате дд.мм.гггг): ")
    deadline = input("Дедлайн (в формате дд.мм.гггг): ")

    # Создание словаря для заметки
    note = {
        "Имя": name,
        "Заголовок": title,
        "Описание": description,
        "Статус": status,
        "Дата создания": creation_date,
        "Дедлайн": deadline
    }

    # Добавление заметки в список
    notes.append(note)
    print("Заметка добавлена!")

    # Отображение всех заметок
    if notes:
        print("\nСписок всех заметок:")
        for idx, note in enumerate(notes, start=1):
            print(f"\nЗаметка {idx}:")
            for key, value in note.items():
                print(f"{key}: {value}")
    else:
        print("Нет созданных заметок.")
