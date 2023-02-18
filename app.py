
from os import environ
from flask import Flask, abort, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import pickle
import sentiment
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "<p>Hello, DivHacksMLBackend!</p>"

@app.route('/test/')
def test():
    return "<p>Hello, DivHacksMLBackend!!!!!!!!</p>"
    
@app.route('/sarcasm/', methods = ['POST'])
def sarcasm():
    x = request.get_json()["text"]
    x2 = request.get_json()["text"]
    print(x)
    cv = pickle.load(open("./models/vectorizer.pickle", 'rb')) 

    filename = 'models/lgModel.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    x = cv.transform([x])
    output = loaded_model.predict(x)[0]
    if output == 1:
        return "Sarcastic"
    else:
        sia = SentimentIntensityAnalyzer()

        results = sia.polarity_scores(x2)
        bagResults = [results['neg'], results['neu'], results['pos']]

        if np.argmax(bagResults) == 2:
            return "Positive Sentiment"
        elif np.argmax(bagResults) == 1:
            return "Neutral Sentiment"
        else:
            return "Negative Sentiment"

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=environ["PORT"])
