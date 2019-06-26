import pandas as pd
import numpy as np
import collections
import csv

# returns count of all words in column A in csv input. delete headers first.
# removes all non-alphanumeric characters from words
def wordCountHash(fileName):
    df = pd.read_csv(fileName)
    numpy_matrix = df.as_matrix()
    x = []
    y = numpy_matrix.tolist()
    
    for each in y:
        x += each

    z = []
    for each in x:
        z.append(each.split(" "))

    a = []
    for each in z:
        a += each

    a = ["".join([ c.lower() if c.isalnum() else "" for c in word ]) for word in a]

    dict1 = {}
    for each in a:
        if each in dict1.keys():
            dict1[each] += 1
        else:
            dict1[each] = 1

    g = sorted(dict1.items(), reverse=True, key=lambda x: x[1])
    
    return(g)

def writeToCSV(arr, filename):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for val in arr:
            writer.writerow([val])

writeToCSV(wordCountHash("fb.csv"), "output.csv")
