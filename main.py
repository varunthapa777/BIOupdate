import instagrapi
import PIL
from quotes import Quote
from weekday import WEEKDAY

USERNAME = "username"
PASSWORD = "password"


today = WEEKDAY()

qt = Quote()
quote_of_the_day = today.get_day()+qt.get_quote()
cl = instagrapi.Client()
cl.login(username="ig_varunthapa", password="VvAaRrUuNn12")

notes = cl.get_notes()

cl.account_set_biography(quote_of_the_day)
cl.logout()
print(quote_of_the_day)