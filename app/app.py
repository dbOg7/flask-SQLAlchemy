from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Students.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))

    def __str__(self):
        return f'<Student {self.name}>'
   

@app.route('/')
def home():
    students = Students.query.all()
    return render_template('home.html', students=students)

if __name__ == '__main__':
   db.create_all()