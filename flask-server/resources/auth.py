from server import app


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


@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('login')
