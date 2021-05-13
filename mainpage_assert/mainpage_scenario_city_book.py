from page_description.home_page_city_book import HomePageScr
from locators_1.locators_city_book import MainPageLocatorsSc2


class MainPagescr(HomePageScr):

    def citys_field_is_clicked(self):
        assert self.city_popup_elements().is_enabled(), "Field is not clicked"
        print("Field is clicked")

    def city_is_chosen(self):
        assert self.city_list_elements().is_enabled(), "City name is not selected"
        print("City name is  selected")

    def open_the_next_page(self):
        assert self.open_next_page().is_displayed(), "Page is not opened"
        print("Page is opened")

    def calendar_day_today_check(self):
        assert self.calendar_popup_next_page_elements().is_displayed(), "Calendar day today is not displayed"
        print("Calendar day today is displayed")

    def calendar_next_day_check(self):
        assert self.calendar_popup_next_page_elements().is_displayed(), "Calendar nex day is not displayed"
        print("Calendar nex day is displayed")

    def search_button_check(self):
        assert self.search_button_selection().is_enabled(), "Search button is not clicked"
        print("Search button is clicked")

    def go_next_step(self):
        assert self.get_element_present(*MainPageLocatorsSc2.SEARCH_BUTTON), "Search button is not clicked"
        print("Search button is clicked")
