from flask import Flask, render_template, request
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


@app.route('/')
def index():
    return render_template('mainBody.html')

@app.route('/question', methods=['POST','GET'])
def question():
    if request.method == 'POST':
        submitted_answer = request.form['answer']
        return submitted_answer
    else:
        questionvar = Question.query.get(0)
        return render_template('Question.html', Question = questionvar)

@app.route('/backend', methods=['POST','GET'])
def backEnd():
    if request.method == 'POST':
        newQuestion = request.form['add question']
        newMultiAnswer = request.form['AllAnswers']
        newAnswer = request.form['answer']
        print(newAnswer, newMultiAnswer, newQuestion)
    else:
        return render_template('backEnd.html')


if __name__ == '__main__':
    app.run(debug=True)

