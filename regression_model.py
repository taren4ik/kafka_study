from sklearn import datasets
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes(as_frame=True)
print(diabetes['data'].columns)
df_diabetes = diabetes['data']
# df_diabetes.head()
# print(diabetes['target'][:20])
df_diabetes['target'] = diabetes['target']

#sns.heatmap(df_diabetes.corr(), annot=True)
# sns.scatterplot(df_diabetes, x='s4', y='target')
# plt.show()

# Разбиваем данные для обучения
X_train, X_test, y_train, y_test = train_test_split(
    diabetes['data'].drop(['target'], axis=1),
    diabetes['target'],
    test_size=0.25
)
#
#  Обучение модели
model_linear = LinearRegression().fit(X_train, y_train)
y_prediction = model_linear.predict(X_test)
mae = mean_absolute_error(y_test, y_prediction)
#print(mae)

with open('model.pkl', 'wb') as f:
    pickle.dump(model_linear, f)

# with open('model.pkl', 'rb') as f:
#     model_leaner = pickle.load(f)
# mae = mean_absolute_error(y_test, model_leaner.predict(X_test))
#print(mae)
# model.fit(X_train, y_train)
#
# # Предсказания
# predictions = model.predict(X_test)
