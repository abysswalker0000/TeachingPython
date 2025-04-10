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