from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(200))
    Answer1 = db.Column(db.String(200))
    Answer2 = db.Column(db.String(200))
    Answer3 = db.Column(db.String(200))
    Answer4 = db.Column(db.String(200))
    Correct_Answer = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def index():
    return render_template('mainBody.html')

@app.route('/question')
def question():
    return render_template('Question.html')

if __name__ == '__main__':
    app.run(debug=True)

