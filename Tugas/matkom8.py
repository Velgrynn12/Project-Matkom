# MULAI
# Mengimpor library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz, export_text
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from IPython.display import Image
import pydotplus

df = pd.read_csv(r'C:\Users\INDAH HARIYANTI\Downloads\datafikesabiessyaallah.csv')

# Menampilkan data
print(df.head())

target = 'Status'
features = [col for col in df.columns if col != target]

X = df[features]
y = df[target]

le = preprocessing.LabelEncoder()
for col in X.select_dtypes(include=['object']).columns:
    X.loc[:, col] = le.fit_transform(X[col])  # Perbaikan menggunakan .loc[]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf = DecisionTreeClassifier(criterion='entropy', random_state=42)


clf.fit(X_train, y_train)


y_pred = clf.predict(X_test)

# Evaluasi
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")


print("\nPohon Keputusan:")
tree_rules = export_text(clf, feature_names=features)
print(tree_rules)

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree


plt.figure(figsize=(12, 8))  
plot_tree(clf, filled=True, feature_names=X.columns, class_names=['Tidak Lulus', 'Lulus'], rounded=True)
plt.show()