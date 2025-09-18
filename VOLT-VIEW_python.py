from flask import Flask, render_template
from flaskwebgui import FlaskUI

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('VOLT-VIEW_html.html')

if __name__ == '__main__':
    FlaskUI(app=app, server="flask", width=800, height=480, port=8000).run()