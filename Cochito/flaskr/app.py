import os

from flask import Flask, render_template, request, session
from flask_session import Session

#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/home", methods=["POST"])
def home():
    username = request.form.get("username") # take the request the user made, access the form,
                                            # and store the field called `username` in a Python variable also called `name`
    return render_template("home.html", username=username)

@app.route("/taste")
def taste():
    return render_template("first_time_form.html")

if __name__ == "__main__":
    app.run(debug=True)
