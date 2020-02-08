import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime


class TagGetter:
    """ Gets and counts all tags from passed url page. """

    def __init__(self, url):
        """ Initialize tag getter and set input url. """
        self.url = url

    def run(self):
        """ Makes url request, parses html page, counts tags and prints them out. """
        # verify url
        self.url_verification()

        # url request
        html = urllib.request.urlopen(self.url).read()

        # url log
        self.url_logger()

        # url parse
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all()

        # collect and count tags
        tag_dict = {}
        for tag in tags:
            tag_dict[tag.name] = tag_dict.get(tag.name, 0) + 1

        return tag_dict

    def url_verification(self):
        """ Verify input URL, add https:// if needed. """
        if not self.url.lower().startswith('https://'):
            self.url = 'https://' + self.url

    def url_logger(self):
        """ Logs date, time and url. """
        # getting date/time
        now = datetime.now()
        current_time = now.time().strftime("%H:%M:%S")
        current_date = now.date()

        # write to file
        with open('log.txt', 'a') as f_reader:
            f_reader.write(str(current_date) + ' ' + str(current_time) + ' ' + self.url + '\n')

