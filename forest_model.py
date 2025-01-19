from sklearn import datasets
import seaborn as sns
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes(as_frame=True)
print(diabetes['data'].columns)
df_diabetes = diabetes['data']
# df_diabetes.head()
# print(diabetes['target'][:20])
df_diabetes['target'] = diabetes['target']

#sns.heatmap(df_diabetes.corr(), annot=True)
sns.scatterplot(df_diabetes, x='bp', y='target')
plt.show()
# Создаем данные
# X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# # Обучение модели
# model = RandomForestRegressor(n_estimators=100, max_depth=5)
# model.fit(X_train, y_train)
#
# # Предсказания
# predictions = model.predict(X_test)
