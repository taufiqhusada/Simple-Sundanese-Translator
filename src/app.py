from flask import Flask, render_template, request
from solver import solve
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/translate', methods = ['POST'])
def translate():
    inputText = request.form['inputText']
    translationOption = request.form['translationOption']
    algoOption = request.form['algoOption']

    res = solve(inputText, algoOption, translationOption)

    return render_template('index.html', result=res)

if __name__ == "__main__":
    app.run()