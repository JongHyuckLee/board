from flask import Flask, abort, render_template
from werkzeug.routing import BaseConverter


def index():
    return 'Hello World'


def sign_in():
    info = dict(
        name='test_name',
        email='test@mail.com',
        nick_name='test_nick_name'
    )
    return render_template('users/index.html', info=info)


def sign_up(id):
    return id
