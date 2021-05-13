import pytest
import sys
sys.path.append("C:/Users/Zhenya_PC/PycharmProjects/BookingSuit/page_description/home_page_city_book")

from page_description.home_page_city_book import HomePageScr
from mainpage_scenario_city_book import MainPagescr




class TestSiteFuncScr:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, chrome_drv):
        self.home_page = HomePageScr(chrome_drv)
        self.main_page = MainPagescr(chrome_drv)
        yield chrome_drv

    def test_click_on_city_field(self):
        self.home_page.city_field_element_click()
        self.home_page.city_list_elements()
        self.main_page.citys_field_is_clicked()

    def test_search_button_click(self):
        self.home_page.search_button_selection()
        self.main_page.open_the_next_page()

    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.s
    # @pytest.mark.xfail
    def test_calendar_field(self):
        # self.pages.calendar_field()
        self.main_page.calendar_day_today_check()
        self.home_page.calendar_today_data()
        self.home_page.calendar_field_out()
        self.main_page.calendar_next_day_check()
        self.home_page.calendar_next_day_data()
        self.home_page.search_button_selection()
        self.main_page.go_next_step()



