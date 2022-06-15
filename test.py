import pandas as pd
import matplotlib.pyplot as plt
from itables import init_notebook_mode, show
import webbrowser

# df = pd.read_csv('Historicals\\2022.csv')
# df = df.iloc[0:1000,0:3]
xls = pd.ExcelFile('Financials.xlsx')
df = pd.read_excel(xls, 'Australian Dollar')
table_html = df.to_html(table_id="table")
html = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    </header>
    <body>
    {table_html}
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table').DataTable({{
                "lengthMenu": [ [15, 50, 100, -1], [15, 50, 100, "All"] ],
            }});
        }});
    </script>
    </body>
    </html>
    """
open("index.html","w").write(html)
webbrowser.open("index.html")
# fp = open("templates\\index.html","w")
# fp.write(df)
# fp.close()
# df.plot(kind="scatter",x="Report_Date_as_MM_DD_YYYY",y="Tot_Rept_Positions_Long_All")
# plt.show()