import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
from first_scrapy_tutorial.items import ScrapeYoutubeItem

class ScrapeYoutubePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host='localhost', user='dev', passwd='dev', db='youtube_scraped_data', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()
        self.cursor.execute("USE youtube_scraped_data")

    def process_item(self, item, spider):
        try:
            self.cursor.execute("""INSERT INTO channels(channel_title, channel_img_url, no_of_subscribers, links_to)
                        VALUES (%s, %s, %s, %s)""",
                        (item['channel_title'].encode('utf-8'),
                         item['channel_img_url'].encode('utf-8'),
                         item['no_of_subscribers'].encode('utf-8'),
                         item['links_to'].encode('utf-8')))
            self.conn.commit()
        except (MySQLdb.Error) as e:
            print(e)
        return item
