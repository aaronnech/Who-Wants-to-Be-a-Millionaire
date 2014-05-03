#!/usr/bin/env python
# Author: Aaron Nech
# Description: Scrapes a sub directory of http://www.indiabix.com
#  And extracts question and answers in json format.
 
import os, sys
import argparse
import requests
import json
from selenium import webdriver
from bs4 import BeautifulSoup
 
 
# Helper functions
def is_letter(s):
	""" Determines if a string is a simple multiple choice letter. (A, B, C, D)
		Returns true if this is the case, false otherwise """
	return s == 'A.' or s == 'B.' or s == 'C.' or s == 'D.'
 
def get_answer(s):
	"""Given a choice (A, B, C, D) this function returns the integer index representation
		of that choice (0, 1, 2, 3)"""
	return 'ABCD'.index(s)
 
# Main declaration for console use
if __name__ == '__main__':
	# Domain to base requests off of
	URL = 'www.indiabix.com'
 
	# command line setup
	parser = argparse.ArgumentParser(description='Scrapes a sub directory of http://www.indiabix.com for multiple choice questions')
	parser.add_argument('dir', help="The input website directory starting with '/'")
	arguments = parser.parse_args()
 
	# IndiaBix.com loads answers in with javascript, so you must render the page
	# in a browser engine first. Luckily selenium can do just this.
	browser = webdriver.Firefox()
	browser.get("http://" + URL + arguments.dir)
	soup = BeautifulSoup(browser.page_source)
 
	# Find each question in the page
	for question in soup.find_all('td', {'class' : 'bix-td-qtxt'}):
		# Build result dictionary
		result = {'question' : question.get_text()}
		result['content'] = []
 
		# Fill content array with answer choices 
		for answer in question.parent.parent.find_all('td', {'class' : 'bix-td-option'}):
			if not is_letter(answer.get_text()):
				result['content'].append(answer.get_text())
		# Scrape correct answer integer index for content array
		result['answer'] = get_answer(question.parent.parent.parent.parent.find_all('b', {'class' : 'jq-hdnakqb'})[0].get_text())
 
		# Dump result json to std. out. and output a comma.
		print json.dumps(result, sort_keys=True, indent=4, separators=(',', ': '))
		print ','