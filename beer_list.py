from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import re, requests, json, sqlite_connect, util

PHILLYTAPFINDER = 'http://www.phillytapfinder.com/'


def get_all_bars():
	req = requests.get(PHILLYTAPFINDER + 'bars')
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find_all('div', {"class": "results-grid tall-results"})
	found_items = _list[1].find_all('a')
	return util.strip_html_list(found_items)

def get_hoods():
	req = requests.get(PHILLYTAPFINDER + 'hoods')
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('div', {"class": "results-grid"})
	found_items = _list.find_all('a')
	return util.strip_html_list(found_items)

def get_breweries():
	req = requests.get(PHILLYTAPFINDER + 'on-tap')
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('div', {"class": "results-grid"})
	found_items = _list.find_all('a')
	return util.strip_html_list(found_items)
	
def get_brewery_details(brewery):
	req = requests.get(PHILLYTAPFINDER + 'brewery/' + util.replaceSpace(brewery))
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('ul', {"class": "the-tap-list"})
	found_items = _list.find_all('h3')
	return util.strip_html_list(found_items)	

def get_bar_details(bar_name):
	req = requests.get(PHILLYTAPFINDER + 'bar/' + util.replaceSpace(bar_name))
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('div', {"class": "bar-data"})
	found_items = _list.find_all('p')
	print (found_items.text.strip()).upper().encode('ascii', 'ignore')
	return found_items
	
def get_all_styles():	
	req = requests.get(PHILLYTAPFINDER + 'styles')
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('div', {"class": "results-grid"})
	found_items = _list.find_all('li')
	return util.strip_html_list(found_items)
	print "\n"
	
def get_bars_in_hood(hood):
	create_request('hood', hood)

def get_tap_list(bar_name):
	create_request('bar', bar_name)
	
def get_beer(beer):
	soup = create_base_request('beer', beer)
	_list = soup.find('span', {"class": "origin"})
	found_items = _list.find_all('a')
	return util.strip_html_list(found_items)
	print "\n"
	
def create_request(prefix, suffix):
	soup = create_base_request(prefix, suffix)
	_list = soup.find('ul', {"class": "grid-list clearfix"})
	found_items = _list.find_all('h4')
	return util.strip_html_list(found_items)
	print "\n"
	
def create_base_request(prefix, suffix):
	print suffix.upper() + ':\n'
	suffix = util.replaceSpace(suffix)
	req = requests.get(PHILLYTAPFINDER + prefix + '/' + suffix)
	soup = BeautifulSoup(req.text, "html.parser")
	return soup