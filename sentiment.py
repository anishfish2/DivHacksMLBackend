import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np


sia = SentimentIntensityAnalyzer()
x = "i hate it here"
results = sia.polarity_scores(x)
bagResults = [results['neg'], results['neu'], results['pos']]

if np.argmax(bagResults) == 2:
    print("Positive Sentiment")
elif np.argmax(bagResults) == 1:
    print("Neutral Sentiment")
else:
    print("Negative Sentiment")
