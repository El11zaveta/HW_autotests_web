import time
from testpage import OperationsHelper, ContactPage
import yaml
import logging
from testpage import TestSearchLocators


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata['browser']


def test_field_login(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_successful_login(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    hello_text = testpage.find_element(TestSearchLocators.LOCATOR_HELLO_TEXT).text
    #testpage.find_element(TestSearchLocators.LOCATOR_MENU).click()
    #testpage.find_element(TestSearchLocators.LOCATOR_LOGOUT_BTN).click()
    assert f"Hello, {testdata['username']}" == hello_text


def test_create_post(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])
    testpage.click_login_button()
    testpage.click_create_button()
    testpage.enter_title(testdata['title'])
    testpage.enter_title(testdata['description'])
    testpage.enter_content(testdata['content'])
    testpage.click_save_button()
    post_title = testpage.find_element(TestSearchLocators.LOCATOR_POST_TITLE).text
    logging.info(f"We found text {post_title} on the page of the post")
    assert post_title == testdata['title']


def test_check_contact_us(browser):
    logging.info("Test4 Starting")
    login_page = OperationsHelper(browser)
    login_page.go_to_site()
    login_page.login(testdata['username'], testdata['password'])
    login_page.contact_btn()
    contact_page = ContactPage(browser, browser.current_url)
    contact_page.input_name(testdata['contact_name'])
    contact_page.input_email(testdata['contact_email'])
    contact_page.input_content(testdata['contact_content'])
    contact_page.submit_form()
    time.sleep(2)
    text = contact_page.get_text_from_alert()
    assert text == 'Form successfully submitted'