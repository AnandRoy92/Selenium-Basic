#Test Case
#..................
#1) Open wen browser
#2) Open Url https://qxf2services.atlassian.net/jira/your-work
#3) Enter Username
#4) Enter password
#5) Click on login
#6) Capture title of the home page
#7) Verify title of the page: Facebook Account (Expected)
#8) Close Browser
#Selenium 4.X
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver\chromedriver.exe")

driver = webdriver.Chrome(service = serv_obj)

driver.get("https://id.atlassian.com/login?continue=https%3A%2F%2Fqxf2services.atlassian.net&prompt=login")
driver.maximize_window()


driver.find_element(By.NAME ,"username").send_keys("anand.roy@qxf2.com")
driver.find_element(By.ID, "login-submit").click()
driver.find_element(By.NAME, "password").send_keys("Gate@2022")
driver.find_element(By.ID, "login-submit").click()

act_title = driver.title
exp_title = "Your work - Jira"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()