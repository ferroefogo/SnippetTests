import browser
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
      
    
def enterGiveaway():
    print("---STEAMGIFTS AUTO ENTRY SCRIPT---")
    #balance = browser.find_element_by_class_name('nav__points')
    #balanceReal = balance.text
    
    #print("Balance: ",balanceReal,'Points')
    
    print("Would you like to enter a ticket for your wishlist games? (Y/N) ")
    wishlistMode = input('')
    if wishlistMode == 'Y':
        browser.get('https://www.steamgifts.com/giveaways/search?type=wishlist')
        i=1
        while i in range(0,i+1):
            back_to_main_page = browser.get('https://www.steamgifts.com/giveaways/search?type=wishlist')
            type(back_to_main_page)
            
            giftName = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[3]/div['+str(i)+']/div/div/h2/a[1]')
            type(giftName)
            giftName.click()
            
            enterElem = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/form/div[1]')
            type(enterElem)
            enterElem.click()
            i+=1
    else:
        
        top2=True
        if top2 == False:
            # Clicks the top Main secluded element
            #...
            mainElem = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div[1]/a")
            type(mainElem)
            mainElem.click()
            
            enterElem1 = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/h2/a[1]")
            type(enterElem1)
            enterElem1.click()
            
            # Clicks the top two secluded elements
            topEl = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/h2/a[1]")
            type(topEl)
            topEl.click()

            enterElem2 = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/h2/a[1]")
            type(enterElem2)
            enterElem2.click()
            
            browser.get("https://www.steamgifts.com/")
            
            botEl = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div[1]/div[2]/div/div/h2/a[1]")
            type(botEl)
            botEl.click()

            enterElem3 = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/h2/a[1]")
            type(enterElem3)
            enterElem3.click()

            browser.get("https://www.steamgifts.com/")
            
        i=1
        while i in range(0,50):
            back_to_main_page = browser.get('https://www.steamgifts.com/')
            type(back_to_main_page)
            
            giftName = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[3]/div['+str(i)+']/div/div/h2/a[1]')
            type(giftName)
            giftName.click()
            
            enterElem = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/form/div[1]')
            type(enterElem)
            enterElem.click()
            i+=1
            
    

def main():
    global browser
    from selenium import webdriver
    from selenium.webdriver.firefox.webdriver import FirefoxProfile

    profile = FirefoxProfile(r'C:\Users\marco\AppData\Roaming\Mozilla\Firefox\Profiles\aiof54fb.default-release')
    browser = webdriver.Firefox(profile)
    type(browser)
    browser.get('https://www.steamgifts.com/')
    EntryTicket = enterGiveaway()
    
if __name__=="__main__":
    main()




