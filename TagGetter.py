import urllib.request
from bs4 import BeautifulSoup


class TagGetter:
    """ Gets and counts all tags from passed url page. """

    def __init__(self, url):
        """ Initialize tag getter and set input url. """
        self.url = url

    def run(self):
        """ Makes url request, parses html page, counts tags and prints them out. """
        self.url_verification()
        html = urllib.request.urlopen(self.url).read()

        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all()

        tag_dict = {}

        for tag in tags:
            tag_dict[tag.name] = tag_dict.get(tag.name, 0) + 1

        return tag_dict

    def url_verification(self):
        if not self.url.lower().startswith('https://'):
            self.url = 'https://' + self.url
