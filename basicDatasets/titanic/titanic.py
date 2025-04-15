import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df["Age"] = df["Age"].fillna(df["Age"].mean())
def get_age_category(age):
    if pd.isna(age) or age > 60:
        return "Пожилой"
    elif age < 18:
        return "Ребенок"
    return "Взрослый"
df["Категория возраста"] = df["Age"].apply(get_age_category)
filtered_passengers = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]

filtered_passengers = filtered_passengers.sort_values(by = "Fare", ascending = False)

age_counts = df["Категория возраста"].value_counts()
print(f"Всего было :\n{age_counts}")

all_survivors = df.groupby("Sex")["Survived"].sum()
print(f"Всего выжило людей :\n{all_survivors}")

survived_men = df[(df["Sex"] == "male") & (df["Survived"] == 1)]
avg_age_surv_men = survived_men["Age"].mean()
print(f"Средний возраст выживших мужчин - {avg_age_surv_men:.2f} лет")

mean_fare_men = survived_men["Fare"].mean()
print(f"Средняя стоимость проезда выживших мужчин - {mean_fare_men:.2f}")

survived_women = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
avg_age_surv_women = survived_women["Age"].mean()
print(f"Средний возраст выживших женщин  - {avg_age_surv_women:.2f} лет")

mean_fare_women = survived_women["Fare"].mean()
print(f"Средняя стоимость проезда выживших женщин - {mean_fare_women:.2f}")

embark_groups_mean_age = df.groupby("Embarked")["Age"].mean()
print(embark_groups_mean_age)

children_survivors = df[(df["Категория возраста"] == "Ребенок") & (df["Survived"] == 1)]
children_by_class = children_survivors.groupby("Pclass").size().reset_index(name="Survived_Count")
print(children_by_class)

sns.barplot(data=children_by_class, x="Survived_Count", y="Pclass")
plt.xlabel("Количество выживших")
plt.ylabel("Класс")
plt.show()


sns.barplot(data=df, x="Embarked", y="Age", estimator="mean")
plt.xlabel("Порт")
plt.ylabel("Возраст")
# plt.show()

sns.countplot(x = "Pclass", hue = "Survived", data = df)
plt.title("Выжившие по классам")
# plt.show()

sns.histplot(data=df, x="Age", hue="Survived", bins=40)
plt.title("Гистограмма выживших по возрасту")
plt.xlabel("Возраст")
plt.ylabel("Количество")
# plt.show()

sns.boxplot(data=df, y="Fare", x="Pclass")
plt.title("Распределение стоимости билетов по классам")
plt.xlabel("Класс")
plt.ylabel("Стоимость билета")
# plt.show()

sns.scatterplot(data=df, y = "Age", x="Fare", hue="Survived")
plt.title("Зависимость возраста и стоимости билета")
plt.xlabel("Цена")
plt.ylabel("Возраст")
# plt.show()