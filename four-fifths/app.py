from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()