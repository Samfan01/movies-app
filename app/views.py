from flask import Flask, render_template,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from app import app
from passlib.hash import sha256_crypt

engine = create_engine('mysql+pymysql://root:user@localhost/subscription')

db=scoped_session(sessionmaker(bind=engine))

#Views
@app.route('/')
def home():
    '''
    View root page function that returns the index page
    and its data
    '''
    title = 'Movie app by us'
    return render_template('home.html',title= title)

#subscription
@app.route('/subscription', methods =['GET','POST'])
def subscription():
    if request.method =='POST':
        name = request.form.get('name')
        username = request.get('username')
        password = request.get('password')
        confirm = request.get('confirm')
        secure_password = sha256_crypt.encrypt(str(password))


        if password == confirm:
            db.execute("INSERT INTO users(name, username, password) VALUES(:name,:username,:password)",
                                        {"name":name, "username":username,"password":secure_password})
            db.commit()
            flash("you hve subscribed and can add profile", "success")
            return redirect(url_for('profile')) 
        else:
            flash("password does not match", "danger")
            return render_template("subscription.html")                                


    return render_template('subscription.html')



#add profile

@app.route('/profile')
def profile():
    return render_template('profile.html')


if __name__ == "__main__":
    app.secret_key="kizito"
    app.run(degug=True)

