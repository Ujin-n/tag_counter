from html.parser import HTMLParser
import urllib.request
import urllib.parse
import urllib.error

url = 'https://google.com'
html = urllib.request.urlopen(url).read().decode()

#print(html)
count = 0

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        count += 1



parser = MyHTMLParser()
parser.feed(html)

#print(type(html))