#  Bayesian Deep Learning Classification Swiss Vector Machine

A Naiive Bayes Classifier tool for UBS hackers to find correlations between stock prices and news headlines

## How it Works 

Facebook news headline data was scraped by a few lines in R:

```r

require(rvest)

url <-  'https://www.wsj.com/search/term.html?KEYWORDS=facebook'
        
webpage <- read_html(url)
        homepage_data <- html_nodes(webpage, '.summary-container p , .headline-container .headline a')
                data <- html_text(homepage_data)

write.csv(data, "facebook.csv", row.names=F)      

```

## A Python model using the NLTK library parsed the raw data and returned a JSON object 

```python 
for line in wordCountHashSet(headlineCSV):
     pol_score = sia.polarity_scores(line)
     pol_score['headline'] = line
     results.append(pol_score)

# writes to json
with open('data.json', 'w') as outfile:  
    json.dump(results, outfile, indent=4)
```

### This Returns a Parsable JSON file 

```json
"source": {
        "id": "the-wall-street-journal",
        "name": "The Wall Street Journal"
      },
      "author": "Alexandra Bruell",
      "title": "In Sunny Cannes, Marketers Fret Over Dark Content Online...",
      "description": "In Sunny Cannes, Marketers Fret Over Dark Content Online... 
      "url": "https://www.wsj.com/
      "urlToImage": "https://images.wsj.net/im-83771/social",
      "publishedAt": "2019-06-21T11:34:38Z",
      "content": "The Cannes Lions ad festival is a sunny fixture for many in marketing..."
    },
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
None
