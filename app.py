from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', greeting='Hello, Flask!', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

