import pandas as pd
import matplotlib.pyplot as plt
from itables import init_notebook_mode, show

df = pd.read_csv('Historicals\\2022.csv')
df = df.iloc[0:20,0:10]
init_notebook_mode(all_interactive=False)
df
# fp = open("templates\\index.html","w")
# fp.write(df)
# fp.close()
# df.plot(kind="scatter",x="Report_Date_as_MM_DD_YYYY",y="Tot_Rept_Positions_Long_All")
# plt.show()