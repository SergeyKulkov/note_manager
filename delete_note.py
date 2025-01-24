
    # Создание заметок, пока не не будет написано 'стоп'

while True:
    print("\nВведите данные для новой заметки (для завершения нажите enter или введите 'стоп'):")
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

    notes = []
    notes.append(note)
    print("Заметка добавлена!")

    # Функция для удаления заметок

def delete_notes(criteria, value):
    global notes
    initial_count = len(notes)
    notes = [note for note in notes if note[criteria] != value]
    if len(notes) < initial_count:
        print(f"Удалено заметок: {initial_count - len(notes)}")
    else:
        print("Заметки для удаления не найдены.")

    # Удаление заметок по критериям

while True:
    print("\nВведите критерий для удаления заметок (имя или заголовок), для завершения нажите enter или введите 'стоп':")
    criteria = input("Критерий (имя/заголовок): ").strip().lower()
    if criteria == 'стоп' or '':
        break
    if criteria not in ['имя', 'заголовок']:
        print("Некорректный критерий. Пожалуйста, введите 'имя' или 'заголовок'.")
        continue

    value = input(f"Введите значение для удаления по критерию '{criteria}': ")

    # Удаляем заметки по заданному критерию

    delete_notes(criteria.capitalize(), value)

    # Отображение всех оставшихся заметок

if notes:
    print("\nСписок всех оставшихся заметок:")
    for idx, note in enumerate(notes, start=1):
        print(f"\nЗаметка {idx}:")
        for key, value in note.items():
            print(f"{key}: {value}")
else:
    print("Нет оставшихся заметок.")