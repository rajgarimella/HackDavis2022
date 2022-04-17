from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os 


#make button work
#upload folder

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bobross'
app.config['UPLOAD_FOLDER'] = 'static/files'

app.permanent_session_lifetime = timedelta(days=5)


#Webpage #1
@app.route("/", methods=['GET', "POST"])
def home():
    if request.method == 'POST':
        for f in request.files.getlist('files'):

            print(f)
            f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            #f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return render_template("home.html")
    return render_template("home.html")

#For Downloading a file
@app.route('/download')
def download_file():
    p = "static/files/P1rust_error.png"
    return send_file(p, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


