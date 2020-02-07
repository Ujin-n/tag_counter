class TagCounter:
    def __init__(self, url):
        self.url = url

    def run(self):
        import urllib.request
        from bs4 import BeautifulSoup

        html = urllib.request.urlopen(self.url).read()

        soup = BeautifulSoup(html, 'html.parser')
        tags = soup.find_all()

        tag_dict = {}

        for tag in tags:
            tag_dict[tag.name] = tag_dict.get(tag.name, 0) + 1

        for tag, count in tag_dict.items():
            print(tag + ":", count)
