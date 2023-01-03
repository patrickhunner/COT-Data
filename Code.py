import pandas as pd

class COT_Data():
    def __init__(self, read):
        look_at = pd.read_excel(read)
        self.xlsx_df = look_at["File"].to_list()
        self.xlsx_names = look_at["File"].to_list()
        self.tickers = look_at["Ticker"].to_list()
        self.code = look_at["Number"].to_list()
        self.past_years = look_at["Historical"].to_list()
        self.df_headers = look_at["Headers"].to_list()
        self.df_headers = self.df_headers[0:35]
        self.df_analysis_columns = look_at["Analysis"].to_list()
        self.df_analysis_columns = [x for x in self.df_analysis_columns if pd.isnull(x) == False]
        if read == "Commodities_Look_At.xlsx":
            self.file = "Commodities.xlsx"
            self.writer = pd.ExcelWriter(self.file)
            self.num_hist = 8
        else:
            self.file = "Financials.xlsx"
            self.writer = pd.ExcelWriter(self.file)
            self.num_hist = 7

    def historical_pandas(self):        # convert historical csv to df
        for index in range(0,self.num_hist):
            df = pd.read_csv(self.past_years[index])
            df = df.filter(self.df_headers)
            self.past_years[index] = df

    def current_pandas(self, clear):           # convert analysis xlsx to df, clear if requested
        if clear == True:               # check if files are empty
            for index in range(0,len(self.xlsx_df)):
                self.xlsx_df[index] = pd.DataFrame(columns = self.df_headers)
        else:
            for index, dfs in enumerate(self.xlsx_df):
                self.xlsx_df[index] = pd.read_excel(self.file, sheet_name = dfs, engine='openpyxl')

    def add_historical(self):           # adds historical data if not already present
        self.historical_pandas()
        self.current_pandas(True)
        for i in range(0,self.num_hist):
            year = self.past_years[i]
            for index, row in year.iterrows():
                num = (index,row[2])[1]
                if num in self.code:
                    self.add_row(num,row, index)

    def add_row(self, num, row, i):        # adds row to the bottom of the dataframe
        row = row.tolist() + 16*[""]
        date = row[1]
        row[19] = row[4] - row[5]
        row[23] = row[6] - row[7]
        row[27] = row[9] - row[10]
        row[31] = row[11] - row[12]
        cur_df = self.xlsx_df[self.code.index(num)]
        cur_df.loc[len(cur_df)] = row

    def to_xlsx(self):          # writes all data to update xlsx files
        for index, files in enumerate(self.xlsx_df):
            ws = self.xlsx_names[index]
            files.to_excel(self.writer, ws, index = False)
        self.writer.save()
            
    def min_max_index(self):        # does what the name says
        above = []
        below = []
        for df in self.xlsx_df:     # iterate through each worksheet (commodity/financial)
            if len(df) > 156:
                for i in reversed(range(0,len(df) - 156)):      # iterate bottom to top, starting three years later than earliest
                    row = df.iloc[i]
                    for j in range(0, len(self.df_analysis_columns) - 4, 4):        # iterate through the different types of buyers
                        net_column = df.loc[i:i + 156, self.df_analysis_columns[j]]
                        max = net_column.max()
                        min = net_column.min()
                        net = row[self.df_analysis_columns[j]]
                        df.loc[i,self.df_analysis_columns[j + 1]] = max
                        df.loc[i,self.df_analysis_columns[j + 2]] = min
                        df.loc[i,self.df_analysis_columns[j + 3]] = ((net - min) / (max - min)) * 100
                        if df.iloc[i,1] == "5/24/2022" and df.loc[i,self.df_analysis_columns[j + 3]] < 10:
                            new = [df.iloc[i,0],self.df_analysis_columns[j + 3]]
                            below.append(new)
                        if df.iloc[i,1] == "5/24/2022" and df.loc[i,self.df_analysis_columns[j + 3]] > 90:
                            new = [df.iloc[i,0],self.df_analysis_columns[j + 3]]
                            above.append(new)
        print("above")
        for things in above:
            print(things)
        print("below")
        for things in below:
            print(things)        

    def remove_row(self):       # helper to remove row in testing
        for files in self.csv_names:
            df = pd.read_excel(files, engine = "openpyxl")
            df = df.drop(df.index[0])

analysis = COT_Data("Financials_Look_At.xlsx")
analysis.add_historical()
analysis.min_max_index()
analysis.to_xlsx()

analysis = COT_Data("Commodities_Look_At.xlsx")
analysis.add_historical()
analysis.min_max_index()
analysis.to_xlsx()
