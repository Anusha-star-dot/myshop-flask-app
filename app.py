from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to MyShop!"

@app.route('/date')
def date():
    return f"Current server time: {datetime.datetime.now()}"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)

