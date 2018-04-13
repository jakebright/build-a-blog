from flask import Flask, request, redirect, render_template, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:launchcode@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

app.secret_key = 'jakebright' 


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)

    def __init__(self, title, body):
        self.title = title
        self.body = body



@app.route('/blog', methods=['POST', 'GET'])
def display_all_posts():
    #import pdb; pdb.set_trace()
    if request.method == 'POST':
        blog = Blog(request.form['title'], request.form['body'])
        db.session.add(blog)
        db.session.commit()

        return redirect('/blog')

    if request.method == 'GET':
        blogs = Blog.query.all()
        
        return render_template('blog.html', title='build-a-blog', blogs=blogs)
  

@app.route('/add_post', methods=['GET'])
def add_post():  
    #if request.method == 'POST':
     #   title = request.form['title']
      #  body = request.form['body']
       # blog = Blog(title, body)
        #db.session.add(blog)
        #db.session.commit()


    return render_template('newpost.html')

@app.route('/newpost', methods=['POST'])
def new_post():
    

    return redirect('/')

@app.route('/', methods =['POST' , 'GET'])
def index():
    return redirect('/blog')


if __name__ == '__main__':
    app.run()

