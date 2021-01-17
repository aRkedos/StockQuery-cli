"""
Commandline Interface for StockQuery
"""

import argparse


help_texts = {"symbol" : "[Mandatory] Ticker symbol of the stock, e.g. AMD for" +
                         " Advanced Micro Devices",
              "start_date" : "[Mandatory] Start date of the period you wish to query" +
                             " in Ymd Format. e.g. 20200101 for the 1st of January 2020",
              "end_date" : "[Optional] End date of the period you wish to query." +
                           " If no date is given, start date will be used",
              "interval" : "[Optional] Interval within the queried time period, 1d, 1wk, 1mo for " +
                           "daily, weekyl or monthly"}

def create_parser():
    """
    Creates the Parser and adds arguments.

    symbol = Ticker symbol of the stock. Mandatory

    start_date = starte_date of the selected period. Mandatory

    end_edate = end_date of the selected period. Optional

    interval = interval within the selected period. Optional
    """

    parser = argparse.ArgumentParser(description="Get historical stock prices" +
                                     " from finance.yahoo.com")

    parser.add_argument("symbol", help=help_texts["symbol"])
    parser.add_argument("start_date", help=help_texts["start_date"])
    parser.add_argument("end_date", nargs="?", default=None, help=help_texts["end_date"])
    parser.add_argument("interval", nargs="?", default=None, help=help_texts["interval"])

    return parser


def parse(parser):
    """
    Parses and returns the arguments
    """

    arguments = parser.parse_args()

    return arguments
