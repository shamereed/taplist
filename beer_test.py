import beer_list

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