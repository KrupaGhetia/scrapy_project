import scrapy

class ScrapeYoutubeItem(scrapy.Item):
    channel_title = scrapy.Field()
    channel_img_url = scrapy.Field()
    no_of_subscribers = scrapy.Field()
    links_to = scrapy.Field()
