# -*- coding: utf-8 -*-
import scrapy

# we will use a crawl spider
from scrapy.spiders import CrawlSpider

# rules are used by crawl spider to control is behaviour
from scrapy.spiders import Rule

from scrapy.linkextractors import LinkExtractor

# importing item here
from reddit.items import RedditItem

class PictureSpider(CrawlSpider):
    # create spider named picture using genspider command
    name = "picture"

    # spider is limited to this domain
    allowed_domains = ["www.reddit.com"]

    # start point for spider
    start_urls = ['http://www.reddit.com/']

    # rules are essentially to tell spider which links to follow
    # consider the following links, and observe the regex where there is number after count and
    # after=, there is a string.
    # https://www.reddit.com/r/pics/?count=26&before=t3_6gkifv
    # https://www.reddit.com/r/pics/?count=25&after=t3_6gkzmd
    # https://www.reddit.com/r/pics/?count=50&after=t3_6ggkmk

    # here callback is the action that needs to be taken if the link matches the pattern
    # follow =  True , we are telling the spider to follow the link

    rules = [
        Rule(LinkExtractor(allow=[r'/?count=\d+&after=\w*']),
             callback='parse_item',
             follow=True)
    ]

    # so when the function is called, it passed the response of the link as an object !

    def parse_item(self,response):
        # div with class=thing, is where title and url is
        # got xpath by inspecting element
        # // *[ @ id = "thing_t3_6gkm6e"] / div[2] / p[1] / a
        # xpath is read as inside div with class=thing ,second div tag > first p tag > a tag and text() inside it

        # url currently scrapping
        url = response.url

        # all div tags with thing class
        divs = response.css('div.thing')

        for div in divs:
            # creating item instance
            item = RedditItem()

            # text() is to get the text between tags !
            title = div.xpath('div[2]/p[1]/a/text()').extract()

            # href is a property which is extracted by @
            img_link = div.xpath('div[2]/p[1]/a/@href').extract()

            # setting item field
            item['title'] = title
            item['img_link'] = img_link

            yield item



