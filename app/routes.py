from werkzeug.wrappers import request
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect

@app.route("/", methods=['GET', 'POST'])
def index():
    print("index")
    form = LoginForm()
    return render_template("/login.html", title="Sign In", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("a")
        flash("Login requested for email {}".format(form.email.data))
        return render_template("/temp.html")
    return render_template("/login.html", title="Sign In", form=form)



