import phonenumbers
from phonenumbers import geocoder
ph_num1 = phonenumbers.parse("+918247794171")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(ph_num1, "en"))
