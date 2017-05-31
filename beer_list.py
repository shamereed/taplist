from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import re, requests, smtplib, json

##################################################################################

def send_email(msg):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxec1254f2c19c40a2a160cffb18bb1886.mailgun.org/messages",
        auth=("api", "key-e5dc1ad3337539060a5624c71821f434"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxec1254f2c19c40a2a160cffb18bb1886.mailgun.org>",
              "to": "Shane <shanem.reed@gmail.com>",
              "subject": "PHILLY TAP LIST",
              "text": msg})

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

  def strip_list(bar_name, beers):
	clean_beers = []
	for beer in beers:
		if beer.text.startswith(".") or beer.text.startswith(" "):
			continue
		name = (beer.text.strip()).upper().encode('ascii', 'ignore')
		clean_beers.append(name)
		print name
	return clean_beers
  
def strip_list_to_file(bar_name, beers):
	fp = open('tap_list.txt', 'a')
	fp.write(bar_name.upper() + ':\n')
	clean_beers = []
	for beer in beers:
		if beer.text.startswith(".") or beer.text.startswith(" "):
			continue
		name = (beer.text.strip()).upper().encode('ascii', 'ignore')
		clean_beers.append(name)
		print name
		fp.write(name + '\n')
	fp.write('\n')
	fp.close()
	return clean_beers
	
def replaceSpace(str_):
	return str_.replace(' ', '-').lower()
	
def ascii_encode(str_):
    return str_.encode('ascii', 'ignore')

def get_all_bars():
	req = requests.get('http://www.phillytapfinder.com/bars')
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('div', {"class": "results-grid tall-results"})
	found_items = _list.find_all('a')
	return strip_list('Bars', found_items)

def get_hoods():
	req = requests.get('http://www.phillytapfinder.com/hoods')
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('div', {"class": "results-grid"})
	found_items = _list.find_all('a')
	return strip_list('Hoods', found_items)

def get_bars_in_hood(hood):
	create_request('hood', hood)

def get_philltapfinder_list(bar_name):
	create_request('bar', bar_name)
	
def create_request(prefix, suffix):
	print suffix.upper() + ':\n'
	suffix = replaceSpace(suffix)
	req = requests.get('http://www.phillytapfinder.com/' + prefix + '/' + suffix)
	soup = BeautifulSoup(req.text, "html.parser")
	_list = soup.find('ul', {"class": "grid-list clearfix"})
	found_items = _list.find_all('h4')
	return strip_list(suffix, found_items)
	print "\n"

# PHILLY
##################################################################################

#NORTH 3RD
def get_north_3rd_list():
    get_philltapfinder_list('north 3rd')

#STANDARD TAP
def get_standard_tap_list():
    get_philltapfinder_list('standard tap')

#JOHNNY BRENDA'S
def get_johnny_brendas_list():
    get_philltapfinder_list('johnny brenda\'s')

#KRAFTWORK
def get_kraftwork_list():
    get_philltapfinder_list('kraftwork')	
	
#VARGA BAR
def get_varga_bar_list():
    get_philltapfinder_list('varga bar')		
	
#RACE STREET CAFE
def get_race_street_cafe_list():
    get_philltapfinder_list('race street')
	
#AMERICAN SARDINE BAR
def get_american_sardine_bar_list():
    get_philltapfinder_list('american sardine bar')
	
#KHYBER PASS PUB
def get_khyber_pass_pub_bar_list():
	get_philltapfinder_list('khyber pass pub')

##################################################################################

