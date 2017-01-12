import scrapy
import urlparse
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from streamer.items import StreamerItem

class AbanteSpider(scrapy.Spider):
	name = "abante"
	page_ctr = 1;

	start_urls = [
		'http://www.abante.com.ph/news/page/2',
	]

	def parse(self, response):
		item_urls = response.xpath("//div[@class='item-details']/h3[@class='entry-title td-module-title']//a/@href").extract()

		for url in item_urls:
			item_url = urlparse.urljoin(response.url, url)
			yield scrapy.Request(item_url,self.parseItem)

		next_page =  response.xpath("//div[@class='page-nav td-pb-padding-side']//a[.='']/@href").extract()[1]
		current = response.xpath("//div[@class='page-nav td-pb-padding-side']/span[@class='current']/text()").extract()
		if current is not "5":
		 	next_page = response.urljoin(next_page)
		 	yield scrapy.Request(next_page, self.parse)


	def parseItem(self, response):
		item = StreamerItem()
		item['title'] = response.xpath("//div[@class='td-post-header']/header[@class='td-post-title']//h1[@class='entry-title']/text()").extract()
		item['content'] = response.xpath("//div[@class='td-post-content']//p/text()").extract()
		item['category'] = 'National'
		yield item
