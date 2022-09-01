from signal import strsignal
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
import os

# Repository root path
root = str(os.path.dirname(__file__))

# Read CSV FILE
df = pd.read_csv(root + '/Input/final_input.csv')

# Load Commit msg & Result label 
strs = df.iloc[:, [1]].to_numpy()
label = df.iloc[:, [2]].to_numpy()

# Flat the vector & transform input format
corpus = strs.flatten()
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
feature_vectors = X.toarray()

# 70% training and 30% test
X_train, X_test, y_train, y_test = train_test_split(feature_vectors, label, test_size=0.3, shuffle=True) 
gnb = MultinomialNB()
gnb.fit(X_train, y_train)

# Output(label)
y_pred = gnb.predict(X_test)
print(y_pred)
print(f'Accuracy: {metrics.accuracy_score(y_test, y_pred)}')

# Ouput(P score)
yv_pred = gnb.predict_proba(X_test)
print(yv_pred)
