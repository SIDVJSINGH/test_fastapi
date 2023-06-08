from configparser import ConfigParser

# initializing the object
config = ConfigParser()

# to read from file
config.read("config.ini")

# PRINTING VALUES

# printing Section name from file
# print(config.sections())

# keys of section
# print(list(config['Company']))

# values of section
# print(config['Company']['name'])

# Adding Values

# # adding section
# # key and section has to be unique all the time but values can be duplicated
# config.add_section('Employee')
# config.set('Employee', 'name', 'siddhant')
# config.set('Employee', 'designation', 'intern')
# config.set('Employee', 'city', 'delhi')
#
# # write to the file
# with open('config.ini', 'w') as file:
#     config.write(file)

# # update values
# config.set('Employee','name', 'siddhant vijay singh')
# with open('config.ini', 'w') as file :
#     config.write(file)