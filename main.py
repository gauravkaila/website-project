# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:01:31 2016

@author: Gaurav
"""

from flask import Flask
from flask import render_template
import os


app = Flask(__name__)
@app.route('/')
@app.route('/home')
def home():
    return "first website, first line"

@app.route('/about/')
def about():
    return 'Gaurav Kaila'

@app.route('/test/')
def test():
    return render_template('test.html')
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    if port == 5000:
        app.debug = True

    app.run(host='0.0.0.0', port=port)
