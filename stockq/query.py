"""
Query object which holds the final url and downloads the Data
"""
import urllib.request


class Query:
    """
    Query object

    self.url = final url for query

    send_query() = sends the query and spoofs the user-agent

    write_data() = writes the data to disk
    """

    def __init__(self, url):

        self.url = url
        self.data = None

    def send_query(self):
        """
        Requests the data
        """
        request = urllib.request.Request(self.url)
        request.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(request) as csv:
            self.data = csv.read().decode("utf-8")

    def write_data(self, filename):
        """
        Writes data from send_query() to disc.
        Will overwrite if file already exists
        """

        with open(filename, "w+") as csv:
            csv.write(self.data)
