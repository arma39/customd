from html.parser import HTMLParser


class ImageFinder(HTMLParser):

    def __init__(self):
        super().__init__()
        self.image_links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for (attributes, value) in attrs:
                if attributes == 'src':
                    self.image_links.append(value)

    def __repr__(self):
        return repr(self.image_links)

    def error(self, message):
        pass
