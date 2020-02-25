import urllib.request
from bs4 import BeautifulSoup


class TagGetter:
    """ Gets and counts all tags from passed url page. """

    def __init__(self, url, current_date, current_time):
        """ Initialize tag getter and set input url. """
        self.url = url
        self.current_date = current_date
        self.current_time = current_time

    def run(self):
        """ Makes url request, parses html page, counts tags and prints them out. """

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

    def url_logger(self):
        """ Logs date, time and url. """

        # write to file
        with open('log.txt', 'a') as f_reader:
            f_reader.write(str(self.current_date) + ' ' + str(self.current_time) + ' ' + self.url + '\n')
