import datetime
import sys
import time
import traceback
from typing import List

import requests
from bs4 import BeautifulSoup

from eventscraper.models.entry import Entry
from eventscraper.models.scraper import Scraper


class MoritzbasteiScraper(Scraper):
    def __init__(self):
        # self.url = "https://www.moritzbastei.de/wp-admin/admin-ajax.php?offset=1&limit=10"
        self.url = "https://www.moritzbastei.de/programm-tickets-veranstaltungen"

    def get_page(self, url: str):
        with requests.get(url) as r:
            soup = BeautifulSoup(r.content, "html.parser")
        time.sleep(0.1)
        return soup

    def scrape(self) -> List[Entry]:
        soup = self.get_page(self.url)

        events = soup.find_all(
            'div',
            class_="fade-in faded flex flex-row flex-nowrap rounded-tr-md rounded-br-md overflow-hidden mb-8"
        )

        result = []
        for event in events:
            try:
                if "abgesagt" in event.text.lower():
                    continue

                event_url = event.find('a')['href']
                event_page = self.get_page(event_url)

                # title
                title = ' '.join(event.find('h3').text.split())

                description = ""
                # description = event_page.find('div', "entry-content leading-relaxed").text  #
                # description = ' '.join([e.replace('\n', '') for e in description.split(' ') if e != ''])

                # tags
                tags = event.find('div', class_="flex flex-row text-xs md:text-sm mt-2").text.replace('\n', '')
                tags = [t for t in tags.split('#') if t]

                # location
                location = event_page.find(
                    'p', "flex flex-row space-x-2 items-center").text.replace('\n', '').replace(' ', '')

                # start
                date_str = event.find('div', class_="o-event-list__date").text.replace('\n', '').replace(' ', '')
                date_str = date_str.split("Uhr")[0][2:]
                try:
                    date = datetime.datetime.strptime(date_str, "%d.%m.%Y,%H:%M")
                except:
                    raise Exception("Error in parsing datetime", title, date_str)

                # end
                end = None

                # url
                # event_url

                # price
                price = event_page.find_all('div', class_="pt-6")
                try:
                    price = price[1].text.strip().split('€')[0].split('\xa0')[1].replace(',', '')
                    price = int(price)
                except:
                    price = -1

                imageUrl = ""  # TO DO

                # origin
                origin = "Moritzbastei"

                event_entry = Entry(title, description, tags, location, date, end, event_url, price, imageUrl, origin)
                result.append(event_entry)

            except:
                print(traceback.format_exc(), file=sys.stderr)

        return result
