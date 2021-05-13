from selenium.webdriver.common.by import By

from helpers.helpers import add_some_day


class MainPageLocatorsSc2:
    CITY_FIELD = (By.XPATH, '//input[@id="ss"]')
    CITY_CHOOSE = (By.XPATH, "//li[@data-label='Kiev']")

    CALENDAR_FIELD_CHECKOUT = (By.XPATH, "//div[(@data-mode='checkout')]")
    CALENDAR_FIELD_CHECKIN = (By.XPATH, "//div[(@data-mode='checkin')]")
    TODAY_CALENDAR_DATA = (By.XPATH, "//td[contains(@class,'bui-calendar__date bui-calendar__date--today')]")
    ANY_DAY = (By.XPATH, f'//td[contains(@data-date,"{add_some_day()}")]')
    NEXT_PAGE_INDICATOR = (By.XPATH, "//button[contains(@class,'show_map entry-point__map_small')]")

    VISIBLE_CITY_FIELD = (By.XPATH, "//ul[@aria-label='List of suggested destinations ']")

    DATA_CALENDAR_FIELD_2 = (By.CLASS_NAME, "bui-calendar__date bui-calendar__date--selected")

    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class,'sb-searchbox__button')]")

    CALENDAR_FIELD_NEXT_PAGE = (By.XPATH, "//div[@class='bui-calendar__main b-a11y-calendar-contrasts']")
