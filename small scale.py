from calendar import c
from email import header
from json import load
from typing import final
from urllib.request import Request, urlopen
import urllib.request
from wsgiref import headers
from xmlrpc.client import Boolean
import requests
import pandas as pd
import numpy as np
from datetime import datetime
import openpyxl
from zipfile import ZipFile
import os
from io import BytesIO
from openpyxl import load_workbook
import pandas_datareader as pdr
import datetime as dt


tickers = pd.read_excel("Financials_Look_At.xlsx")["Anything"].to_list()

for thing in tickers:
    if thing == "None" or thing == "Date":
        pass
    else:
        print(thing)
        start = dt.datetime(1980,1,1)
        end = dt.datetime(2022,6,13)
        data = pdr.get_data_yahoo(thing,start,end)
        data = data["Close"]
        print(data)

# print(final_dict)
# print(final_dict["04/22/2022"])


