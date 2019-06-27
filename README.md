#  Bayesian Deep Learning Classification Swiss Vector Machine

A Naiive Bayes Classifier tool for UBS hackers to find correlations between stock prices and news headlines

## How it Works 

News headline data was scraped by a custom web scrapin tool with R:

```r

url <-  'https://www.wsj.com/search/term.html?KEYWORDS=facebook'
        
webpage <- read_html(url)
homepage_data <- html_nodes(webpage, '.summary-container p , .headline-container .headline a')
data <- html_text(homepage_data)

write.csv(data, "facebook.csv", row.names=F)      

```

## Generate an API Key and run commands from terminal

```bash
curl https://newsapi.org/v2/everything -G \
    -d q=Facebook \
    -d sources=the-wall-street-journal \
    -d from=2019-05-29 \
    -d to=2019-06-27 \
    -d sortBy=popularity \
    -d apiKey=8f8daf483b3741aba5a24a99b1ac0f2b >output.json
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
