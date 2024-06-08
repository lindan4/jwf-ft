from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route('/')
def renderMain():
     return render_template('index.html')


if __name__ == '__main__':
     app.run(port='5090')