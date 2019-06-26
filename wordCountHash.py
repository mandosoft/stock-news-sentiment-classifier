import pandas as pd
import numpy as np
import csv
from collections import Counter

# returns count of all words in column A in csv input called fileName. delete headers first.
# removes all non-alphanumeric characters from words
def wordCountHash(fileName):
    df = pd.read_csv(fileName)
    numpy_matrix = df.as_matrix()
    x = []
    y = numpy_matrix.tolist()
    
    # converts to 1D array
    for each in y:
        x += each
    z = []
    for each in x:
        z.append(each.split(" "))
    a = []
    for each in z:
        a += each
        
    # removes all non-alphanumeric characters
    a = ["".join([ c.lower() if c.isalnum() else "" for c in word ]) for word in a]
    
    g = Counter(a).most_common()
    
    return(g)

# writes Counter returned from wordCountHash to csv.
def writeToCSV(cnter, filename):
    with open(filename,"w") as f:
        writer=csv.writer(f, lineterminator="\r\n") 
        writer.writerow(['Word', 'Frequency'])
        writer.writerows(cnter)
        
# e.g.
writeToCSV(wordCountHash("fb.csv"),"fboutput5.csv")