#Data from Headline Dataset on Kaggle

import pandas as pd
import numpy as np, re
from nltk.stem.porter import PorterStemmer
from sklearn.utils import all_estimators
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score
import pickle
import matplotlib as plt

np.random.seed(0)

data = pd.read_json("./sarcasmData/data.json", lines = True)

data['headline'] = data['headline'].apply(lambda s : re.sub('[^a-zA-Z]', ' ', s))

x = data['headline']
y = data['is_sarcastic']
ps = PorterStemmer()
x = x.apply(lambda x: x.split())
x = x.apply(lambda x : ' '.join([ps.stem(word) for word in x]))

tv = TfidfVectorizer(max_features = 5000)


x = list(x)
x = tv.fit_transform(x).toarray()
pickle.dump(tv, open("./models/vectorizer.pickle", "wb"))
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .4, random_state = 0)

lgModel = LogisticRegression(verbose = 0)
lnModel = LinearSVC(verbose = 0)
gaussModel = GaussianNB()
randomForest = RandomForestClassifier(verbose = 0)
xgboost = XGBClassifier()
bernoulli = BernoulliNB()


models = [lgModel, lnModel, gaussModel, randomForest, xgboost, bernoulli]
modelNames = ['LogisticRegression', 'LinearSVC', 'GaussianNB', 'RandomForestClassifier', 'XGBClassifier', 'BernoulliNB', 'ensemble']

modelPerformances = []

modelProbas = []

for i in range(len(models)):
    
    models[i].fit(x_train, y_train)

    y_pred = models[i].predict(x_test)


    estimators = all_estimators()

    goodEstimators = []
    for name, class_ in estimators:
        if hasattr(class_, 'predict_proba'):
            goodEstimators.append(name)

    if modelNames[i] in goodEstimators:
        y_pred_proba = models[i].predict_proba(x_test)[::,1]

        modelProbas.append(y_pred_proba)

    score = roc_auc_score(y_test, y_pred)

    modelPerformances.append(score)

    print("Model", modelNames[i], ":", score, "ROC AUC")



ensembleResults = [0] * len(y_test)

for i in modelProbas:
    ensembleResults = ensembleResults + i

ensemblePreds = np.asarray([1 if i >= .5 else 0 for i in ensembleResults]) / len(models)

score = roc_auc_score(y_test, ensemblePreds)

modelPerformances.append(score)

print("Model: ensemble :", score, "ROC AUC")


print("Best Model is:", modelNames[np.argmax(modelPerformances)], "with ROC_AUC of", modelPerformances[np.argmax(modelPerformances)])

for i in range(len(models)):
    filename = './models/{}.sav'.format(modelNames[i])
    pickle.dump(models[i], open(filename, 'wb'))