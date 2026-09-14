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
import random
import string


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page
#-----------------------------------------------------------
@app.get("/")
def home_page():
        if session.get("logged_in"):
            with connect_db() as db:
                sql = """
                    SELECT * FROM users WHERE id=?
                """
                params = (session["user"]["id"],)

                user = db.execute(sql,params).fetchone()

                sql = """
                    SELECT * FROM moves WHERE user_id=?
                """
                params = (session["user"]["id"],)
                
                moves = db.execute(sql,params).fetchall()
                
                return render_template("pages/home.jinja", user=user, moves=moves)
        else:
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
        return redirect("/")


#-----------------------------------------------------------
# Log in route
#-----------------------------------------------------------
@app.post("/login")
def log_in_route():
    username = request.form.get('name', '').strip()
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
            return redirect("/login_form")

        if not check_password_hash(user["pass_hash"], password):
            flash(f"Incorrect password", "error")
            return redirect("/login_form")

        session["logged_in"] = True
        session["user"] = {
            "id":       user["id"],
            "name": user["name"]
        }

        flash("Login successful", "success")
        return redirect("/")


#-----------------------------------------------------------
# Log out route
#-----------------------------------------------------------
@app.get("/logout")
def logout_user():
    session.clear()
    flash(f"You have been logged out", "success")
    return redirect("/")

#-----------------------------------------------------------
# Joining a move route
#-----------------------------------------------------------
@app.post("/join")
def join():
    move_code = request.form.get('code','')
    with connect_db() as db:
        sql = """
            SELECT * FROM moves WHERE move_code=?
        """
        params = (move_code,)
        move = db.execute(sql, params).fetchone()
        if not move:
            flash(f"Incorrect code", "error")
            return redirect("/")
        else:
            return redirect(f"/move/{move[0]}")


#-----------------------------------------------------------
# Move page
#-----------------------------------------------------------
@app.get("/move/<int:id>")
def move(id):
    with connect_db() as db:
        sql = """
            SELECT * FROM moves WHERE id=? 
        """
        params = (id,)
        move = db.execute(sql, params).fetchone()
        sql = """
            SELECT * FROM boxes WHERE move_id=?
        """
        boxes = db.execute(sql, params).fetchall()
        return render_template("pages/move.jinja", move=move, boxes=boxes)

#-----------------------------------------------------------
# Generate new code
#-----------------------------------------------------------
@app.get("/new_code/<int:id>")
def new_code(id):
    with connect_db() as db:
        code = ""
        for _ in range[8]:
            code.join(random.choice(string.ascii_letters + string.digits + string.punctuation))
        sql = """
            INSERT INTO moves (move_code) WHERE id=? VALUES (?)
        """
        params = (id, code)

        db.execute(sql,params)
        return redirect(f"/move/{id}")

#-----------------------------------------------------------
# Weird page
#-----------------------------------------------------------
@app.get("/weird")
def weird_route():
    return render_template("pages/weird.html")


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

