# Make program to scrape through JD and find jordans of x size
# Include creation of account and log in.
import webbrowser
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select


def fillRegister():
    alreadyRegistered = True
    while alreadyRegistered == False:
        # Finds register button on page
        registerElem = browser.find_element_by_id('')
        registerElem.click()

        # Finds Field Element and Fills it in.
        fNameElem = browser.find_element_by_id('firstName')  # Field Name Finder
        fNameElem.send_keys('First Name Here')

        surnameElem = browser.find_element_by_id('lastName')
        surnameElem.send_keys('Surname Here')

        emailElem = browser.find_element_by_id('username')
        emailElem.send_keys('email address here')

        telephoneElem = browser.find_element_by_id('phone')
        telephoneElem.send_keys('phone number here')

        passwordElem = browser.find_element_by_id('password')
        passwordElem.send_keys('password')

        confirm_passwordElem = browser.find_element_by_id('confirmPassword')
        confirm_passwordElem.send_keys('confirm password')

        countryElem = Select(browser.find_element_by_id('country'))
        countryElem.select_by_visible_text('country here')

        manualAddressElem = browser.find_element_by_id('showAutoCompletables')
        manualAddressElem.click()

        postcodeElem = browser.find_element_by_id('postcode')
        postcodeElem.send_keys('postcode')

        address1Elem = browser.find_element_by_id('address1')
        address1Elem.send_keys('address1')

        address2Elem = browser.find_element_by_id('address2')
        address2Elem.send_keys('address2')

        townElem = browser.find_element_by_id('town')
        townElem.send_keys('town')

        countyElem = browser.find_element_by_id('billingCountyInp')
        countyElem.send_keys('county')

        # Press Register Button
        registerButtonElem = browser.find_element_by_class('btn btn-level1 large')
        registerButtonElem.click()
    else:
        loginElem = browser.find_element_by_id('username')
        loginElem.send_keys('username')

        passElem = browser.find_element_by_id('password')
        passElem.send_keys('password')

        # Click the Sign In Button
        signInElem = browser.find_element_by_id('doLogin')
        signInElem.click()


def jordans():
    # Go straight to Men's Footwear Jordans, Size = 8.5, Under £150
    browser.get(
        'https://www.jdsports.co.uk/men/mens-footwear/size/8-5,8-5-11/?q=Jordans&minprice-gbp=60&maxprice-gbp=150')


def main():
    global browser
    browser = webdriver.Firefox()
    type(browser)
    browser.get('https://www.jdsports.co.uk/myaccount/dashboard/')
    registration = fillRegister()
    findJordans = jordans()


if __name__ == "__main__":
    main()
