import tkinter as tk  # Импорт модуля tkinter для создания графического интерфейса
import time  # Импорт модуля time для работы с временем
import math  # Импорт модуля math для математических операций

# Функция для обновления показаний часов
def update_clock(canvas, hours_hand, minutes_hand, seconds_hand):
    current_time = time.localtime()  # Получение текущего времени
    current_seconds = current_time.tm_sec  # Получение секунд
    current_minutes = current_time.tm_min  # Получение минут
    current_hours = current_time.tm_hour % 12  # Получение часов в 12-часовом формате

    # Вычисление углов для стрелок часов
    seconds_angle = math.radians((current_seconds - 15) * 6)
    minutes_angle = math.radians((current_minutes - 15) * 6)
    hours_angle = math.radians((current_hours - 3) * 30 + int(current_minutes / 2))

    # Обновление позиций стрелок на холсте
    canvas.coords(seconds_hand, 150, 150, 150 + 70 * math.cos(seconds_angle), 150 + 70 * math.sin(seconds_angle))
    canvas.coords(minutes_hand, 150, 150, 150 + 60 * math.cos(minutes_angle), 150 + 60 * math.sin(minutes_angle))
    canvas.coords(hours_hand, 150, 150, 150 + 50 * math.cos(hours_angle), 150 + 50 * math.sin(hours_angle))

    # Запуск функции обновления каждую секунду
    root.after(1000, update_clock, canvas, hours_hand, minutes_hand, seconds_hand)

# Создание главного окна приложения
root = tk.Tk()
root.title("Analog Clock")  # Заголовок окна

# Создание холста для рисования часов
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

canvas.create_oval(50, 50, 250, 250)  # Создание круга для циферблата
hours_hand = canvas.create_line(150, 150, 150, 100, width=3)  # Создание стрелки часов
minutes_hand = canvas.create_line(150, 150, 150, 90, width=2)  # Создание стрелки минут
seconds_hand = canvas.create_line(150, 150, 150, 80, fill="red")  # Создание стрелки секунд

# Запуск функции обновления времени на часах
update_clock(canvas, hours_hand, minutes_hand, seconds_hand)

# Запуск главного цикла обработки событий
root.mainloop()