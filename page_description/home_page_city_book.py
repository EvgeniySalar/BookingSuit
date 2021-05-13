from base_page import BasePage
from locators_city_book import MainPageLocatorsSc2


class HomePageScr(BasePage):

    def city_field_element_click(self):
        city_field = self.get_element_present(*MainPageLocatorsSc2.CITY_FIELD)
        city_field.click()

    def city_popup_elements(self):
        city_popup = self.get_element_present(*MainPageLocatorsSc2.VISIBLE_CITY_FIELD)
        return city_popup

    def city_list_elements(self):
        city_list = self.get_element_present(*MainPageLocatorsSc2.CITY_CHOOSE)
        city_list.click()
        return city_list

    def calendar_field_out(self):
        calendar_field = self.get_element_present(*MainPageLocatorsSc2.CALENDAR_FIELD_CHECKOUT)
        calendar_field.click()
        return calendar_field

    def calendar_field(self):
        calendar_field_o = self.get_element_present(*MainPageLocatorsSc2.CALENDAR_FIELD_CHECKIN)
        calendar_field_o.click()
        return calendar_field_o

    def calendar_today_data(self):
        calendar_today = self.get_element_present(*MainPageLocatorsSc2.TODAY_CALENDAR_DATA)
        calendar_today.click()
        return calendar_today

    def calendar_next_day_data(self):
        calendar_next = self.get_element_present(*MainPageLocatorsSc2.ANY_DAY)
        calendar_next.click()
        return calendar_next

    def search_button_selection(self):
        search_button = self.get_element_present(*MainPageLocatorsSc2.SEARCH_BUTTON)
        search_button.click()
        return search_button

    def open_next_page(self):
        open_next = self.get_element_present(*MainPageLocatorsSc2.NEXT_PAGE_INDICATOR)
        return open_next

    def calendar_popup_next_page_elements(self):
        calendar_popup = self.get_element_present(*MainPageLocatorsSc2.CALENDAR_FIELD_NEXT_PAGE)
        return calendar_popup

