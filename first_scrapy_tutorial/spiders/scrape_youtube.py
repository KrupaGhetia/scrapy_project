# -*- coding: utf-8 -*-
import scrapy
from first_scrapy_tutorial.items import ScrapeYoutubeItem

class ScrapeYoutubeSpider(scrapy.Spider):
    name = 'scrape_youtube'
    allowed_domains = ['youtube.com']
    start_urls = ['https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/channels']

    def parse(self, response):
        items = []
        for channels in response.css('ul.channels-browse-content-grid li.channels-content-item'):
            for channel_content in channels.css('div.yt-lockup-channel'):
                item = ScrapeYoutubeItem()
                item['channel_title'] = channel_content.css('div.yt-lockup-content h3.yt-lockup-title a.spf-link::text')[0].extract()
                item['channel_img_url'] = 'https:' + channel_content.css('div.yt-lockup-thumbnail a.spf-link span.yt-thumb span.yt-thumb-square span.yt-thumb-clip img::attr(src)')[0].extract()
                item['no_of_subscribers'] = channel_content.css('div.yt-lockup-content span.yt-uix-button-subscription-container span.yt-uix-tooltip::attr(aria-label)')[0].extract()
                item['links_to'] = response.urljoin(channel_content.css('div.yt-lockup-thumbnail a::attr(href)')[0].extract())                
                items.append(item)
        return items