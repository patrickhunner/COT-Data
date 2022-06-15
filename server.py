from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', template_folder='templates')
  
@app.route('/commodities')
def about():
  return render_template("about.html", template_folder='templates')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')