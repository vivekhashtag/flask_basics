from flask import Flask, request,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)


app.config.update(
    SECRET_KEY ='topsecret',
    SQLALCHEMY_DATABASE_URI ="postgresql://postgres:vivek@localhost/catalog_db",
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
def hello_flask():
    return'Hello Flask!'

#text

@app.route('/user')
@app.route('/user/<name>/<name2>')
def no_query_string(name="mina", name2="yes"):
    return '<h1> Hello There! {} {} </h1>'.format(name ,name2)
#numbers
@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> Yes the number you picked is '+str(num)+ '</h1>'

@app.route('/add/<int:num1>/<int:num2>')
def addition_of_numbers(num1,num2):
    return'<h1> The Sum is {} </h1>'.format(num1+num2)


@app.route('/product/<float:num1>/<float:num2>')
def product_of_numbers(num1,num2):
    return'<h1> The Sum is {} </h1>'.format(num1*num2)

#templates
@app.route('/temp')

def using_templates():

    movies_list =['Robot' ,
                  'Kabali',
                  'Sivaji',
                   '2.0'
                  ]
    return render_template('hello.html',
                           movies=movies_list,
                           name='Vivek')

#tables
@app.route('/table')

def using_tables():

    movies_list ={'Robot' : 1.5,
                  'Kabali' :1.8,
                  'Sivaji':2.3,
                   '2.0' :3
    }
    return render_template('tabledata.html',
                           movies=movies_list,
                           name='Vivek')


class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(80), nullable = False)

    def __init__(self, name):

        self.name=name

    def __repr__(self):
        return 'The Publisher is {}'.format(self.name)

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)