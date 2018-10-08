import beer_list

#NORTH 3RD
def get_north_3rd_list():
    beer_list.get_tap_list('north 3rd')

#STANDARD TAP
def get_standard_tap_list():
    beer_list.get_tap_list('standard tap')

#JOHNNY BRENDA'S
def get_johnny_brendas_list():
    beer_list.get_tap_list('johnny brenda\'s')

#KRAFTWORK
def get_kraftwork_list():
    beer_list.get_tap_list('kraftwork')	
	
#VARGA BAR
def get_varga_bar_list():
    beer_list.get_tap_list('varga bar')		
	
#RACE STREET CAFE
def get_race_street_cafe_list():
    beer_list.get_tap_list('race street')
	
#AMERICAN SARDINE BAR
def get_american_sardine_bar_list():
    beer_list.get_tap_list('american sardine bar')
	
#KHYBER PASS PUB
def get_khyber_pass_pub_bar_list():
	beer_list.get_tap_list('khyber pass pub')

def get_tap_list():
	
	fp = open('tap_list.txt', 'w').close()
	
	fp = open('tap_list.txt', 'r+')
	
	beer_list.get_standard_tap_list()
	
	beer_list.get_race_street_cafe_list()
	
	beer_list.get_johnny_brendas_list()
	
	beer_list.get_north_3rd_list()
	
	beer_list.get_kraftwork_list()
	
	beer_list.get_varga_bar_list()
	
	beer_list.get_american_sardine_bar_list()
	
	beer_list.get_khyber_pass_pub_bar_list()
	
	msg = fp.read()
	
	fp.close()
	
	#beer_list.send_email(msg)
	return msg