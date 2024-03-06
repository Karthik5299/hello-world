from flask import Flask , redirect,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)
# @app.route('/admin')
# def hello_admin():
#     return "HELLO ADMIN"
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return"HELLO %s"%guest
# @app.route('/user/<name>')
# def hello_user(name):
#     if name=='admin':
#         return  redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest',guest=name))
# @app.route('/app')
# def hello():
#     return "HELLO"
#@app.route("/")
#def home():
   # return render_template("index.html")
# @app.route('/hello/<name>')
# def hello_name(name):
#     return f'HELLO{Name}'
# @app.route("/home")
# def fun():
#     addition = 10+100
#     return render_template( "home.html",result = addition)
# if __name__=='__main__':
#     app.run(debug=True)
# #----------------------------------------------------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.db'
# Suppresses warning while tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

# sample_data = [{"id":1,'name': 'John', 'age': 25},
# {"id":2,'name': 'Alice', 'age': 30},
# {"id":3,'name': 'Bob', 'age': 22}]

sample_data = [{'name': 'John', 'age': 25},
{'name': 'Alice', 'age': 30},
{'name': 'Bob', 'age': 22}]

with app.app_context():
    db.drop_all()
    db.create_all()

    for entry in sample_data:
        obj =  Person(name = "entry['name']",age = entry['age'])
        db.session.add(obj)
    db.session.commit()

@app.route("/")
def display_data():
    data = Person.query.all()

    return render_template('person.html',people = data)

if __name__ == "__main__":
    app.run(debug=True)  # This line of code is added in this section