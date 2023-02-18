import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import pickle

cv = pickle.load(open("./models/vectorizer.pickle", 'rb')) 

filename = 'models/lgModel.sav'
loaded_model = pickle.load(open(filename, 'rb'))
user = input("Enter a Text: ")
x = cv.transform([user])
output = loaded_model.predict(x)[0]
if output == 0:
    print("not sarcastic")
else:
    print("sarcastic")
