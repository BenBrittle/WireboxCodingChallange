from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

current_Question = ''

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
        if submitted_answer == current_Question.Correct_Answer:
            return 'correct'
    else:
        randomQuestion=[]
        AllQuestion = Question.query.order_by(Question.id).all()
        for x in AllQuestion:
            randomQuestion.append(x.id)
        
        questionvar = Question.query.get(random.choices(randomQuestion))
        current_Question = questionvar
        return render_template('Question.html', Question = questionvar)


@app.route('/addQuestion', methods=['POST','GET'])
def addQuestion():
    if request.method == 'POST':
        newQuestion = request.form['add question']
        newMultiAnswer = request.form['add all answers']
        newAnswer = request.form['add answer']
        newRow = Question(Question=newQuestion, Answers=newMultiAnswer, Correct_Answer=newAnswer)


        db.session.add(newRow)
        db.session.commit()
        return redirect('/viewQuestions')

    else:
        return render_template('backEnd.html')

@app.route('/viewQuestions')
def viewQuestions():
    questions = Question.query.order_by(Question.id).all()
    return render_template('viewQuestions.html', questions=questions)

@app.route('/delete/<int:id>')
def delete(id):
    Question_to_delete = Question.query.get_or_404(id)

    try:
        db.session.delete(Question_to_delete)
        db.session.commit()
        return redirect('/viewQuestions')

    except:
        return 'there was a problem deleting that question'

if __name__ == '__main__':
    app.run(debug=True)

