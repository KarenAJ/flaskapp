completion = validate(username,password)
        if completion ==False:
            return render_template('login.html', msg="invalid")
        if completion == True:
            return ("Successfully logged in!")
        if completion == -1:
            return redirect('/signup')
    else:
     return render_template('login.html')



"""
    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
"""

#POST_USERNAME = str(request.form['username'])
#POST_PASSWORD = str(request.form['password'])

#print ("Logged in User is", POST_USERNAME, "Password is", POST_PASSWORD )
