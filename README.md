#  BayesWave Indicator Deep Learning Classification Vector Machine

A Naiive Bayes Classifier tool for UBS hackers to find correlations between stock prices and news headlines

## How it Works 

Wall Street Journal articles are mined using [News API](https://newsapi.org) which returns JSON files: 

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
