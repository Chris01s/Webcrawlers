#!/bin/python

from urllib.parse import urlparse

class DiscardJunk:
	def check_if_website(self):
		child_url_parsed = urlparse(self.href)
		if child_url_parsed.scheme:
			self.is_website = True
		elif child_url_parsed.netloc:
			self.is_website = True
		else:
			self.is_website = False
	
	
	def check_if_external_link(self):
		base_url_parsed = urlparse(self.url)
		child_url_parsed = urlparse(self.href)
		if self.is_website:
			if base_url_parsed.netloc in child_url_parsed.netloc:
				self.is_external = False
			else:
				self.is_external = True
		else:
			self.is_external = False
			
			
	def check_if_junk(self):
		if len(self.article_title.strip().split(" ")) < 6:
			return True
		elif not self.href:
			return True
		elif self.is_external:
			return True
		else:
			return False
	
	
	def combine_child_with_parent(self):
		if not self.is_junk:
			if not self.is_website:
				base_url_parsed = urlparse(self.url)
				child_url_parsed = urlparse(self.href)		
				self.href = base_url_parsed.scheme+"://"+base_url_parsed.netloc+child_url_parsed.path
	
