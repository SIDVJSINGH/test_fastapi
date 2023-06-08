from configparser import ConfigParser

# initializing the object
config = ConfigParser()

# to read from file
config.read("config.ini")

# PRINTING VALUES

# printing Section name from file
# print(config.sections())

# keys of section
# print(list(config['COMPANY']))

# values of section
# print(config['COMPANY']['name'])

# Adding Values

# # adding section
# # key and section has to be unique all the time but values can be duplicated
# config.add_section('EMPLOYEE')
# config.set('EMPLOYEE', 'name', 'siddhant')
# config.set('EMPLOYEE', 'designation', 'intern')
# config.set('EMPLOYEE', 'city', 'delhi')
#
# # write to the file
# with open('config.ini', 'w') as file:
#     config.write(file)

# # update values
# config.set('EMPLOYEE','name', 'siddhant vijay singh')
# with open('config.ini', 'w') as file :
#     config.write(file)

# Adding section, key and value pair in config file
# This way you can add and change values anytime without setting section first
config["USERINFO"] = {
    "admin": "Siddhant",
    "loginid": "sidvjsingh",
    "password": "gogol"
}

config["DEFAULT_CONFIG"] = {
    "host": "google.com",
    "port": "8080",
    "ipaddr": "8.8.8.8",
    "service_account_filepath": "C:/Users/siddhant vijay singh/Downloads/sushant-calcium-sunbeam-341614-3db196fe803d.json",
    "num_threds": "8"
}

# # REMOVING A SECTION
config.remove_section("USERINFO")
config.remove_section("USERINFO")

with open('config.ini','w') as file:
    config.write(file)

# list of all sections of config file
print(list(config.sections()))