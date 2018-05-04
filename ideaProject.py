from flask import Flask,url_for
from flask import request
from flask import render_template,redirect,flash
from form import LoginForm
from config import *
from flask import make_response
from model.User import User
from form import *
from flask import abort

app = Flask(__name__)

@app.route('/ttttt')
def hello_world():
    user_agent=request.headers.get('User-Agent')
    print user_agent
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    #read cookie
    #username=request.cookies.get('username')
    #store cookie
    #resp=make_response(render_template())
    #resp.set_cookie('username')
    abort(404)
    return redirect('http://www.baidu.com')


@app.route('/')
def test():
    return render_template('base.html')

@app.route('/test/<username>/<int:number>/')
def show_user(username,number):
    u=User(username)
    u.passwd='123456'

    return 'welcome No:%d user %s'%(number,username)
@app.route('/<user>')
def users(user):
    mydict = {"key": "To Be or Not To Be"}
    mylist = ['it', 'is', 'a', 'problem']
    myintvar = 0

    return render_template('users.html',name=user,mydict=mydict,mylist=mylist,myintvar=myintvar)
@app.route('/flow/<user>')
def flow(user):
    comm=['this','is','a','problem']
    return render_template('flow.html', user=user,comments=comm)

@app.route('/test/login',methods=['GET','POST'])
def login():
    form=LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(name=request.form['username']).first()
            if user is not None (user.password, request.form['password']):
                pass
                flash('You were logged in. Go Crazy.')
                return redirect(url_for('home.home'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error)

@app.route('/test/page')
def show_page():
    return render_template('hello.html')

@app.route('/test/<name>')
def show_name(name):
    return render_template('test.html',name=name)

@app.route('/test/url')
def show_url():
    url=url_for('show_page')
    return 'url is %s'%(url)

@app.route('/get/',methods=['GET','POST'])
def makelogin():
    name=request.args.get('name')
    passwd=request.args.get('passwd')

@app.route('/friend/<friends>')
def get_friend(friends):
    return render_template('friend.html',friend=friends)

@app.route('/friend/')
def home_friend():
    return render_template('friend.html')

@app.route('/match/')
def match():
    return render_template('match.html')

@app.route('/help/')
def help():
    return render_template('help.html')





if __name__ == '__main__':
    app.debug=True #debug mode
    with app.test_request_context():
        print url_for('test')
    app.config.from_object('config')
    app.run()

