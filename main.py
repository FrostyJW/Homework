from flask import Flask, render_template
import os
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('base.html')

@app.route('/todopage')
def todopage():
    return render_template('todopage.html')

@app.route('/todolist')
def todolist():
    return render_template('todolistpage.html')


if __name__ == "__main__":
    app.run()