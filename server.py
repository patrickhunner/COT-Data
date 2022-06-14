from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
  from waitress import serve
  serve(app, host="0.0.0.0", port=8080)
