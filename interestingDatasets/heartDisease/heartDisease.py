import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("heart_disease_uci.csv")
# print(df)
df["IsSick"] = df["num"] != 0
# print(df["IsSick"])

df["chol"] = df["chol"].fillna(df["chol"].mean())
df["thalch"] = df["thalch"].fillna(df["thalch"].mean())
df["trestbps"] = df["trestbps"].fillna(df["trestbps"].mean())
df["oldpeak"] = df["oldpeak"].fillna(df["oldpeak"].mean())
# df["ca"] = df["ca"].fillna(df["ca"].mean())
numeric_df = df.select_dtypes(include=(["int64", "float64"]))
corr_matrix = numeric_df.corr()
best_feature = corr_matrix["num"].drop("num").abs().idxmax()
# print(f"Признак {best_feature}, корреляция - {corr_matrix["num"][best_feature]}")

chest_pain_patitent = df.groupby("cp")["IsSick"].sum().reset_index()
# print(chest_pain_patitent)

mean_chol_level = df.groupby("IsSick")["chol"].mean().reset_index()
# print(mean_chol_level)

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
# print(accuracy)
# print(df[["IsSick","IsSickPrediction"]])

patients_for_every_dataset = df.groupby("dataset")["IsSick"].sum().reset_index()
# print(patients_for_every_dataset)

numeric_features = df.filter(items=["age", "chol", "thalch"])

# sns.barplot(data=patients_for_every_dataset, x="dataset", y="IsSick")
# plt.show()

# sns.boxplot(data=df, x="IsSick", y="age")
# plt.show()

# sns.pairplot(data=df, vars=numeric_features, hue="IsSick")
# plt.show()

# sns.barplot(data=mean_chol_level, x="IsSick", y="chol", )
# plt.title("Средний уровень холестерина")
# plt.show()

# sns.countplot(data=df, x="sex", hue="num")
# plt.title("Распределение болезни по полу")
# plt.show()

# sns.boxplot(data=df, hue="IsSick", y="thalch")
# plt.title("Максимальная частота сердечных сокращений")
# plt.show()

# sns.scatterplot(data=df, x="age", y="chol", hue = "IsSick")
# plt.show()

# sns.countplot(data=df, x="cp", hue="IsSick")
# plt.show()

# sns.heatmap(data=corr_matrix, annot=True)
# plt.title("Корреляционная матрица")
# plt.show()

# sns.histplot(data=df, hue="IsSick", x="age", bins=30)
# plt.title("Зависимость болезней от возраста")
# plt.show()

# sns.boxplot(data=df, x='num', y='chol')
# plt.title("Разброс холестерина в зависимости от типа болезни")
# plt.show()

for_prediction_df = numeric_df.drop(columns= ['num','ca', 'trestbps'])

# X = for_prediction_df
# print(X)
# y = df["IsSick"]
# X_train, X_test, y_train,y_test = train_test_split(X, y ,test_size=0.2, random_state=42)
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train,y_train)
# y_predict = model.predict(X_test)
# print(pd.DataFrame({"Реальные": y_test, "Предсказанные": y_predict}))
# print(f"\nРезультат предсказаний - {accuracy_score(y_test, y_predict)*100}%")
# score = cross_val_score(model, X, y, cv = 20, scoring="accuracy")
# mean_score = score.mean()
# std_score = score.std()
# print(f"Средняя точность {mean_score:.2f}")
# print(f"Стандартное отклонение {std_score:.2f}")

# sns.heatmap(X.corr(), annot=True)
# plt.show()

X = for_prediction_df
y = df["IsSick"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
logreg = LogisticRegression(max_iter=1000)
knn = KNeighborsClassifier(n_neighbors=10)
tree = DecisionTreeClassifier(random_state=42, max_depth=4)
forest = RandomForestClassifier(n_estimators=100, random_state=42)
logreg_scores = cross_val_score(logreg,X_scaled,y,cv =5, scoring="accuracy")
knn_scores = cross_val_score(knn,X_scaled,y,cv =5,scoring="accuracy")
tree_scores = cross_val_score(tree,X_scaled,y,cv =5,scoring="accuracy")
forest_scores = cross_val_score(forest, X_scaled,y, cv = 5, scoring = "accuracy")
forest.fit(X_scaled, y)
feature_importance = pd.DataFrame({"Feature": X.columns, "Importance": forest.feature_importances_})
print(feature_importance.sort_values(by="Importance", ascending=False))
sns.barplot(data=feature_importance, x="Importance", y="Feature")
plt.title("Важность признаков")
plt.show()

print(f"Логистическая регрессия: {logreg_scores.mean():.2f} (±{logreg_scores.std():.2f})")
print(f"KNN: {knn_scores.mean():.2f} (±{knn_scores.std():.2f})")
print(f"Дерево решений: {tree_scores.mean():.2f} (±{tree_scores.std():.2f})")
print(f"RandomForest:{forest_scores.mean():.2f} (±{forest_scores.std():.2f})")
sns.barplot(x=["LogReg", "KNN", "Tree", "RandomForest"], y=[logreg_scores.mean(), knn_scores.mean(), tree_scores.mean(), forest_scores.mean()])
plt.title("Сравнение средних точностей")
plt.show()