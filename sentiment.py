import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np


sia = SentimentIntensityAnalyzer()

def yay (text):
    return f"yay {text} !!!!"

results = sia.polarity_scores("Wow, NLTK sucks ass!")
bagResults = [results['neg'], results['neu'], results['pos']]

if np.argmax(bagResults) == 2:
    print("Positive Sentiment")
elif np.argmax(bagResults) == 1:
    print("Neutral Sentiment")
else:
    print("Negative Sentiment")
