from booking.booking import Booking

inst = Booking()
inst.land_first_page()
inst.select_currency(currency="USD")
# inst.select_language("ja")
inst.search_place(place="Tokyo")
inst.select_dates(check_in_date="2021-11-11",check_out_date="2021-11-23")
inst.select_guests(adult=5)
inst.click_search()
inst.set_lowest_price()