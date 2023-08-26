import random

import pandas
quote_data = pandas.read_csv("quotes.csv")
# quote_polish_data = quote_data[len(quote_data.Quote) < 120]
quotes = []
for index, row in quote_data.iterrows():
    new_quote = {}
    if len(row["Quote"]) < 120:
        new_quote["author"] = row["Author"]
        new_quote["quote"] = row["Quote"]
        quotes.append(new_quote)


class Quote:

    def __init__(self):
        self.quote_list = quotes

    def pick_quote(self):
        rand_quote = random.choice(self.quote_list)

        return rand_quote

    def get_quote(self):
        new_pick = self.pick_quote()
        formatted_quote = new_pick["quote"]

        return formatted_quote



