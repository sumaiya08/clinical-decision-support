#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic mortality prediction using  machine learning methods like logistic 
regression, SVM, Random Forest, etc. 
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Loading dummy data here; you might have to load data via dataframes
data = np.random.randn(2000, 20)
labels = np.random.randint(low=0, high=2, size=2000)

x_train, x_test, y_train, y_test = train_test_split(data, 
                                                    labels, 
                                                    test_size=0.25, 
                                                    random_state=0)

# Run normalization on the features, below is just an example
mu = x_train.mean()
std = x_train.std()
x_train = (x_train - mu)/std
x_test = (x_test - mu)/std

# Pick a model for this task; experiment with others like SVM, Random Forest etc
model = LogisticRegression()

# Start the model fitting process
model.fit(x_train, y_train)

# Run inference on trained model
predictions = model.predict(x_test)

# Get model accuracy
acc = model.score(x_test, y_test)

# Get model area under the curve score
fpr, tpr, thresholds = metrics.roc_curve(y_test, predictions)
auc = metrics.roc_auc_score(y_test, predictions)

# Get model precision, recall and f1 scores
precision, recall, _ = metrics.precision_recall_curve(y_test, predictions)
f1 = metrics.f1_score(y_test, predictions)

# summarize scores
print('*'*30)
print(f'Logistic Regression results: \n')
print(f'\t Acc = {acc:.3f} \n\t AUC = {auc:.3f} \n\t F1={f1:.3f} \n\t')

# Visualize the predictions via confusion matrix 
cm = metrics.confusion_matrix(y_test, predictions)
plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, 
            square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
all_sample_title = 'Accuracy Score: {0}'.format(acc)
plt.title(all_sample_title, size = 15);

# Visualize ROC curve 
plt.figure(figsize=(12,9))
plt.plot(fpr, tpr, marker='+', label='LR')
plt.grid()
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend()
plt.title(f'ROC Curve, AUC = {auc:.3f}')

# Visualize the precision-recall curve
plt.figure(figsize=(12,9))
plt.plot(recall, precision, marker='.', label='LR')
plt.grid()
plt.legend()
plt.ylabel('Precision')
plt.xlabel('Recall')
plt.title(f'Precision-Recall curve')
