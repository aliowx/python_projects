print('__________Aliowx__________')
number = "+989301553519" # so this is your number you should bring it 

# from test import  number
# also you can make any other file and chose the vatriable of your number and import that if you like it
import phonenumbers
from phonenumbers import geocoder

loc_number = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(loc_number,"en"))





  