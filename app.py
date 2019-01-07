
from flask import Flask, render_template
from config import Config
from forms import LoginForm


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
  return "<h1>Test</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
@app.route('/index')
def index():
    user = {'username': 'Ciaran'}
    return render_template('index.html', title='Home', user=user)
if __name__ =="__main__":
  app.run(debug=True,port=5000)

