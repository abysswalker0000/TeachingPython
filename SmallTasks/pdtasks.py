import pandas as pd
import numpy as np

data = {
    "Имя": ["Аня", "Дима", "Лена", "Саша"],
    "Математика": [85, 90, 75, 95],
    "Физика": [80, 85, 70, 88],
    "Информатика": [90, 88, 82, 92]
}

df = pd.DataFrame(data)
df["Mean"] = df[["Математика", "Физика", "Информатика"]].mean(axis=1)
filtered = df[df["Mean"] > 80]
best_student = df.loc[df["Mean"].idxmax(), "Имя"]
print(df)
print(filtered)
print(best_student)



data = {
    "Товар": ["Хлеб", "Молоко", "Сыр"],
    "День1": [50, 80, 120],
    "День2": [60, 90, 150],
    "День3": [70, 85, 130]
}
df = pd.DataFrame(data)
df["SumForDays"] = df[["День1", "День2", "День3"]].sum(axis=1)
daily_totals = df[["День1", "День2", "День3"]].sum()
best_day = daily_totals.idxmax()
high_sales = df[df[["День1", "День2", "День3"]].gt(100).any(axis=1)]
print(high_sales)
print(best_day)
print(daily_totals)


data = {
    "Имя": ["Катя", "Миша", "Олег", "Света"],
    "Проект1": [80, 65, 90, 70],
    "Проект2": [85, 70, 95, 75],
    "Проект3": [90, 60, 85, 80]
}
df = pd.DataFrame(data)
df["Mean"] = df[["Проект1","Проект2","Проект3",]].mean(axis=1)
filtered = df[df["Mean"]>75]

miniman = df.loc[df["Mean"].idxmin(), "Имя"]

print(filtered)
print(df)
print(miniman)


data = {
    "Блюдо": ["Суп", "Паста", "Салат"],
    "День1": [40, 60, 30],
    "День2": [50, 55, 45],
    "День3": [30, 70, 25]
}
df = pd.DataFrame(data)
df["Общая сумма"] = df[["День1","День2","День3"]].sum(axis=1)
total = df[["День1","День2","День3"]].sum()
minimum = total.idxmin()
nice_sales = df[df[["День1","День2","День3"]].gt(50).any(axis=1)]
print(df)
print("Суммы заказов по дням:")
print(total)
print("Блюда с заказами > 50 в любой день:")
print(nice_sales[["Блюдо", "Общая сумма"]])
print(f"\nДень с минимальным количеством заказов: {minimum} : {total[minimum]}")




data = {
    "Название": ["Война и мир", "Гарри Поттер", "Мастер и Маргарита", "1984", "Шантарам"],
    "Страницы": [1200, 400, 350, 250, 900],
    "Выдачи": [5, 25, 15, 8, 30]
}
df = pd.DataFrame(data)
df["Популярность"] = df["Выдачи"].apply(lambda x: "Высокая" if x>20 else "Средняя" if 10<=x<=20 else "Низкая" )
filtered = df[df["Страницы"]>300].sort_values(by="Выдачи", ascending=False)
print(f"Отфильтрованная таблица : \n{filtered}")
total = df.loc[df["Страницы"].idxmax(), ["Название", "Страницы"]]
print(f"Книга с большим кол-вом страниц - {total["Название"]} с {total["Страницы"]} страниц")


data = {
    "Имя": ["Игорь", "Алина", "Сергей", "Маша"],
    "Дисциплина1": [85, 70, 90, 55],
    "Дисциплина2": [80, 65, 95, 60],
    "Дисциплина3": [90, 75, 85, 50],
    "Возраст": [25, 22, 30, 28]
}
df = pd.DataFrame(data)
df["Средний балл"] = df[["Дисциплина1", "Дисциплина2", "Дисциплина3"]].mean(axis=1)
df["Результат"] = df["Средний балл"].apply(lambda x: "Отличный" if x > 80 else "Хороший" if 60<=x<=80 else "Удовлетворительный")
df = df.drop("Возраст", axis=1)
df = df[df["Результат"].isin(["Отличный", "Хороший"])]
df = df.sort_values(by = "Средний балл", ascending = 0)
best = df.loc[df["Дисциплина1"].idxmax(), "Имя"]
print(f"Таблица после изменений : \n {df}")
print(f"Лучший по 1 дисциплине - {best}") 

