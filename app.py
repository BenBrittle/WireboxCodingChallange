from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Question = db.Column(db.String(200))
    Answers = db.Column(db.String(300))
    Correct_Answer = db.Column(db.Integer)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST','GET'])
def index():
    return render_template('mainBody.html')

@app.route('/question', methods=['POST', 'GET'])
def question():
    return render_template('Question.html')

if __name__ == '__main__':
    app.run(debug=True)

