import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

def phone_details():
    number = input("Enter phone number with country code: ")

    try:
        phone = phonenumbers.parse(number)

        print("\n--- Phone Number Details ---")
        print("Valid:", phonenumbers.is_valid_number(phone))
        print("Possible:", phonenumbers.is_possible_number(phone))
        print("Country/Region:",
              geocoder.description_for_number(phone, "en"))
        print("Carrier:",
              carrier.name_for_number(phone, "en"))
        print("International Format:",
              phonenumbers.format_number(
                  phone,
                  phonenumbers.PhoneNumberFormat.INTERNATIONAL
              ))

    except phonenumbers.NumberParseException:
        print("Invalid phone number")

phone_details()
