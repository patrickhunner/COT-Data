import pandas as pd
from sodapy import Socrata
from openpyxl import load_workbook

overbought = []
oversold = []

commodity_look = pd.read_excel("Commodities_Look_At.xlsx")
financial_look = pd.read_excel("Financials_Look_At.xlsx")

commodity_codes = commodity_look["Number"].to_list()
financial_codes = financial_look["Number"].to_list()

commodity_columns = commodity_look["Headers"].to_list()
financial_columns = financial_look["Headers"].to_list()

commodity_writer = pd.ExcelWriter("Commodities.xlsx", engine='openpyxl')
financial_writer = pd.ExcelWriter("Financials.xlsx", engine='openpyxl')

client = Socrata("publicreporting.cftc.gov", None)

def compile_commodity(code):
    params = {
        "cftc_contract_market_code": code
    }
    resp = client.get("72hh-3qpy", **params)
    df = pd.DataFrame.from_records(resp)
    df = df.filter(commodity_columns)
    if df.shape[0] > 0:
        df["report_date_as_yyyy_mm_dd"] = pd.to_datetime(df["report_date_as_yyyy_mm_dd"])
        df = df.sort_values(by="report_date_as_yyyy_mm_dd", ascending=False)
        label = df.iloc[1,0].split("-")[0]
        df = commodity_min_max_analysis(df)
        print(label)
        df.to_excel(commodity_writer, sheet_name=label, index=False)
    
def compile_financial(code):
    params = {
        "cftc_contract_market_code": code
    }
    resp = client.get("gpe5-46if", **params)
    df = pd.DataFrame.from_records(resp)
    df = df.filter(financial_columns)
    if df.shape[0] > 0:
        df["report_date_as_yyyy_mm_dd"] = pd.to_datetime(df["report_date_as_yyyy_mm_dd"])
        df = df.sort_values(by="report_date_as_yyyy_mm_dd", ascending=False)
        label = df.iloc[1,0].split("-")[0]
        df = financial_min_max_analysis(df)
        print(label)
        df.to_excel(financial_writer, sheet_name=label.replace("/","-"), index=False)

def commodity_min_max_analysis(df):
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
    if df.at[0, "Comm_Index"] > 90 or df.at[0, "Swap_Index"] > 90 or df.at[0, "M_Money_Index"] > 90 or df.at[0, "Other_Index"] > 90:
        overbought.append(df.at[0, "market_and_exchange_names"])
    elif df.at[0, "Comm_Index"] < 10 or df.at[0, "Swap_Index"] < 10 or df.at[0, "M_Money_Index"] < 10 or df.at[0, "Other_Index"] < 10:
        oversold.append(df.at[0, "market_and_exchange_names"])
    return df

def financial_min_max_analysis(df):
    df["dealer_net"] = df["dealer_positions_long_all"].astype(int) - df["dealer_positions_short_all"].astype(int)
    df["dealer_max"] = df["dealer_net"].max()
    df["dealer_min"] = df["dealer_net"].min()
    df["dealer_index"] = ((df["dealer_net"] - df["dealer_min"]) / (df["dealer_max"] - df["dealer_min"])) * 100
    df["asset_mgr_net"] = df["asset_mgr_positions_long"].astype(int) - df["asset_mgr_positions_short"].astype(int)
    df["asset_mgr_max"] = df["asset_mgr_net"].max()
    df["asset_mgr_min"] = df["asset_mgr_net"].min()
    df["asset_mgr_index"] = ((df["asset_mgr_net"] - df["asset_mgr_min"]) / (df["asset_mgr_max"] - df["asset_mgr_min"])) * 100
    df["lev_money_net"] = df["lev_money_positions_long"].astype(int) - df["lev_money_positions_short"].astype(int)
    df["lev_money_max"] = df["lev_money_net"].max()
    df["lev_money_min"] = df["lev_money_net"].min()
    df["lev_money_index"] = ((df["lev_money_net"] - df["lev_money_min"]) / (df["lev_money_max"] - df["lev_money_min"])) * 100
    df["other_net"] = df["other_rept_positions_long"].astype(int) - df["other_rept_positions_short"].astype(int)
    df["other_max"] = df["other_net"].max()
    df["other_min"] = df["other_net"].min()
    df["other_index"] = ((df["other_net"] - df["other_min"]) / (df["other_max"] - df["other_min"])) * 100
    if df.at[0, "dealer_index"] > 90 or df.at[0, "asset_mgr_index"] > 90 or df.at[0, "lev_money_index"] > 90 or df.at[0, "other_index"] > 90:
        overbought.append(df.at[0, "market_and_exchange_names"])
    elif df.at[0, "dealer_index"] < 10 or df.at[0, "asset_mgr_index"] < 10 or df.at[0, "lev_money_index"] < 10 or df.at[0, "other_index"] < 10:
        oversold.append(df.at[0, "market_and_exchange_names"])
    return df

if __name__ == "__main__":
    for num in commodity_codes:
        compile_commodity(num)
    commodity_writer.close()
    for num in financial_codes:
        compile_financial(num)
    financial_writer.close()
    print("OVERBOUGHT:")
    for item in overbought:
        print(item)
    print("OVERSOLD:")
    for item in oversold:
        print(item)