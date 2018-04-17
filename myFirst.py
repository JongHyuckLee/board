from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def join_form():
    return render_template('join_form.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
