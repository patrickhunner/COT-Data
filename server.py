from flask import Flask, render_template

app = Flask(__name__)       

@app.route('/')
def index():
    return render_template('index.html', template_folder='templates')
  
@app.route('/financials')
def financials():
  return render_template("Financials.html", template_folder='templates')

@app.route('/commodities')
def commodities():
  return render_template("commodities.html", template_folder='templates')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')