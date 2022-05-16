import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd


class Scrapper:
    def __init__(self, url):
        self.url = url

    def scrapping(self):
        EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}"
        url_open = urlopen(self.url)

        soup = BeautifulSoup(url_open, 'html.parser')
        soup = soup.get_text()

        emails = set(re.findall(EMAIL_REGEX, soup))
        email_list = list(emails)

        print(email_list)


if __name__ == '__main__':
    sc = Scrapper("https://www.nichi.com/contact-us/")
    sc.scrapping()