from flask import Flask, render_template, request
import pandas as pd
app = Flask(__name__)  
import numpy as np

def financials():
  look_at = pd.read_excel("Look_At/Financials_Look_At.xlsx")
  names = look_at["File"].to_list()
  html = look_at["File"].to_list()

  xls = pd.ExcelFile('Financials.xlsx')
  financials_html = f"""<b>Financials</b>
  <p>
      <a href="\">Home</a> | 
      <a href="financials">Financials</a> |
      <a href="commodities">Commodities</a> |
      <a href="scanner">Scanner</a> |
  </p>

  <html>
    <body>
        <form method = "post" action = "/financials">
          <p><input type = "submit" name = "submit_button" value = "Australian Dollar" />
          <input type = "submit" name = "submit_button" value = "Bitcoin" />
          <input type = "submit" name = "submit button" value = "Brazilian Real" />
          <input type = "submit" value = "British Pound" />
          <input type = "submit" value = "Canadian Dollar" />
          <input type = "submit" value = "DJIA Consolidated" />
          <input type = "submit" value = "Dow Jones" />
          <input type = "submit" value = "E-Mini S&P" />
          <input type = "submit" value = "E-Mini S&P Energy" />
          <input type = "submit" value = "E-Mini S&P Financial" />
          <input type = "submit" value = "E-Mini S&P Health Care" />
          <input type = "submit" value = "E-Mini S&P Utilities" />
          <input type = "submit" value = "Ethereum" />
          <input type = "submit" value = "Euro FX" />
          <input type = "submit" value = "Euro FX British Pound" />
          <input type = "submit" value = "Eurodollars" />
          <input type = "submit" value = "Fed Funds" />
          <input type = "submit" value = "Japanese Yen" />
          <input type = "submit" value = "Mexican Peso" />
          <input type = "submit" value = "Micro Bitcoin" />
          <input type = "submit" value = "Micro E-Mini Nasdaq" />
          <input type = "submit" value = "Micro Ether" />
          <input type = "submit" value = "Nasdaq Mini" />
          <input type = "submit" value = "Nasdaq Consolidated" />
          <input type = "submit" value = "Nikkei Stock" />
          <input type = "submit" value = "NZ Dollar" />
          <input type = "submit" value = "Russell E-Mini" />
          <input type = "submit" value = "S&P Consolidated" />
          <input type = "submit" value = "SO African Rand" />
          <input type = "submit" value = "Swiss Franc" />
          <input type = "submit" value = "Ultra UST 10Y" />
          <input type = "submit" value = "Ultra UST Bond" />
          <input type = "submit" value = "USD Index" />
          <input type = "submit" value = "UST 10Y" />
          <input type = "submit" value = "UST 2Y" />
          <input type = "submit" value = "UST 5Y" />
          <input type = "submit" value = "UST Bond" />
          <input type = "submit" value = "VIX" /></p>
        </form>   
    </body>
  </html>
  """
  for index, i in enumerate(names):
    df = pd.read_excel(xls, i)
    table_html = df.to_html(table_id="table", index=False)
    html[index] = table_html
    file = "templates/" + i + ".html"
    f = open(file,"w")
    html_code = financials_html + f"""
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
    f.write(html_code)

def commodities():
  look_at = pd.read_excel("Look_At/Commodities_Look_At.xlsx")
  names = look_at["File"].to_list()
  html = look_at["File"].to_list()

  xls = pd.ExcelFile('Commodities.xlsx')
  commodities_html = f"""<b>Commodities</b>
  <p>
      <a href="\">Home</a> | 
      <a href="financials">Financials</a> |
      <a href="commodities">Commodities</a> |
      <a href="scanner">Scanner</a> |
  </p>

  <html>
    <body>
        <form method = "post" action = "/commodities">
          <p><input type = "submit" name = "submit_button" value = "Aluminum" />
          <input type = "submit" name = "submit_button" value = "Butter" />
          <input type = "submit" name = "submit_button" value = "Canola" />
          <input type = "submit" name = "submit_button" value = "Cheese" />
          <input type = "submit" name = "submit_button" value = "Coal" />
          <input type = "submit" name = "submit_button" value = "Cocoa" />
          <input type = "submit" name = "submit_button" value = "Coffee" />
          <input type = "submit" name = "submit_button" value = "Copper" />
          <input type = "submit" name = "submit_button" value = "Corn" />
          <input type = "submit" name = "submit_button" value = "Cotton" />
          <input type = "submit" name = "submit_button" value = "Crude Oil" />
          <input type = "submit" name = "submit_button" value = "Ethane" />
          <input type = "submit" name = "submit_button" value = "Ethanol" />
          <input type = "submit" name = "submit_button" value = "Orange Juice" />
          <input type = "submit" name = "submit_button" value = "Gasoline" />
          <input type = "submit" name = "submit_button" value = "Gold" />
          <input type = "submit" name = "submit_button" value = "Henry Hub" />
          <input type = "submit" name = "submit_button" value = "Henry Hub Index" />
          <input type = "submit" name = "submit_button" value = "Lean Hogs" />
          <input type = "submit" name = "submit_button" value = "Live Cattle" />
          <input type = "submit" name = "submit_button" value = "Natural Gas" />
          <input type = "submit" name = "submit_button" value = "Palladium" />
          <input type = "submit" name = "submit_button" value = "Platinum" />
          <input type = "submit" name = "submit_button" value = "Propane" />
          <input type = "submit" name = "submit_button" value = "Rough Rice" />
          <input type = "submit" name = "submit_button" value = "Silver" />
          <input type = "submit" name = "submit_button" value = "Soybean Meal" />
          <input type = "submit" name = "submit_button" value = "Soybean Oil" />
          <input type = "submit" name = "submit_button" value = "Soybeans" />
          <input type = "submit" name = "submit_button" value = "Steel" />
          <input type = "submit" name = "submit_button" value = "Sugar" />
          <input type = "submit" name = "submit_button" value = "Wheat-HRW" />
          <input type = "submit" name = "submit_button" value = "Wheat" />
          <input type = "submit" name = "submit_button" value = "WTI Crude Oil" />
          <input type = "submit" name = "submit_button" value = "WTI" />
          <input type = "submit" name = "submit_button" value = "WTI" />
          <input type = "submit" name = "submit_button" value = "WTI" />
          <input type = "submit" name = "submit_button" value = "WTI" />
          <input type = "submit" value = "WTI" /></p>
        </form>   
    </body>
  </html>
  """
  for index, i in enumerate(names):
    df = pd.read_excel(xls, i)
    table_html = df.to_html(table_id="table")
    html[index] = table_html
    file = "templates/" + i + ".html"
    f = open(file,"w")
    html_code = commodities_html + f"""
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
    f.write(html_code)

# commodities()
# financials()


@app.route('/')
def home():
    return render_template('home.html', template_folder='templates')
  
@app.route('/financials',methods = ['POST','GET'])
def financials():
  if request.method == 'POST':
    return render_template(request.form.get("submit_button") + ".html", template_folder="templates")
  else:
    return render_template("financials.html", template_folder='templates')

@app.route('/commodities', methods = ['Post','Get'])
def commodities():
  if request.method == 'POST':
    return render_template(request.form.get("submit_button") + ".html", template_folder="templates")
  else:
    return render_template("commodities.html", template_folder='templates')

@app.route('/scanner')
def scanner():
  return render_template("scanner.html", template_folder='templates')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')