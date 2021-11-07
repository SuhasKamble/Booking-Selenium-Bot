from selenium import webdriver
import os

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:/SeleniumDrivers"):
        self.driver_path  = driver_path
        os.environ['PATH'] = self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def land_first_page(self):
        self.get()


    def select_currency(self, currency=None):
        selected_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        selected_element.click()

        selected_currecy_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currecy_element.click()

    def select_language(self, lang=None):
        selected_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your language"]'
        )    
        selected_element.click()
        
        selected_lang_element = self.find_element_by_css_selector(
            f'a[data-lang="{lang}"]'
        )
        selected_lang_element.click()

    def search_place(self, place):
        search_field = self.find_element_by_id("ss")
        search_field.clear()
        search_field.send_keys(place)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        ) 
        first_result.click()
    
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_guests(self, adult=1):
        selected_element = self.find_element_by_id("xp__guests__toggle")
        selected_element.click()

        while True:
            decrease_adult_btn = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )  
            decrease_adult_btn.click()

            value_count_element = self.find_element_by_id("group_adults")
            value_count = value_count_element.get_attribute("value")
           
            if int(value_count) == 1:
                break

        increase_adult_btn = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for i in range(adult - 1):
            increase_adult_btn.click()
    
        

    def click_search(self):
        submit_btn = self.find_element_by_css_selector(
            'button[type="submit"]'
        )        
        submit_btn.click()
        
        
    def set_lowest_price(self):
        selected_element = self.find_element_by_css_selector(
            'a[data-type="price"]'
        )
        selected_element.click()
        
    
        
            