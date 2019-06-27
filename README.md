#  Bayesian Deep Learning Classification Swiss Vector Machine

A Naiive Bayes Classifier tool for UBS hackers to find correlations between stock prices and news headlines

<img src="wordcloud.png"
     alt="Facebook Wordcloud"
     style="float: left; margin-right: 10px; height: 10px;" />


## How it Works 

Facebook news headline data was scraped by a few lines in R:

```r

require(rvest)

url <-  'https://www.wsj.com/search/term.html?KEYWORDS=facebook'
        
webpage <- read_html(url)
        homepage_data <- html_nodes(webpage, '.summary-container p , +
        .headline-container .headline a')
                data <- html_text(homepage_data)

write.csv(data, "facebook.csv", row.names=F)      

```

## Using the NLTK Library

A python model parsed the raw csv data headlines and returned a JSON object with classification vectors based on a pre-trained model in nltk 

```bash 
pip install nltk 
```

Model calculates polarity score:

```python 
for line in wordCountHashSet(headlineCSV):
     pol_score = sia.polarity_scores(line)
     pol_score['headline'] = line
     results.append(pol_score)

# writes to json
with open('data.json', 'w') as outfile:  
    json.dump(results, outfile, indent=4)
```

The returned JSON Object with metrics:

```txt
 {
    "neg": 0.0,
    "neu": 1.0,  <- sentiment ranking
    "pos": 0.0,
    "compound": 0.0,
    "headline": "A senior Facebook executive, Nick Clegg, took a veiled shot at Apple, 
                 continuing the sniping between the tech giants as their business models 
                 are under increasing scrutiny from global regulators."
  }

```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
None
