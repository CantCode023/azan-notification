# Gets local prayer time
from requests_html import HTMLSession
session = HTMLSession()

def _set_digits(digits, number): # set_digits(3, 2) -> 002
        str_number = str(number)
        number_length = len(str_number)

        if number_length == digits:
            return str_number
        while number_length != digits:
            str_number = "0" + str_number
            number_length = len(str_number)
        return str_number

def _12_to_12_hour_format(hour, am_pm):
    if am_pm == "am":
         return _set_digits(2, hour) if hour != 12 else "00"
    else:
         return _set_digits(2, hour+12) if hour != 12 else "12"

def get_prayer_times():
    prayers = {}

    response = session.get("https://www.google.com/search?q=maghrib")
    prayer_times = [i.text for i in response.html.find(".NxVxCc")]

    for index, time in enumerate(prayer_times[6:], 0):
        prayer = prayer_times[index]
        digits = time.replace("\u202f","").replace(":","")
        hour = int(digits[0])
        minutes = _set_digits(2, int(digits[1:3]))
        am_pm = digits[3:]
        _24_hour = _12_to_12_hour_format(hour, am_pm)

        prayers[prayer] = _24_hour+minutes

    return prayers