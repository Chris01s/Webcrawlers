#!/bin/python

from .get_soup import GetSoup
from urllib.parse import urlparse
from .requests_class import RequestsException
import re 


class Content(GetSoup):		
	def get_title(self):
		try:
			self.title = self.soup.title.text.strip()
		except:
			try:
				self.title = self.soup.find("title").text.strip()
			except:	
				self.title = ""
	
	
	def get_a_tags(self):
		self.a_tags = self.soup.find_all("a")
		if not self.a_tags:
			print("Something went wrong: could not find a_tags")
			raise RequestsException("Something went wrong: could not find a_tags")
	
		
	def get_paragraphs(self):
		self.paragraphs = self.soup.find_all("p")
		if not self.paragraphs:
			print("Something went wrong: could not find a_tags")
			raise RequestsException("Something went wrong: could not find a_tags")
	
			

	def get_article_title(self):
		try:
			self.article_title = self.a_tag.attrs['title']
		except:
			self.article_title = self.a_tag.text
	
	
	def get_href(self):
		try:
			self.href = self.a_tag.attrs['href']
		except:
			self.href = ""
	
