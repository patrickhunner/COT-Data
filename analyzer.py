import json
import pandas as pd
import openpyxl
from sodapy import Socrata
# from sodapy import Socrata
import requests
from IPython.display import display
from openpyxl import load_workbook

commodity_look = pd.read_excel("Commodities_Look_At.xlsx")
financial_look = pd.read_excel("Financials_Look_At.xlsx")

commodity_codes = commodity_look["Number"].to_list()
financial_codes = financial_look["Number"].to_list()

commodity_columns = commodity_look["Headers"].to_list()
financial_columns = financial_look["Headers"].to_list()

commodity_analysis = commodity_look["Analysis"].to_list()
financial_analysis = financial_look["Analysis"].to_list()

writer = pd.ExcelWriter("New_Commodities.xlsx", engine='openpyxl')

client = Socrata("publicreporting.cftc.gov", None)

def compile_commodity(code):
    params = {
        "cftc_contract_market_code": code,
    }
    resp = client.get("72hh-3qpy", **params)
    df = pd.DataFrame.from_records(resp)
    # df = df[::-1]
    df = df.filter(commodity_columns)
    if df.shape[0] > 0:
        df["report_date_as_yyyy_mm_dd"] = pd.to_datetime(df["report_date_as_yyyy_mm_dd"])
        df = df.sort_values(by="report_date_as_yyyy_mm_dd", ascending=False)
        label = df.iloc[1,0].split("-")[0]
        df = min_max_analysis(df)
        print(label)
        df.to_excel(writer, sheet_name=label, index=False)

def min_max_analysis(df):
    df["Comm_Net"] = df["prod_merc_positions_long"].astype(int) - df["prod_merc_positions_short"].astype(int)
    df["Comm_Max"] = df["Comm_Net"].max()
    df["Comm_Min"] = df["Comm_Net"].min()
    df["Comm_Index"] = ((df["Comm_Net"] - df["Comm_Min"]) / (df["Comm_Max"] - df["Comm_Min"])) * 100
    df["Swap_Net"] = df["swap_positions_long_old"].astype(int) - df["swap__positions_short_old"].astype(int)
    df["Swap_Max"] = df["Swap_Net"].max()
    df["Swap_Min"] = df["Swap_Net"].min()
    df["Swap_Index"] = ((df["Swap_Net"] - df["Swap_Min"]) / (df["Swap_Max"] - df["Swap_Min"])) * 100
    df["M_Money_Net"] = df["m_money_positions_long_old"].astype(int) - df["m_money_positions_short_old"].astype(int)
    df["M_Money_Max"] = df["M_Money_Net"].max()
    df["M_Money_Min"] = df["M_Money_Net"].min()
    df["M_Money_Index"] = ((df["M_Money_Net"] - df["M_Money_Min"]) / (df["M_Money_Max"] - df["M_Money_Min"])) * 100
    df["Other_Net"] = df["other_rept_positions_short_1"].astype(int) - df["other_rept_positions_long_1"].astype(int)
    df["Other_Max"] = df["Other_Net"].max()
    df["Other_Min"] = df["Other_Net"].min()
    df["Other_Index"] = ((df["Other_Net"] - df["Other_Min"]) / (df["Other_Max"] - df["Other_Min"])) * 100
    return df

def analysis(df):
    for i in reversed(range(0,len(df) - 156)):      # iterate bottom to top, starting three years later than earliest
        row = df.iloc[i]
        for j in range(0, len(commodity_analysis) - 4, 4):        # iterate through the different types of buyers
            net_column = df.loc[i:i + 156, commodity_analysis[j]]
            max = net_column.max()
            min = net_column.min()
            net = row[commodity_analysis[j]]
            df.loc[i,commodity_analysis[j + 1]] = max
            df.loc[i,commodity_analysis[j + 2]] = min
            df.loc[i,commodity_analysis[j + 3]] = ((net - min) / (max - min)) * 100
            if df.iloc[i,1] == "5/24/2022" and df.loc[i,commodity_analysis[j + 3]] < 10:
                new = [df.iloc[i,0], commodity_analysis[j + 3]]
            if df.iloc[i,1] == "5/24/2022" and df.loc[i,commodity_analysis[j + 3]] > 90:
                new = [df.iloc[i,0], commodity_analysis[j + 3]]
    return df

def compile_financial(code):
    pass

def analyze_index():
    pass

def notify_user():
    pass

if __name__ == "__main__":
    for num in commodity_codes:
        compile_commodity(num)
    writer.close()
    for num in financial_codes:
        break
        compile_financial(num)