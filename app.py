from flask import Flask, render_template,request,session,logging,url_for,redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from app import app
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/')
def index():
    '''
    View root page function that returns the index page
    and its data
    '''
    title = 'Movie app by us'
    return render_template('home.html',title= title)
# #subscription form

@app.route('/subscription')
def subscription():
    return render_template('subscription.html')

if __name__ =="__main__":
    app.run(debug=True)