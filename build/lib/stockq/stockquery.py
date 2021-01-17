from datetime import datetime


class StockQuery(object):

    def __init__(self, symbol, date_start, date_end = None, interval = None):

        self.symbol = symbol
        self.date_str_start = date_start + " 00:00:00"
        if date_end is None:
            self.date_str_end = self.date_str_start
        else:
            self.date_str_end = date_end + " 00:00:00"
        if interval is None:
            self.interval = "1d"
        else:
            self.interval = interval

        date_start_obj = datetime.strptime(self.date_str_start, "%Y%m%d %H:%M:%S")
        self.start_timestamp = str(int(datetime.timestamp(date_start_obj) + 3600))

        if self.date_str_end is not None:
            date_end_obj = datetime.strptime(self.date_str_end, "%Y%m%d %H:%M:%S")
            self.end_timestamp = str(int(datetime.timestamp(date_end_obj) + 3600))
        else:
            self.end_timestamp = self.start_timestamp

    def build_url(self):

        return  ("https://query1.finance.yahoo.com/v7/finance/download/" + 
                 self.symbol + "?period1=" + self.start_timestamp + "&period2=" +
                 self.end_timestamp + "&interval=" + self.interval + "&events" +
                 "=history&includeAdjustedClose=true")  





