# Reddit-Image-Scrapper-in-Python
### Scrapy Bot 
Scrapy is an open source and collaborative framework for extracting the data you need from websites.
In a fast, simple, yet extensible way.

To install scrapy on Ubuntu 
```bash
pip install scrapy
```

Some basics :
To scrap any kind of data, we need to have a template for that data, this is defined in scrapy with the help of
'item' object.
For example:
To get images from reddit, we need a template that defines the image name and url to download the image.

We use Spider object to traverse through pages, you can call it the heart of the scrapy engine.
It defines how we traverse and extract the data.

We use pipeline object to deal with extracted data.

To start a project 
```bash
scrapy startproject reddit
```
All the following commands need to be run from within the project folder

To generate a spider
```bash
scrapy genspider <spider-name> [spider-link/url-of-website]
```

To list spiders
```bash
scrapy list
```

To run the spider
```bash
scrapy crawl [options] <spider-name>
```

It supports 3 types of output formats
1. Json
2. XML
3. CSV

To output to csv
```bash
scrapy crawl -o output.csv(file-name) -t csv(file type) --nolog <spider-name>
eg.
scrapy crawl -o output.csv -t csv picture
```

Everything else is mentioned in the program 
GLHF


