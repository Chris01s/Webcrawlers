#!/bin/python

from junk_classifiers.junk_classifier import DiscardJunk
from .content_class import Content
import os
import sys

class Crawler(Content, DiscardJunk):	
	def do_parsing(self):
		self.get_a_tags()
		self.get_paragraphs()
	
	def check_if_already_scraped(self):
		if self.href in self.scraped_hrefs:
			return True
		
	def print_results(self):
		self.scraped_hrefs = list()
		for element in self.a_tags:
			self.a_tag = element			
			self.get_article_title()
			self.get_href()
			self.check_if_website()
			self.check_if_external_link()
			self.is_junk = self.check_if_junk()
			if self.is_junk:
				continue
			else:
				self.combine_child_with_parent()
				if self.check_if_already_scraped():
					continue
				else:
					self.scraped_hrefs.append(self.href)
					print(self.article_title.strip().replace("	",""))
					print(self.href.strip(), end="\n")		
	
	
	def do_scrape(self):
		self.get_firefox_driver()
		self.start_driver()
		self.get_status_code()
		self.do_parsing()
		self.print_results()
		self.close_driver()
		
		
			
		
