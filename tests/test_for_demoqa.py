from selene import browser



def test_registration_page():
    # GIVEN

    browser.open('https://demoqa.com/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')


