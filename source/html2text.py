# http://softwaremaniacs.org/forum/django/14909/
from HTMLParser import HTMLParser
from re import sub


class _DeHTMLParser(HTMLParser):
    def __init__(self, extract_link):
        HTMLParser.__init__(self)
        self.extract_link = extract_link
        self.is_skip = False
        self.__text = []
        self.html_link = ''

    def handle_data(self, data):
        if self.is_skip:
            self.is_skip = False
            return

        text = data.strip()
        if len(text) > 0:
            text = sub('[\t\r\n]+', '', text)
            self.__text.append(text + ' ')
            if self.html_link:
                self.__text.append(self.html_link.encode('utf8'))
                self.__text.append(' ')

        self.html_link = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n')
        elif tag == 'br':
            self.__text.append('\n')
        elif tag == 'style':
            self.is_skip = True
        elif tag == 'a':
            if self.extract_link:
                link = dict(attrs).get('href', '')
                if link.startswith('http'):
                    self.html_link = link

    def text(self):
        return ''.join(self.__text).strip()


def convert(text, extract_link=False):
    if '</html>' not in text:
        return sub(r'<.+?>', '', text)

    try:
        parser = _DeHTMLParser(extract_link)
        parser.feed(text)
        parser.close()

        return parser.text()

    except Exception as e:
        return str(e)
