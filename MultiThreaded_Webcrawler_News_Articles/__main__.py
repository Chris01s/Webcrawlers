#!/bin/python


from requests_classes.requests_class import RequestsException
from requests_classes.scraper_class import Crawler as RequestsCrawler
from selenium_classes.scraper_class import Crawler as SeleniumCrawler
import threading
import time


def request_scrape_thread(url, exceptioned_urls):
	print("Entering {} Thread".format(url))
	try:
		scraper_obj = RequestsCrawler(url, add_proxies=True)	
		scraper_obj.do_scrape()
	except RequestsException as reqex:
		print("Something went wrong", reqex.__str__())
		print("Killing spider thread...")
		exceptioned_urls.append(url)
	print("Exiting {} Thread".format(url))


def selenium_scrape_thread(url):
	print("Entering {} Thread".format(url))
	try:
		scraper_obj = SeleniumCrawler(url, add_proxies=True)	
		scraper_obj.do_scrape()
	except Exception as ex:
		print("Something went wrong", ex.__str__())
		print("Killing spider thread...")
		scraper_obj.close_driver()
	print("Exiting {} Thread".format(url))
	


if __name__ == '__main__':

	threads = list()
	exceptioned_urls = list()
	
	with open("urls.txt", "r") as FILE:
		base_urls = FILE.readlines()
	
	for base_url in base_urls:
		base_url = base_url.strip()
		thread = threading.Thread(
			target = request_scrape_thread,
			args = (base_url, exceptioned_urls)
		)
		threads.append(thread)
		thread.start()
		
	for thread in threads:
		thread.join()
		
		
	print("list of exceptioned urls:{}".format(exceptioned_urls))
	time.sleep(2)
	threads = list()
	for base_url in exceptioned_urls:
		base_url = base_url.strip()
		thread = threading.Thread(
			target = selenium_scrape_thread,
			args = (base_url,)
		)
		thread.start()
		threads.append(thread)
		
	for thread in threads:
		thread.join()



