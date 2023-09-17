import allure
from selene import browser


@allure.title("Successful fill form")
def test_registration_page(setup_browser):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')
