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



# Main declaration for console use
if __name__ == '__main__':
	# Domain to base requests off of
	URL = 'developer.google.com'

	# command line setup
	parser = argparse.ArgumentParser(description='Scrapes a sub directory of http://www.developer.google.com for IO codes')
	parser.add_argument('dir', help="The input website directory starting with '/'")
	arguments = parser.parse_args()

	# Find each question in the page
	for question in soup.find_all('a'):
		# Build links in a dictionary
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


