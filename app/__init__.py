#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all notes
#-----------------------------------------------------------
@app.get("/")
def home_page():
        return render_template("pages/home.jinja")

#-----------------------------------------------------------
# Sign up page
#-----------------------------------------------------------
@app.get("/signup_form")
def sign_up_page():
    return render_template("pages/signup_form.jinja")



#-----------------------------------------------------------
# Log in page
#-----------------------------------------------------------
@app.get("/login_form")
def log_in_page():
    return render_template("pages/login_form.jinja")


#-----------------------------------------------------------
# Sign up route
#-----------------------------------------------------------
@app.post("/signup")
def sign_up_route():
    with connect_db() as db:
        name = html.escape(request.form.get('name','').strip())
        pass_hash = generate_password_hash(html.escape(request.form.get('password','').strip()))
        sql = """
            INSERT INTO users (name, pass_hash)
            VALUES (?, ?)
        """
        params = (name, pass_hash)
        db.execute(sql, params)
        return render_template("/")
    

#-----------------------------------------------------------
# Log in route
#-----------------------------------------------------------
@app.post("/login")
def log_in_route():
    username = request.form.get('name', '').strip().lower()
    password = request.form.get('password', '').strip()

    with connect_db() as db:
        sql = """
            SELECT id, name, pass_hash
            FROM users
            WHERE name=?
        """
        params = (username,)
        user = db.execute(sql, params).fetchone()

        if not user:
            flash(f"Unknown user", "error")
            return redirect("/login")

        if not check_password_hash(user["pass_hash"], password):
            flash(f"Incorrect password", "error")
            return redirect("/login")

        session["logged_in"] = True
        session["user"] = {
            "id":       user["id"],
            "name": user["name"]
        }

        flash("Login successful", "success")
        return redirect("/")
    

#-----------------------------------------------------------
# Weird page
#-----------------------------------------------------------
@app.get("/weird")
def weird_route():
    return redirect("pages/weird.html")


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

