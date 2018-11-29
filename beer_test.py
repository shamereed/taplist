import tapfinder

# print("\nList of Hoods")
tapfinder.get_hoods()

hood = raw_input("Enter hood name: ")
tapfinder.get_bars_in_hood(hood)

bar = raw_input("Enter bar name: ")
tapfinder.get_tap_list(bar)

tapfinder.get_all_styles()

tapfinder.get_bar_details(bar)

tapfinder.get_all_bars()

tapfinder.get_breweries()

brewery = raw_input("Enter brewery name: ")
tapfinder.get_brewery_details(brewery)
