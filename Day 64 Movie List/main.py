from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
db= SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///movies.db"
db.init_app(app)
all_movie = []
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    year = db.Column(db.Integer)
    description= db.Column(db.String(200), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.String(200), nullable=False)
    review = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(250))
with app.app_context():
    db.create_all()




#with app.app_context():
    #new_movie = Movie(title="Phone Booth",
    #year=2002,
    #description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #rating=7.3,
    #ranking=10,
    #review="My favourite character was the caller.",
    #img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#)
#with app.app_context():
    #db.session.add(new_movie)
    #db.session.commit()

#with app.app_context():
    #second_movie = Movie(
    #title="Avatar The Way of Water",
    #year=2022,
    #description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #rating=4.3,
    #ranking=9,
    #review="I liked the water.",
    #img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#)
#with app.app_context():
    #db.session.add(second_movie)
    #db.session.commit()

with app.app_context():
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movie = result.scalars()

@app.route("/")
def home():
    return render_template("index.html", new_movie= Movie)



if __name__ == '__main__':
    app.run(debug=True, port=5002, host="127.0.0.1")
