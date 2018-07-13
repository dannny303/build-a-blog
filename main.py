from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://buildablog:myfirstblog@localhost:8889/buildablog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'Lm4YWvQ6jYMT'



class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    content = db.Column(db.Text(500))
   
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
@app.route('/')
@app.route('/blog', methods=['POST', 'GET'])
def index():

    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs)

@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        newpost = Blog(title, content)
        db.session.add(newpost)
        db.session.commit()

        return redirect('/individ?id=' + str(newpost.id))
    
    return render_template('newpost.html', title='Newpost')


@app.route('/individ', methods=['POST', 'GET'])
def individ():

    
    blog_id = request.args.get("id")
    blog = Blog.query.filter_by(id=blog_id).first()
    return render_template('individ.html', blog=blog) 

if __name__ == '__main__':
    app.run()