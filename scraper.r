library(rvest)
library(dplyr)
library(readr)
library(jsonlite)

url <-  'https://www.wsj.com/search/term.html?KEYWORDS=facebook&page=5'
        
webpage <- read_html(url)
homepage_data <- html_nodes(webpage, '.summary-container p , .headline-container .headline a')
data <- html_text(homepage_data)

write.csv(data, "facebook5.csv", row.names=F)      

