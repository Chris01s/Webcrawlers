#!/bin/python

from bs4 import BeautifulSoup
from .requests_class import GetRequests
from .requests_class import RequestsException

class GetSoup(GetRequests):	
	def get_markup(self):
		if self.status_code == 200:
			self.markup = self.response.text
		else:
			print("Something went wrong", self.status_code)
			raise RequestsException("Something went wrong", self.status_code)
			
	def get_soup(self):
		self.soup = BeautifulSoup(
			markup = self.markup,
			features = "lxml"
		)
		
		
		


