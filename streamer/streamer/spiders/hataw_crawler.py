import scrapy
import urlparse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from streamer.items import StreamerItem

class HatawSpider(scrapy.Spider):
	name = "hataw"

	start_urls = [
		'http://www.hatawtabloid.com/category/news/page/2/',
	]

	def parse(self, response):
		item_urls = response.xpath("//div[@class='post-listing']/article[@class='item-list']/h2//a/@href").extract()

		for url in item_urls:
			item_url = urlparse.urljoin(response.url, url)
			yield scrapy.Request(item_url,self.parseItem)

		next = int(response.xpath("//div[@class='pagination']/span[@class='current']/text()").extract()[0]) + 1
		next_page =  response.xpath("//div[@class='pagination']//a[.="+str(next)+"]/@href").extract()[0]

		if next_page is not None:
		 	next_page = response.urljoin(next_page)
		 	yield scrapy.Request(next_page, self.parse)


	def parseItem(self, response):
		item = StreamerItem()
		item['title'] = response.xpath("//div[@class='post-inner']//h1[@class='post-title entry-title']/text()").extract()
		item['content'] = response.xpath("//div[@class='entry']//p/text()").extract()
		item['category'] = ''
		yield item
