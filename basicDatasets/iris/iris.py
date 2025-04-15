import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


df = pd.read_csv("IRIS.csv")

def get_species_prediction(petal_length):
    if 0<petal_length<2.1:
        return "Iris-setosa"
    elif 2.1<petal_length<4.7:
        return "Iris-versicolor"
    return "Iris-virginica"

df["Specie prediction"] = df["petal_length"].apply(get_species_prediction)
df["successful_predictions"] = df["Specie prediction"] == df["species"]
accuracy = df["successful_predictions"].sum() / len(df)
# print(f"Доля успешных предсказаний - {accuracy}")

df["petal_ratio"] = df["petal_length"] / df["petal_width"]
mean_ratio_evert_spiece = df.groupby("species")["petal_ratio"].mean()
# print(f"Среднее значение отношения длины к ширине каждого вида :\n {mean_ratio_evert_spiece}")

mean_petal_length = df.groupby("species")["petal_length"].mean()
# print(f"Средняя длина лепестка каждого вида: \n {mean_petal_length}")

min_sepal_width = df.groupby("species")["sepal_width"].min()
# print(f"Минимальная ширина чашелистика для каждого вида:\n{min_sepal_width}")

max_sepal_width = df.groupby("species")["sepal_width"].max()
# print(f"Максимальная ширина чашелистика для каждого вида:\n{max_sepal_width}")

mean_sepal_width = df.groupby("species")["sepal_width"].mean()
# print(f"Средняя ширина чашелистика для каждого вида:\n{mean_sepal_width}")

dependencies_table = df.groupby("species")["sepal_width"].agg(["min", "max", "mean"])
# print(f"Таблица зависимостей :\n{dependencies_table}")

sepal_length_meadian = df.groupby("species")["sepal_length"].median()
# print(f"Медиана длины чашелистика от вида :\n {sepal_length_meadian}")

amount_every_spieces = df["species"].value_counts()

numeric_df = df.select_dtypes(include=["float64", "int64"])
corr_matrix = numeric_df.corr()

X = numeric_df
y = df["species"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42 )
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_predict = model.predict(X_test)
print(pd.DataFrame({"Реальные": y_test, "Предсказанные": y_predict}))
print(f"\nРезультат предсказаний - {accuracy_score(y_test, y_predict)*100}%")
scores = cross_val_score(model,X,y,cv=5, scoring="accuracy")
mean_score = scores.mean()
std_score = scores.std()
print(f"Средняя точность {mean_score:.2f}")
print(f"Стандартное отклонение {std_score:.2f}")



sns.heatmap(data=corr_matrix, annot=True)
plt.title("Корреляция числовых признаковы ирисов")
# plt.show()

plt.pie(amount_every_spieces,autopct="%.1f%%", labels=amount_every_spieces.index)
plt.title("Количество цветов каждого вида в выборке")
# plt.show()

sns.pairplot(data=df, hue="species")
plt.suptitle("Сравнение длины и ширины лепестков")
# plt.show()

sns.violinplot(data=df, x="species", y="sepal_length")
plt.title("Распределение длины чашелистика от его вида")
plt.xlabel("Вид")
plt.ylabel("Длина чашелистика")
# plt.show()

sns.boxplot(data=df, x="species", y="sepal_width")
plt.title("Распределение ширины чашелистика от его вида")
plt.xlabel("Вид")
plt.ylabel("Ширина чашелистика")
# plt.show()


sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species")
plt.title("Зависимость длины лепестка от его ширины")
plt.xlabel("Длина")
plt.ylabel("Ширина")
# plt.show()