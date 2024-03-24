from flask import Flask, render_template, send_from_directory, request, redirect, session, url_for
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import bcrypt
# import os

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'

# user_marks = db.Table('user_marks',
#     db.Column('user_id',db.Integer,db.Foreign_key('user_id')),
#     db.Column('marks_id',db.Integer,db.Foreign_key('marks_id'))
# )

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    # score = db.Column(db.Integer, 0)
    user_score = db.relationship('Quiz',backref='user')

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

class Quiz(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    # name = db.Column(db.String(100), nullable=True)
    # email = db.Column(db.String(100), unique=True)
    quiz_type = db.Column(db.String)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __init__(self,quiz_type,score,user_id):
        # self.name = name
        # self.email = email
        self.quiz_type = quiz_type
        self.score = score
        self.user_id = user_id
        # new_score = Marks(name=name,email=email,quiz_type=quiz_type,ai_score=ai_score)
        # db.session.add(new_score)
        # db.session.commit()




ai_correct_answers = {
    'question-87518975480':'radio0002',
    'question-87518975481':'radio0006',
    'question-87518975482':'radio0011',
    'question-87518975483':'radio0015',
    'question-87518975484':'radio0019',
    'question-87518975485':'radio0023',
    'question-87518975486':'radio0026',
    'question-87518975487':'radio0031',
    'question-87518975488':'radio0034',
    'question-87518975489':'radio0039',
    'question-87518975490':'radio0043',
    'question-87518975491':'radio0048',
    'question-87518975492':'radio0051',
    'question-87518975493':'radio0055',
    'question-87518975494':'radio0058',
}

ml_correct_answers = {
    'question-77518975480':'radio1001',
    'question-77518975481':'radio1008',
    'question-77518975482':'radio1009',
    'question-77518975483':'radio1016',
    'question-77518975484':'radio1020',
    'question-77518975485':'radio1023',
    'question-77518975486':'radio1028',
    'question-77518975487':'radio1030',
    'question-77518975488':'radio1036',
    'question-77518975489':'radio1038',
    'question-77518975490':'radio1043',
    'question-77518975491':'radio1045',
    'question-77518975492':'radio1049',
    'question-77518975493':'radio1054',
    'question-77518975494':'radio1059',
}

ds_correct_answers = {
    'question-67518975480':'radio2002',
    'question-67518975481':'radio2006',
    'question-67518975482':'radio2011',
    'question-67518975483':'radio2013',
    'question-67518975484':'radio2017',
    'question-67518975485':'radio2021',
    'question-67518975486':'radio2026',
    'question-67518975487':'radio2032',
    'question-67518975488':'radio2035',
    'question-67518975489':'radio2039',
    'question-67518975490':'radio2042',
    'question-67518975491':'radio2046',
    'question-67518975492':'radio2050',
    'question-67518975493':'radio2055',
    'question-67518975494':'radio2059',
}

ba_correct_answers = {
    'question-57518975480':'radio3002',
    'question-57518975481':'radio3007',
    'question-57518975482':'radio3009',
    'question-57518975483':'radio3015',
    'question-57518975484':'radio3018',
    'question-57518975485':'radio3022',
    'question-57518975486':'radio3026',
    'question-57518975487':'radio3030',
    'question-57518975488':'radio3034',
    'question-57518975489':'radio3038',
    'question-57518975490':'radio3042',
    'question-57518975491':'radio3047',
    'question-57518975492':'radio3049',
    'question-57518975493':'radio3054',
    'question-57518975494':'radio3060',
}











with app.app_context():
    db.create_all()


@app.route("/")

def index():
    # logged_in = 'email' in session
    # if logged_in:
    #     return send_from_directory('../src/pages','home.html?logged_in=True')
    # else:
    #     return send_from_directory('../src/pages','home.html?logged_in=False')
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('home.html', user=user, logged_in=True, email=session['email'])
    return render_template('home.html', logged_in=False)


@app.route('/aiquiz', methods=['GET','POST'])

def aiquiz():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        
        if request.method == 'POST':
            # quiz_type = 'AI'
            score = ai_calculate_score(request.form)
            session['latest_score'] = score
            session['type_quiz'] = 'AI'
            # print("Latest session (AI):", session['type_quiz'])

            user_id = user.id
            quiz = Quiz(quiz_type='AI', user_id=user_id, score=score)
            db.session.add(quiz)
            db.session.commit()
            # new_score = Marks(name=session['name'],email=session['email'],quiz_type=typequiz,ai_score=score,user_id=user.id)
            # db.session.add(new_score)
            # db.session.commit()

            return redirect(url_for('dashboard', user_id=user_id))
        
        return render_template('aiform.html',user=user)

    return redirect('/login')


def ai_calculate_score(user_answers):
    score = 0
    for question, answer in user_answers.items():
        if answer == ai_correct_answers.get(question):
            score += 1
    return score




@app.route('/mlquiz', methods=['GET','POST'])

def mlquiz():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        
        if request.method == 'POST':
            # quiz_type = 'ML'
            score = ml_calculate_score(request.form)
            session['latest_score'] = score
            session['type_quiz'] = 'ML'
            # print("Latest session (ML):", session['type_quiz'])

            user_id = user.id
            quiz = Quiz(quiz_type='ML', user_id=user_id, score=score)
            db.session.add(quiz)
            db.session.commit()
            # new_score = Marks(name=session['name'],email=session['email'],quiz_type=typequiz,ai_score=score,user_id=user.id)
            # db.session.add(new_score)
            # db.session.commit()

            return redirect(url_for('dashboard', user_id=user_id))
        
        return render_template('mlform.html',user=user)

    return redirect('/login')

def ml_calculate_score(user_answers):
    score = 0
    for question, answer in user_answers.items():
        if answer == ml_correct_answers.get(question):
            score += 1
    return score





@app.route('/dsquiz', methods=['GET','POST'])

def dsquiz():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        
        if request.method == 'POST':
            # quiz_type = 'DS'
            score = ds_calculate_score(request.form)
            session['latest_score'] = score
            session['type_quiz'] = 'DS'
            # print("Latest session (DS):", session['type_quiz'])

            user_id = user.id
            quiz = Quiz(quiz_type='DS', user_id=user_id, score=score)
            db.session.add(quiz)
            db.session.commit()
            # new_score = Marks(name=session['name'],email=session['email'],quiz_type=typequiz,ai_score=score,user_id=user.id)
            # db.session.add(new_score)
            # db.session.commit()

            return redirect(url_for('dashboard', user_id=user_id))
        
        return render_template('dsform.html',user=user)

    return redirect('/login')

def ds_calculate_score(user_answers):
    score = 0
    for question, answer in user_answers.items():
        if answer == ds_correct_answers.get(question):
            score += 1
    return score

@app.route('/baquiz', methods=['GET','POST'])

def baquiz():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        
        if request.method == 'POST':
            # quiz_type = 'BA'
            score = ba_calculate_score(request.form)
            session['latest_score'] = score
            session['type_quiz'] = 'BA'
            # print("Latest session (BA):", session['type_quiz'])

            user_id = user.id
            quiz = Quiz(quiz_type='BA', user_id=user_id, score=score)
            db.session.add(quiz)
            db.session.commit()
            # new_score = Marks(name=session['name'],email=session['email'],quiz_type=typequiz,ai_score=score,user_id=user.id)
            # db.session.add(new_score)
            # db.session.commit()

            return redirect(url_for('dashboard', user_id=user_id))
        
        return render_template('baform.html',user=user)

    return redirect('/login')

def ba_calculate_score(user_answers):
    score = 0
    for question, answer in user_answers.items():
        if answer == ba_correct_answers.get(question):
            score += 1
    return score







@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('../src/pages', filename)

app.template_folder = '../src/pages'

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    # return send_from_directory('../src/pages','register.html')
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            # return redirect('/')
            return redirect(url_for('dashboard', user_id=user.id))
        else:
            # return send_from_directory('../src/pages','login.html',error='Invalid user')
            return render_template('login.html',error='Invalid user')
    # return send_from_directory('../src/pages','login.html')
    return render_template('login.html')

# @app.route('/dashboard')
# def dashboard():
#     if session['email']:
#         user = User.query.filter_by(email=session['email']).first()
#         # if user:
#         #     marks = Marks.query.filter_by(user_id=user.id).all()
#         #     return render_template('dashboard.html',user=user,marks=marks)
#         if request.method == 'POST':
#             new_score = ai_calculate_score(request.form)
#             session['score'] = new_score
#             return render_template('dashboard.html',user=user,new_score=new_score)
        
#         new_score = session['score']
#         return render_template('dashboard.html',user=user,new_score=new_score)
#     else:
#         return redirect('/login')

@app.route('/dashboard/<int:user_id>')
def dashboard(user_id):
    user = User.query.get_or_404(user_id)
    # quiz = Quiz.query.filter_by(user_id=user_id).first()
    # return render_template('dashboard.html', user=user,quiz=quiz)
    ai_quiz_score = Quiz.query.filter_by(user_id=user_id, quiz_type='AI').first()
    ml_quiz_score = Quiz.query.filter_by(user_id=user_id, quiz_type='ML').first()
    ds_quiz_score = Quiz.query.filter_by(user_id=user_id, quiz_type='DS').first()
    ba_quiz_score = Quiz.query.filter_by(user_id=user_id, quiz_type='BA').first()
    latest_score = session.get('latest_score')
    score = str(latest_score)
    latest_quiz_type = session.get('type_quiz')
    quiztype = str(latest_quiz_type)
    # print("Latest score (Dashboard):", score)
    # print("Latest session (Dashboard):", latest_quiz_type)
    return render_template('dashboard.html', user=user, score=score, latest_quiz_type=latest_quiz_type, ai_quiz_score=ai_quiz_score, ml_quiz_score=ml_quiz_score, ds_quiz_score=ds_quiz_score, ba_quiz_score=ba_quiz_score)

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('login')


if __name__=="__main__":
    app.run(debug=True)

