from io import BytesIO
from urllib.request import urlopen
import pandas as pd
from requests import Request
from calendar import c
from csv import writer
from email import header
from json import load
from typing import final
from urllib.request import Request, urlopen
import urllib.request
from wsgiref import headers
from xmlrpc.client import Boolean
import requests
import pandas as pd
from datetime import datetime
import openpyxl
from zipfile import ZipFile
import os
from io import BytesIO
import pandas_datareader as pdr
import datetime as dt
import xlsxwriter
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook

url = "https://www.cftc.gov/dea/newcot/FinFutWk.txt"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
data = urlopen(request_site).read()
data = pd.read_csv(BytesIO(data), header=None)
row = data.iloc[5]


# other = pd.read_csv("thing2.csv")
# other = other.iloc[0]
# beg = 0
# list = []
# for i in range(0,len(row)):
#     print(i)
#     print(row[i])



# columns = [0,2,3,7,]