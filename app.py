from flask import Flask, render_template, request, redirect,url_for
import convert

users = {}

app = Flask('File Convertor')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods = ['POST'])
def submit():
    pass


if __name__ == '__main__':
    app.run(debug=True)
