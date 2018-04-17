from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/user')
def showUserName() :
    return render_template('user.html', name=session['userName'])

@app.route('/post/<int:postId>')
def showPost(postId) :
    return postId

@app.route('/')
def login_form() :
    return render_template('login_form.html')

@app.route('/login', methods=['POST'])
def login() :
    if request.method== 'POST' :
        session['userName']=request.form['userName']
        return redirect(url_for('showUserName'))
    else :
        return 'login failed'

    if __name__ == "__main__":
        app.run(host="127.0.0.1", port=8080)