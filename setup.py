from setuptools import setup


setup (

        name = "StockQuery",
        version="0.1.0",
        author="aRkedos",
        packages=['stockq'],
        description = "Query historical stock prices from finance.yahoo.com",
        entry_points = { 'console_scripts': ['stockq=stockq.main:main']},

)
