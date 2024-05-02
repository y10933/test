from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('intro.html')#

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80

