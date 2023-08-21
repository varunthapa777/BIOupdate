import instagrapi
import PIL
from quotes import Quote
from weekday import WEEKDAY
import os

USERNAME = os.environ["INSTA_USER"]
PASSWORD = os.environ["INSTA_PASSWORD"]


today = WEEKDAY()

qt = Quote()
quote_of_the_day = today.get_day()+qt.get_quote()
cl = instagrapi.Client()
cl.load_settings('dump.json')
cl.login(username=USERNAME, password=PASSWORD)



cl.account_set_biography(quote_of_the_day)

print(quote_of_the_day)
