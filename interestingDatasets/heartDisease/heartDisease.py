import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("heart_disease_uci.csv")
df["IsSick"] = df["num"] != 0
# print(df["IsSick"])

df["chol"] = df["chol"].fillna(df["chol"].mean())
numeric_df = df.select_dtypes(include=(["int64", "float64"]))
corr_matrix = numeric_df.corr()
best_feature = corr_matrix["num"].drop("num").abs().idxmax()
# print(f"Признак {best_feature}, корреляция - {corr_matrix["num"][best_feature]}")

chest_pain_patitent = df.groupby("cp")["IsSick"].sum().reset_index()
# print(chest_pain_patitent)

mean_chol_level = df.groupby("IsSick")["chol"].mean().reset_index()
print(mean_chol_level)

mean_thlach = df.groupby("IsSick")["thalch"].mean()
# print(mean_thlach)

def chol_to_check(chol):
    if 170<chol<280:
        return False
    else:
        return True

df["IsSickPrediction"] = df["chol"].apply(chol_to_check)
df["SuccesfulPredictions"] = df["IsSick"] == df["IsSickPrediction"]
accuracy = df["SuccesfulPredictions"].sum() / len(df)
print(accuracy)
print(df[["IsSick","IsSickPrediction"]])

numeric_features = df.filter(items=["age", "chol", "thalch"])

sns.boxplot(data=df, x="IsSick", y="age")
# plt.show()

sns.pairplot(data=df, vars=numeric_features, hue="IsSick")
# plt.show()

sns.barplot(data=mean_chol_level, x="IsSick", y="chol", )
plt.title("Средний уровень холестерина")
# plt.show()

sns.countplot(data=df, x="sex", hue="num")
plt.title("Распределение болезни по полу")
# plt.show()

sns.boxplot(data=df, hue="IsSick", y="thalch")
plt.title("Максимальная частота сердечных сокращений")
# plt.show()

sns.scatterplot(data=df, x="age", y="chol", hue = "IsSick")
# plt.show()

sns.countplot(data=df, x="cp", hue="IsSick")
# plt.show()

sns.heatmap(data=corr_matrix, annot=True)
plt.title("Корреляционная матрица")
# plt.show()

sns.histplot(data=df, hue="IsSick", x="age", bins=30)
plt.title("Зависимость болезней от возраста")
# plt.show()

sns.boxplot(data=df, x='num', y='chol')
plt.title("Разброс холестерина в зависимости от типа болезни")
# plt.show()