#!/usr/bin/env python3

from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    sample_variable = "Contents of the sample variable"
    chars = ['a','b','c']
    return render_template('basic.html',test_variable=sample_variable,test_list=chars)

if(__name__ == '__main__'):
    app.run()
