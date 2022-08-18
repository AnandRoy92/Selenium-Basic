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

#launch the webdriver from selenium
serv_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")

driver = webdriver.Chrome(service = serv_obj)

#get the url which it will navigate
driver.get("https://weathershopper.pythonanywhere.com/")
driver.maximize_window()

#Locate the temperature button and perform click action.
temperature_txt= driver.find_element(By.XPATH,"//span[@id='temperature']")
print(temperature_txt.text)

#Click on moisturizer option
if temperature_txt.text <= ('23°C'):
    time.sleep(2)
    driver.find_element(By.XPATH,"//button[contains(text(),'Buy moisturizers')]").click()
    Products = driver.find_element((By.XPATH,"//p[contains(text(),'Price')]"))
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


    Least_items = driver.find_element(By.XPATH,"//p[contains(start-with(),'product_price')]/following-sibling::button[@class='btn btn-primary']").click()

#Click on suncreen option
elif temperature_txt.text >= ('30°C'):
    time.sleep(2)
    driver.find_element(By.XPATH,"//p[contains(text(),'Buy sunscreens')]").click()
    Products = driver.find_element((By.XPATH,"//p[contains(text(),'Price')]"))
    product_price = []
    Least_items = 500

    for item in product_price:
        print(item)
        item = int((item.text)[-3::])
        product_price.append(item)
    print(product_price)
    Minimum_price = min(product_price)
    print(Minimum_price)
#
    Least_items = driver.find_element(By.XPATH, "//p[contains(starts-with(),'product_price')]/following-sibling::button[@class='btn btn-primary']").click()

#Adding the product in the cart by clicling the cart button
driver.find_element(By.XPATH, "//button[@class='thin-text nav-link']").click()

time.sleep(2)

#Pays for the product by clicking the pay button
#normalize space() = The element has spaces in its text or in the value of any attribute.

button=driver.find_element(By.XPATH,"//span[normalize-space()='Pay with Card']").click()


time.sleep(3)

# Close the browser
driver.close()






