from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# go to login page
def got_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, '#login_link')
    login_link.click()


# checking that user can go to login page
def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    got_to_login_page(browser)


