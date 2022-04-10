import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_brixicals")
def get_brixicals():
    brixicals = mongo.db.brixicals.find()
    return render_template("brixicals.html", brixicals=brixicals)


@app.route("/search", methods=["GET","POST"])
def search():
    query = request.form.get("query")
    brixicals = mongo.db.brixicals.find({"$text":{"$search": query}})
    return render_template("brixicals.html", brixicals=brixicals)


@app.route("/register", methods=["GET", "POST"])
def register():
    if session["user"]:
        return redirect(url_for("get_brixicals"))

    if request.method == "POST":
        # check for existing Username
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash
                (request.form.get("password")),
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "email": request.form.get("email").lower(),
            "country": request.form.get("country").lower()
        }
        mongo.db.users.insert_one(register)

        #log the username in the session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("view_profile", username=session["user"]))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("user")!= None:
        return redirect(url_for("get_brixicals"))

    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "view_profile", username=session["user"]))
                
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
    
        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/view_profile/<username>")
def view_profile(username):
    # collect current users 'username' from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})
    if session["user"]:
        return render_template("view_profile.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove currently logged in user from cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_brixical", methods=["GET", "POST"])
def add_brixical():
    if request.method == "POST":
        upvotes = 0
        downvotes = 0
        brixical = {
            "brixword": request.form.get("brixword"),
            "definition": request.form.get("definition"),
            "upvotes": upvotes,
            "downvotes": downvotes,
            "imageUrl": request.form.get("imageUrl"),
            "created_by": session["user"]
        }
        mongo.db.brixicals.insert_one(brixical)
        flash("Brixicon Entry Successfully Added!")
        return redirect(url_for("get_brixicals"))

    return render_template("add_brixical.html")


@app.route("/edit_brixical/<brixical_id>", methods=["GET", "POST"])
def edit_brixical(brixical_id):
    if session.user!="admin":
        return redirect(url_for("get_brixicals"))

    if request.method == "POST":

        submit = {
            "brixword": request.form.get("brixword"),
            "definition": request.form.get("definition"),
            "imageUrl": request.form.get("imageUrl"),
        }
        mongo.db.brixicals.update_one({"_id": ObjectId(brixical_id)}, { "$set":submit})
        flash("Brixicon Entry Successfully Updated!")
        
    brixical = mongo.db.brixicals.find_one({"_id": ObjectId(brixical_id)})
    return render_template("edit_brixical.html", brixical=brixical)


@app.route("/delete_brixical/<brixical_id>")
def delete_brixical(brixical_id):
    mongo.db.brixicals.delete_one({"_id": ObjectId(brixical_id)})
    flash("Brixicon Entry Successfully Deleted")
    return redirect(url_for("get_brixicals"))


@app.route("/upvote_brixical/<brixical_id>/<upvotes>", methods=["GET", "POST"])
def upvote_brixical(brixical_id, upvotes):
    
    upvotes = int(upvotes) + 1
    upvotes = str(upvotes)
    submit = {
        "upvotes": upvotes
    }
    mongo.db.brixicals.update_one({"_id": ObjectId(brixical_id)}, { "$set":submit})
    flash("Thanks for the Upvote!")
    return redirect(url_for("get_brixicals"))


@app.route("/downvote_brixical/<brixical_id>/<downvotes>", methods=["GET", "POST"])
def downvote_brixical(brixical_id, downvotes):

    downvotes = int(downvotes) + 1
    downvotes = str(downvotes)
    submit = {
        "downvotes": downvotes
    }
    mongo.db.brixicals.update_one({"_id": ObjectId(brixical_id)}, { "$set":submit})
    flash("Thanks for the Downvote!")
    return redirect(url_for("get_brixicals"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=True)