# Make program to scrape through JD and find discounts on jordans.
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
        type(registerElem)
        registerElem.click()

        # Finds Field Element and Fills it in.
        fNameElem = browser.find_element_by_id('firstName')  # Field Name Finder
        type(fNameElem)
        fNameElem.send_keys('Marco')  # Fills in the Field with 'Marco'

        surnameElem = browser.find_element_by_id('lastName')
        type(surnameElem)
        surnameElem.send_keys('Fernandes')

        emailElem = browser.find_element_by_id('username')
        type(emailElem)
        emailElem.send_keys('marcoff2002@gmail.com')

        telephoneElem = browser.find_element_by_id('phone')
        type(telephoneElem)
        telephoneElem.send_keys('7888981342')

        passwordElem = browser.find_element_by_id('password')
        type(passwordElem)
        passwordElem.send_keys('HR29sdQC.Aq/KNg')

        confirm_passwordElem = browser.find_element_by_id('confirmPassword')
        type(confirm_passwordElem)
        confirm_passwordElem.send_keys('HR29sdQC.Aq/KNg')

        countryElem = Select(browser.find_element_by_id('country'))
        type(countryElem)
        countryElem.select_by_visible_text('United Kingdom (excluding Channel Islands)')

        manualAddressElem = browser.find_element_by_id('showAutoCompletables')
        type(manualAddressElem)
        manualAddressElem.click()

        postcodeElem = browser.find_element_by_id('postcode')
        type(postcodeElem)
        postcodeElem.send_keys('RH11 8UG')

        address1Elem = browser.find_element_by_id('address1')
        type(address1Elem)
        address1Elem.send_keys('2, Wiston Court')

        address2Elem = browser.find_element_by_id('address2')
        type(address2Elem)
        address2Elem.send_keys('Cuckfield Close')

        townElem = browser.find_element_by_id('town')
        type(townElem)
        townElem.send_keys('Crawley')

        countyElem = browser.find_element_by_id('billingCountyInp')
        type(countyElem)
        countyElem.send_keys('West Sussex')

        # Press Register Button
        registerButtonElem = browser.find_element_by_class('btn btn-level1 large')
        type(registerButtonElem)
        registerButtonElem.click()
    else:
        loginElem = browser.find_element_by_id('username')
        type(loginElem)
        loginElem.send_keys('marcoff2002@gmail.com')

        passElem = browser.find_element_by_id('password')
        type(passElem)
        passElem.send_keys('HR29sdQC.Aq/KNg')

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
