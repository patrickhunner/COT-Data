import pandas_datareader as pdr
import datetime as dt
import pandas as pd


seven = pdr.get_data_yahoo("6A=F","5/3/2022","5/28/2022")
print(seven)