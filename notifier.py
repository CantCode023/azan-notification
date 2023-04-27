import plyer.platforms.win.notification
from plyer import notification

class ToastNotifier:
    def show_toast(self, title, body):
        notification.notify(title, body)