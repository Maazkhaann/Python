import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input ("Enter mobile Number with country code: ")
mobileNo = phonenumbers.parse(mobileNo)

#Get Time Zone a phone number
print(timezone.time_zones_for_number(mobileNo))

# Getting carrier of a phone number
print(carrier.name_for_number(mobileNo,"en"))

#Getting region information
print(geocoder.description_for_number(mobileNo, "en"))

#Validating a phone Number
print("Valid Mobile No:",phonenumbers.is_valid_number(mobileNo))

#checking possibility of a number
print("checking possibility of Number :", phonenumbers.is_possible_number(mobileNo))