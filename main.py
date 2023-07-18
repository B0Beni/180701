# ngrok.com
# HEROKU
# PYHTONANYWHERE
# PYHTON Railwe
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask приветствует вас'
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

