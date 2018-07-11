from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:blogblogblog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'Lm4YWvQ6jYMT'



posts = [
   {
       'title': 'First Blog Post! Hooray Me!', 
       'content': 'First blog app using Python, Flask and MYSQL', 
   }, 
   {
       'title': 'This is the second blog post',
       'content': 'blahblahblahblahblhablhablha'
   }
]


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    entry = db.Column(db.String(500))
   

    def __init__(self, name):
        self.name = name
        self.blog = blog



@app.route('/')
@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts)

@app.route('/newpost')
def newpost():

    if request.method == 'POST':
        blog_name = request.form['Name']
        db.session.add(blog_name)
        db.session.commit

    return render_template('newpost.html', title='Newpost')


if __name__ == '__main__':
    app.run()