from flask import Flask, redirect, url_for, render_template, request, session, flash, send_file
from datetime import timedelta
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os 
import tensorflow
import keras


#from views import views
#import numpy as np
#import pytorch as py


# This is a test to see if I can commit properly

app = Flask(__name__)
#app.register_blueprint(views, url_prefix='/views')
#secret key: way that we decrypt and encrypt data


app.config['SECRET_KEY'] = 'bobross'
app.config['UPLOAD_FOLDER'] = 'static/files'
app.secret_key = "bobross"
app.permanent_session_lifetime = timedelta(days=5)


def test():
    return 987



#Webpage #1
@app.route("/", methods=['GET', "POST"])
def home():
    if request.method == 'POST':
        
        if request.form.get("GetModel") == "MODEL":
            return redirect(url_for("about")) 
        
        # elif request.form.get("GetResults") == "RESULTS":
        #     return redirect(url_for("team"))

        
        elif request.form.get("About") == "ABOUT":
            return redirect(url_for("about"))
        
        # elif request.form.get("Home") == "HOME":
        #     about = request.form["Home"]
        #     session["home"] = about
        #     return redirect(url_for("logout"))
        
        
        elif request.form.get("Team") == "TEAM":
            return redirect(url_for("team"))

        elif request.form.get("Settings") == "SETTINGS":
            return redirect(url_for("settings"))
        
        elif request.files.getlist('files'):
            
            for f in request.files.getlist('files'):
                if f.filename:
                    f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
                else:
                    return render_template("home.html")
        
        else:
            return render_template("home.html")
    return render_template("home.html")
    
    
#For Downloading a file
@app.route('/download')
def download_file():
    p = "static/files/p2_rust2_error.png"
    return send_file(p, as_attachment=True)

        
        # get_request(request.form.get('action1'), request.form.get("About"), request.form.get("Home"), request.form.get("Team"), request.form.get("Settings"))
        
        


        #Set our session to be valid for a certain amount of time
        #even if you close webpage
        # session.permanent = True
        # user = request.form["nm"]
        # session["user"] = user
        # session["user2"] = 12
        # flash("Login Successful")
        #return redirect(url_for("user", usr=user, usr2=user2))
        # return redirect(url_for("user"))
    


    
@app.route("/about", methods=["POST", "GET"])
def about():

    if request.method == "POST":
        
        # if request.form.get('action1') == "RUN":
        #     # session.permanent = True
        #     user = request.form["action1"]
        #     session["user"] = user
        #     session["user2"] = "BOB"
        #     return redirect(url_for("user"))
        
        if request.form.get("About") == "ABOUT":
            about = request.form["About"]
            session["about"] = about
            return redirect(url_for("about"))
        
        elif request.form.get("Home") == "HOME":
            about = request.form["Home"]
            session["home"] = about
            return redirect(url_for("/"))
        
        
        elif request.form.get("Team") == "TEAM":
            about = request.form["Team"]
            session["team"] = about
            return redirect(url_for("team"))

        elif request.form.get("Settings") == "SETTINGS":
            about = request.form["Settings"]
            session["settings"] = about
            return redirect(url_for("settings"))

    else:
        #If user has already logged in and is in session
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("user"))
        return render_template("about.html", name="About")
    


@app.route("/settings", methods=["POST", "GET"])
def settings():

    if request.method == "POST":
        
        # if request.form.get('action1') == "RUN":
        #     # session.permanent = True
        #     user = request.form["action1"]
        #     session["user"] = user
        #     session["user2"] = "BOB"
        #     return redirect(url_for("user"))
        
        if request.form.get("About") == "ABOUT":
            about = request.form["About"]
            session["about"] = about
            return redirect(url_for("about"))
        
        elif request.form.get("Home") == "HOME":
            about = request.form["Home"]
            session["home"] = about
            return redirect(url_for("/"))
        
        
        elif request.form.get("Team") == "TEAM":
            about = request.form["Team"]
            session["team"] = about
            return redirect(url_for("team"))

        elif request.form.get("Settings") == "SETTINGS":
            about = request.form["Settings"]
            session["settings"] = about
            return redirect(url_for("settings"))

    else:
        #If user has already logged in and is in session
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("user"))
        return render_template("settings.html", name="Settings")


@app.route("/team", methods=["POST", "GET"])
def team():

    if request.method == "POST":
        
        # if request.form.get('action1') == "RUN":
        #     # session.permanent = True
        #     user = request.form["action1"]
        #     session["user"] = user
        #     session["user2"] = "BOB"
        #     return redirect(url_for("user"))
        
        if request.form.get("About") == "ABOUT":
            about = request.form["About"]
            session["about"] = about
            return redirect(url_for("about"))
        
        elif request.form.get("Home") == "HOME":
            about = request.form["Home"]
            session["home"] = about
            return redirect(url_for("/"))
        
        
        elif request.form.get("Team") == "TEAM":
            about = request.form["Team"]
            session["team"] = about
            return redirect(url_for("team"))

        elif request.form.get("Settings") == "SETTINGS":
            about = request.form["Settings"]
            session["settings"] = about
            return redirect(url_for("settings"))

    else:
        #If user has already logged in and is in session
        if "user" in session:
            flash("Already Logged in!")
            return redirect(url_for("user"))
        return render_template("team.html", name="Team")



#@app.route("/<usr>/<usr2>")
#def user(usr, usr2):
#    return f"<h1>{usr}</h1><h2>{usr2}</h2>"

#Page path ~/user
# @app.route("/user")
# def user():
#     #Check if the user was in session
#     if "user" in session:        
#         usr = test()
#         #usr = session["user"]
#         usr2 = session["user2"]
#         #return f"<h1>{usr}</h1><h2>{usr2}</h2>"
#         return render_template("user.html", user=usr, user2=usr2)

#     #Else if theres no user in my session
#     else:
#         flash("You are not logged in!")
#         return redirect(url_for("/"))

# @app.route("/logout")
# def logout():
#     #Only show you were logged out if you had been logged in
#     if "user" in session:
#         user = session["user"]
#         flash(f"You have logged out successfully {user}", "info")
#     session.pop("user", None)
#     return redirect(url_for("/"))

if __name__ == '__main__':
    app.run(debug=True)
    







#   {% with messages = get_flashed_messages() %}
#         {% if messages %}
#             {% for msg in messages %}
#                 <p>{{msg}}</p>
#             {% endfor %}
#         {% endif %}
