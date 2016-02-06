from flask import render_template, url_for, redirect, request, jsonify, session
from gdg_flask import app, db
from gdg_flask.forms import UserRegisterForm
from werkzeug.security import generate_password_hash

from .models import UserDB


@app.route('/')
def home():
    return render_template("gdg-article/home.html")


# URL Prefix '/about' is
# about ourselves(gdg-ssu)
# So, if you want to make URL and template resource about GDG-SSU
# You have to post url Prefix '/about' and template resource path to '/templates/gdg-article/about/*'
@app.route('/about')
@app.route('/about/intro')
def about_intro():
    return render_template('gdg-article/about/intro.html')


@app.route('/about/members')
def about_members():
    return render_template('gdg-article/about/members.html')


@app.route('/about/activities')
def about_activities():
    return render_template('gdg-article/about/activities.html')


@app.route('/about/recruits')
def about_recruits():
    return render_template('gdg-article/about/recruits.html')


# URL Prefix '/account' is
# about User Account (login, logout, register.. and so on)
# So, if you want to make URL and template resource about User Account
# You have to post url Prefix '/account' and template resource path to '/templates/gdg-article/account/*'

@app.route('/account/register', methods=['GET', 'POST'])
def account_register():
    form = UserRegisterForm()
    script_list = ["js/account/register.js"]
    if request.method == 'POST' and form.validate():
        user_id = form.user_id.data
        password = form.password.data
        user = UserDB(
            user_id=user_id,
            user_pw=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        session['user_id']=user_id
        session['permission']=user.permission

    return render_template('gdg-article/account/register.html', form=form, script_list=script_list)


@app.route('/account/login')
def account_login():
    form = UserLoginForm()

    return render_template('gdg-article/account/login.html')


@app.route('/account/logout')
def account_logout():
    return redirect(url_for('home'))


@app.route('/account/check/field')
def account_registerForm_check():
    form = UserRegisterForm()

    field_id = request.args.get('field_id')
    field_value = request.args.get('field_value')

    field_bind_id = request.args.get('field_bind_id')
    field_bind_value = request.args.get('field_bind_value')

    if field_bind_id and field_bind_value:
        form[field_bind_id].data = field_bind_value

    form[field_id].data = field_value

    result = form[field_id].validate(form)
    # 만족시 True
    # Boolean

    return jsonify(result=result)


@app.route('/helper')
def helper():
    return render_template("gdg-article/help-desk/gdg-ssu-help.html")


@app.route('/test')
def test():
    user = UserDB(user_id='youdskaj', user_pw='textpw1212')
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/test12')
def test12():
    user = UserDB.query.all()
    # print(user)
    # print(user[0].user_id)

    return render_template("gdg-article/help-desk/temp_test.html", test_db=user)


@app.route('/tempform', methods=['GET', 'POST'])
def tempForm():
    form = UserRegisterForm()
    if request.method == 'POST' and form.validate():
        print('forms ok')
    else:
        print('forms no')

    return render_template("gdg-article/help-desk/temp_form.html", form=form)

# @app.route('/temp12')
# def temp12():
#     return render_template("base/layout.html")
