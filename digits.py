from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import metrics

digits = datasets.load_digits()
fig = plt.figure()

# print(digits.DESCR)

X = digits.data
y = digits.target
# print(X.shape)
# print(y.shape)

# for i, x in enumerate(X[0:10], 0):
#     sp = fig.add_subplot(2, 5, (i + 1))
#     sp.imshow(x.reshape(8, 8), cmap = "gray")
# plt.show()

X_train = X[:1201]
X_test  = X[1201:]
y_train = y[:1201]
y_test  = y[1201:]

classifier = SVC(kernel = "linear", gamma = "scale")
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

# 学習結果
print(y_pred)
# テストデータ
print(y_test)
# 評価
print(metrics.accuracy_score(y_test, y_pred))