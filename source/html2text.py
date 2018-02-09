# http://softwaremaniacs.org/forum/django/14909/
from HTMLParser import HTMLParser
from re import sub


class _DeHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_skip = False
        self.__text = []

    def handle_data(self, data):
        if self.is_skip:
            self.is_skip = False
            return

        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')
        elif tag == 'style':
            self.is_skip = True

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def convert(text):
    if '</html>' not in text:
        return sub(r'<.+?>', '', text)

    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()

        return parser.text()

    except Exception as e:
        return str(e)
