import datetime as dt
import random
import pytz

emojies = ["😁", "😉", "😋", "😙", "🥱", "🫠", "🫤", "🦊", "😺", "😸", "🦁", "🐼", "😜", "😌", "😶‍🌫️", "😤", "😼", "🐣", "🐧", "🦋", "🫰",
           "🤞", "✌️", "🫶", "✨"]


class WEEKDAY:

    def __init__(self):
        self.now = dt.datetime.now(pytz.timezone("Asia/Kolkata"))

    def get_day(self):
        emoji = random.choice(emojies)
        match (self.now.weekday()):
            case 0:
                return "Monday" + emoji + "\n"
            case 1:
                return "Tuesday" + emoji + "\n"
            case 2:
                return "Wednesday" + emoji + "\n"
            case 3:
                return "Thursday" + emoji + "\n"
            case 4:
                return "Friday" + emoji + "\n"
            case 5:
                return "Saturday" + emoji + "\n"
            case 6:
                return "Sunday" + emoji + "\n"
            case _:
                return ""
