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
from selenium.webdriver.common.by import By
import time
import Conf_File.Locators_File as locators

driver = webdriver.Chrome()

#get the url which it will navigate
driver.get("https://weathershopper.pythonanywhere.com/")

#maximize the window
driver.maximize_window()

#Assigning all the locators in Locators_File
Temperature_text = locators.Temperature_text
Buy_moisturizers = locators.Buy_moisturizers
Price_of_items = locators.Price_of_items
Buy_sunscreens = locators.Buy_sunscreens
Least_Priced = locators.Least_Priced
Add_cart = locators.Add_cart
Make_payment = locators.Make_payment


#Check the temperature .
temperature_text = driver.find_element(By.XPATH,Temperature_text)
temperature = int((temperature_text.text)[0:2])
print("The temperature is:", temperature, "°C")

def get_minimum_price():

    product_price = []
    Least_items = 500

    #Select the minimum product price
    for item in products:
        print(item)
        item = int((item.text)[-3::])
        product_price.append(item)
    print("product price of all the items:", product_price)
    Minimum_price = int(min(product_price))
    print("The minimum price is:", Minimum_price)
    Least_items = driver.find_element(By.XPATH, Least_Priced%Minimum_price).click()

if  temperature <= 23:
    time.sleep(2)
    driver.find_element(By.XPATH, Buy_moisturizers).click()
    products = driver.find_elements((By.XPATH, Price_of_items))

#Click on sunscreen option
elif temperature >= 24:
    time.sleep(2)
    driver.find_element(By.XPATH,Buy_sunscreens).click()
    products = driver.find_element((By.XPATH , Price_of_items))

get_minimum_price()

#Adding the product in the cart by clicking the cart button

Adding_the_product = driver.find_element(By.XPATH, Add_cart).click()

time.sleep(2)

#Pays for the product by clicking the pay button

Payment=driver.find_element(By.XPATH,Make_payment).click()

time.sleep(3)

# Close the browser
driver.close()