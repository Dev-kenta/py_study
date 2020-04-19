from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics

irisdata = datasets.load_iris()

# print(irisdata.DESCR)
# print(irisdata.feature_names)
# print(irisdata.target_names)
# print(irisdata.target)

X_train, X_test, y_train, y_test = train_test_split(irisdata.data, irisdata.target, test_size = 0.2, train_size = 0.8, shuffle = True)
classifier = SVC(kernel = "linear", gamma = "scale")
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# 学習結果
print(y_pred)
# テストデータ
print(y_test)
# 評価
print(metrics.accuracy_score(y_test, y_pred))