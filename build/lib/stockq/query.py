import urllib.request


class Query(object):

    def __init__(self, url):

        self.url = url
        self.data = None

    def send_query(self):
        request = urllib.request.Request(self.url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(request) as csv:
            self.data = csv.read().decode("utf-8")

    def write_data(self, filename, data):

        with open(filename, "w+") as csv:
            csv.write(data)
