from flask import Flask, render_template, url_for, redirect
from forms import RegistrationForm, LogInForm,AddForm

mob=Flask(__name__)

mob.config['SECRET_KEY']= '5465687987bbnu7365763hbskjhfb '

@mob.route('/')
@mob.route('/home')
def home():
        return render_template('home.html')

# @mob.route('/')
# def about():
#     return render_template('about.html', title ='title sent')

@mob.route('/signup')
def register():
    form = RegistrationForm()
    # if form.validate_on_submit ():
    #         flash(f 'Account created for {form.username.data}', 'success')
    #         return redirect(url_for('home'))
    return render_template('register.html', title = 'register', form =form)


@mob.route('/signin')
def signin():
    form = LogInForm()
    return render_template('signin.html', title = 'login', form =form)



@mob.route('/add')
def add():
        form = AddForm()
        return render_template('add.html', title = 'login',form =form)

@mob.route('/login')
def login():
        form =RegistrationForm()
        return render_template('login.html')


if __name__=='__main__':
    mob.run(debug=True)
