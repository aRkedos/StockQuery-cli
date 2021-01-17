"""
StockQuery Object which handles the variable parts of the url

"""
from datetime import datetime


class StockQuery:
    """
    StockQuery object which holds the Data required to make a query.

    symbol = ticker symbol
    date_start = start date of the selected period
    date_end = end date of the selected period
    interval = interval within the selected period,
               1d = daily, 1wk = weekly, 1mo = monthly
    event = type of query within the selected period,
            history for price history
            div for dividends
            split for stock splits
    """
    def __init__(self, symbol, date_start, date_end = None):

        self.symbol = symbol
        self.date_str_start = date_start + " 00:00:00"
        if date_end is None:
            self.date_str_end = self.date_str_start
        else:
            self.date_str_end = date_end + " 00:00:00"

        self.interval = "1d"
        self.event = "history"

        date_start_obj = datetime.strptime(self.date_str_start, "%Y%m%d %H:%M:%S")
        self.start_timestamp = str(int(datetime.timestamp(date_start_obj) + 3600))

        if self.date_str_end is not None:
            date_end_obj = datetime.strptime(self.date_str_end, "%Y%m%d %H:%M:%S")
            self.end_timestamp = str(int(datetime.timestamp(date_end_obj) + 3600))
        else:
            self.end_timestamp = self.start_timestamp

    def set_interval(self, interval):
        """
        sets the interval attribute to the desired value
        """
        if interval in ["1d", "1wk", "1mo"]:
            self.interval = interval
        else:
            self.interval = "1d"


    def set_event(self, event):
        """
        sets the event attribute to the desired value
        """
        if event in ["history", "div", "split"]:
            self.event = event
        else:
            self.event = "history"
