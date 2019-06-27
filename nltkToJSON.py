from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import numpy as np
import nltk
import json

# function that returns headlines from csv (column A) as a set
def wordCountHashSet(fileName):
    df = pd.read_csv(fileName)
    numpy_matrix = df.as_matrix()
    x = []
    y = numpy_matrix.tolist()
    z = set()
    for a in y:
    	for b in a:
    		z.add(b)
    return(z)

# input
headlineCSV = input("Enter filename: ")

# calculates score of headlines from csv
headlines = set()
sia = SIA()
results = []
for line in wordCountHashSet(headlineCSV):
     pol_score = sia.polarity_scores(line)
     pol_score['headline'] = line
     results.append(pol_score)

# writes to json
with open('data.json', 'w') as outfile:  
    json.dump(results, outfile, indent=4)
