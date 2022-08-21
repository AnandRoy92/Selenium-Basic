''' Write an Automation Script to do these following Steps.

Based on temperature navigate to appropriate link. Select a least proceed item and add to cart. Go to cart and confirm your item is added.
Detailed steps

* Reading a text value (temperature).
* Click on a button based on temperature.
* Read the price of all elements.
* Click the add button for least price item.
* Click on Cart.
* Confirm the cart item is filled with price. '''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import configparser

#launch the webdriver from selenium
serv_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")

driver = webdriver.Chrome(service = serv_obj)

#get the url which it will navigate
driver.get("https://weathershopper.pythonanywhere.com/")
driver.maximize_window()

def check_temperature():

    #Locate the temperature button and perform click action.
    temperature_txt = driver.find_element(By.XPATH,"//span[@id='temperature']")
    print(temperature_txt.text)

def compare_temperature(temperature_txt):
    config_Weather_Shopper = configparser.ConfigParser()
    config_Weather_Shopper.read("Config.ini")
    #Click on moisturizer option
    x = config_Weather_Shopper["Temperature_Below_23°C"]
    buy_moisturizers = int(x["buy_moisturizers"])

    y = config_Weather_Shopper["Temperature_Above_30°C"]
    buy_sunscreens = int(y["buy_sunscreens"])

    if temperature_txt.text == buy_moisturizers:
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[contains(text(),'Buy moisturizers')]").click()
        products = driver.find_element((By.XPATH,"//p[contains(text(),'Price')]"))
        product_price = []
        Least_items = 500

    #Select the minimum product price
        for item in product_price:
            print(item)
            item = int((item.text)[-3::])
            product_price.append(item)
        print(product_price)
        Minimum_price = min(product_price)
        print(Minimum_price)


        Least_items = driver.find_element(By.XPATH,"//p[contains(text(),'product_price')]/following-sibling::button[@class='btn btn-primary']").click()
        return products, product_price, Least_items

    #Click on suncreen option
    elif temperature_txt.text == buy_sunscreens:
        time.sleep(2)
        driver.find_element(By.XPATH,"//button[contains(text(),'Buy sunscreens')]").click()
        products = driver.find_element((By.XPATH,"//p[contains(text(),'Price')]"))
        product_price = []
        Least_items = 500

        for item in product_price:
            print(item)
            item = int((item.text)[-3::])
            product_price.append(item)
        print(product_price)
        Minimum_price = min(product_price)
        print(Minimum_price)

        Least_items = driver.find_element(By.XPATH, "//p[contains(starts-with(),'product_price')]/following-sibling::button[@class='btn btn-primary']").click()
        return products, product_price, Least_items

def Adding_the_product():
    #Adding the product in the cart by clicling the cart button

    Adding_the_product = driver.find_element(By.XPATH, "//button[@class='thin-text nav-link']").click()
    return Adding_the_product

time.sleep(2)

def Payment_of_the_product():
    #Pays for the product by clicking the pay button
    #normalize space() = The element has spaces in its text or in the value of any attribute.

    Payment=driver.find_element(By.XPATH,"//span[normalize-space()='Pay with Card']").click()
    return Payment

time.sleep(3)

if __name__=="__main__":
    temperature_txt = check_temperature()
    The_least_priced = compare_temperature(temperature_txt)


# Close the browser
driver.close()

