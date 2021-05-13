import pytest
from selenium import webdriver
# from prestashop.url_contains.data_prestashop_url import MAIN_PAGE_URL as m
# print(m)
# from prestashop.url_contains.data_prestashop_url import MAIN_PAGE_URL as main_page_url
# print(main_page_url)
# from dataurl import MAIN_PAGE_URL
MAIN_PAGE_URL = "https://www.booking.com/index.html?label=" \
                "gen173nr-1DCAEoggI46AdIM1gEaOkBiAEBmAEhuAEXyAEM2AED6AEBiAIBqAIDuALh7-" \
                "uCBsACAdICJGYxZDgxZThiLTZjZDQtNDk1Mi05ZDcwLWQwN2Q4OTZjODA3NtgCBOACAQ&sid=" \
                "28deaec43840af3789c593babab79aa1&lang=en-us&sb_price_type=total&soz=" \
                "1&lang_click=other;cdl=ru;lang_changed=1"


@pytest.fixture(scope="session")
def chrome_drv(request):
    print("\nstart chrome browser for test..")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(MAIN_PAGE_URL)
    yield driver
    print("\nquit browser..")
    driver.quit()
    return driver

    # def resource_teardown():
    #     print("module teardown")
    #     print("\nquit browser..")
    #     driver.quit()
    #     request.addfinalizer(resource_teardown)
    #     return driver

# yield driver
#     print("\nquit browser..")
#     driver.quit()
#     return driver





