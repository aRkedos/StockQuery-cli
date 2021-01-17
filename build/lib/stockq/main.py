import urllib.error


from .stockquery import StockQuery
from .query import Query 
from . import cli
from stockq import main


def main():

    parser = cli.create_parser()
    arguments = cli.parse(parser)

    stockq = StockQuery(arguments.symbol, arguments.start_date, arguments.end_date, 
                       arguments.interval)

    url = ("https://query1.finance.yahoo.com/v7/finance/download/" + 
           stockq.symbol + "?period1=" + stockq.start_timestamp + "&period2=" +
           stockq.end_timestamp + "&interval=" + stockq.interval + "&events" +
           "=history&includeAdjustedClose=true") 

    try:
        get_data = Query(url)
        get_data.send_query()
        get_data.write_data(stockq.symbol + ".csv", get_data.data)
    except urllib.error.HTTPError:
        print("No Data availbe for selected time period. Maybe it was a non Trade day.")

if __name__ == "__main__":
    main()
