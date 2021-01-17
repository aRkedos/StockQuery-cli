"""
Entrypoint for StockQuery. Sets up the parser, the StockQuery Object
and the URL for the query
"""
import urllib.error

from .stockquery import StockQuery
from .query import Query
from . import cli


def main():

    """
    Sets up the argument parser.

    parser = the argument parser from the cli module.

    stock = the StockQuery object which will be initialized with the parsed
             arguments

    get_data = Query object which will retrieve the data from finance.yahoo.com

    """

    parser = cli.create_parser()
    arguments = cli.parse(parser)

    stock = StockQuery(arguments.symbol, arguments.start_date, arguments.end_date)

    url = ("https://query1.finance.yahoo.com/v7/finance/download/" +
           stock.symbol + "?period1=" + stock.start_timestamp + "&period2=" +
           stock.end_timestamp + "&interval=" + stock.interval + "&events" +
           "=history&includeAdjustedClose=true")

    try:
        get_data = Query(url)
        get_data.send_query()
        get_data.write_data(stock.symbol + ".csv")
    except urllib.error.HTTPError:
        print("No Data available for selected time period. Maybe it was a non Trade day.")


if __name__ == "__main__":
    main()
