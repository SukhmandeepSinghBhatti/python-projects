import phonenumbers
from phonenumbers import timezone,carrier,geocoder

number = input('Enter the number here: ')
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
e = phonenumbers.FrozenPhoneNumber(phone)
print(phone)
print(time)
print(car)
print(reg)
print(e)