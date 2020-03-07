#!/bin/python

from .selenium_class import GetSelenium, SeleniumException
from urllib.parse import urlparse
import re 


class Content(GetSelenium):		
	def get_title(self):
		try:
			self.title = self.driver.find_element_by_tag_name("title")
			if not self.title:
				self.title = self.driver.find_element_by_tag_name("h1")	
		except:
			self.title = ""
	
	
	def get_a_tags(self):
		self.a_tags = self.driver.find_elements_by_tag_name("a")
		if not self.a_tags:
			print("Something went wrong: could not find a_tags")
			raise SeleniumException("Something went wrong: could not find a_tags")
	
	
	def get_paragraphs(self):
		self.paragraphs = self.driver.find_elements_by_tag_name("p")
		if not self.paragraphs:
			print("Something went wrong: could not find a_tags")
			raise SeleniumException("Something went wrong: could not find a_tags")
			

	def get_article_title(self):
		try:
			self.article_title = self.a_tag.attrs['title']
		except:
			self.article_title = self.a_tag.text
	
	
	def get_href(self):
		try:
			self.href = self.a_tag.get_attribute("href")
		except:
			try:
				self.href = self.a_tag.attrs['href']
			except:
				self.href = ""
	
