from final import created_date
deadline_date = input("Введите дату дедлайна в формате 'дд-мм-гггг': ")    # Запрашиваем у пользователя дату дедлайна

try:
    # Преобразуем введенную строку в объект даты
    deadline_date = created_date.strptime(deadline_input, "%d-%m-%Y")
except ValueError:
    print("Неверный формат даты. Пожалуйста, используйте формат 'дд-мм-гггг'.")
    return


current_date = datetime.now()                 # Получаем текущую дату


if deadline_date < current_date:
    print("Дедлайн истёк! Пожалуйста, примите меры.")
elif deadline_date == current_date:                                     # Сравниваем даты
    print("Сегодня последний день для выполнения задачи!")
else:

    remaining_days = (deadline_date - current_date).days
    print(f"До истечения дедлайна осталось {remaining_days} дней.")             # Вычисляем разницу в днях