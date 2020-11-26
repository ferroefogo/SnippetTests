# Scrape scrap.tf and join all raffles.

# trying to implement method of filtering out raffles that I have already joined.
import browser

def enterRaffle():
    wishlistMode = input('enter N: ')
    if wishlistMode == 'N':
        i=1
        while i in range(0,128):
                back_to_main_page = browser.get('https://scrap.tf/raffles/ending')
                type(back_to_main_page)

                raffleName = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div[3]/div[1]/div['+str(i)+']/div[1]/div[1]/a')
                type(raffleName)
                raffleName.click()

                browser.execute_script("window.scrollTo(0, 300)") 

                time.sleep(3)
                
                enterElem = browser.find_element_by_id('raffle-enter')
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
    browser.get('https://scrap.tf/raffles/ending')
    raffle = enterRaffle()


if __name__ == "__main__":
    main()
