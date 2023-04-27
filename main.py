from notifier import ToastNotifier
from datetime import datetime
import time
from get_prayer_times import get_prayer_times

toaster = ToastNotifier()

while True:
    prayer_times = get_prayer_times()
    current_time = datetime.now().strftime("%H%M")
    if current_time == prayer_times["Fajr"]:
        toaster.show_toast("Time to pray Fajr!", "By praying Fajr, our day will begin with light. It also saves you from the hell.")
    elif current_time == prayer_times["Sunrise"]:
        toaster.show_toast("Time to pray Dhuha", "Praying Dhuha benefits in health, intellect, physical, spirit and emotion. 2 rakaah of dhuah prayer is equal to giving alms to the poor.")
    elif current_time == prayer_times["Dhuhr"]:
        toaster.show_toast("Time to pray Dhuhr!", "During Zuhr, the gates of jannah is opened for the muslims!")
    elif current_time == prayer_times["Asr"]:
        toaster.show_toast("Time to pray for Asr!", "One who offers Asr prayer will get a double reward, don't miss your chance!")
    elif current_time == prayer_times["Maghrib"]:
        toaster.show_toast("Time to pray for Maghrib!", "Allah SWT will fullfil your Duas if you offer Maghrib prayer.")
    elif current_time == prayer_times["Isha"]:
        toaster.show_toast("Time to pray for Isha!", "Prayer Isha ensures a good night sleep keeping our minds free of guilt.")
    time.sleep(60)