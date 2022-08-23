import configparser

subject_file = configparser.ConfigParser()

subject_file.add_section("Xpath_main_text")
subject_file.set("Xpath_main_set", "Check temperature", "//span[@id='temperature']")
subject_file.set("Xpath_main_set", "Buy moisturizers", "//button[contains(text(),'Buy moisturizers')]")
subject_file.set("Xpath_main_set", "Buy sunscreens", "//button[contains(text(),'Buy sunscreens')]")


subject_file["Product Samples"] = {"For moisturizers samples":
                 "//p[contains(text(),'Price')]",
                "For sunscreens samples":
                "//p[contains(text(),'Price')]"}

subject_file["Least_Price"] = {"Least price for sunscreens":
                            "//p[contains(text(),'product_price')]/following-sibling::button[@class='btn btn-primary']",
                             "Least price for moisturizers" :
                             "//p[contains(text(),'product_price')]/following-sibling::button[@class='btn btn-primary']"}

with open(r"Config.ini", 'w') as configfile:
    subject_file.write(configfile)