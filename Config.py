import configparser

subject_file = configparser.ConfigParser()

subject_file.add_section("Temperature_Below_23°C")
subject_file.set("Temperature_Below_23°C", "Buy_moisturizers", "23°C")


subject_file.add_section("Temperature_Above_23°C")
subject_file.set("Temperature_Above_23°C", "Buy_sunscreens", "30°C")


with open(r"Config.ini", 'w') as configfile:
    subject_file.write(configfile)