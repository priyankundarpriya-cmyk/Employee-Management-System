from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint("auth", _name_)

# Demo admin account
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = generate_password_hash("Admin@12345")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == ADMIN_USERNAME and check_password_hash(
            ADMIN_PASSWORD_HASH, password
        ):
            session["admin"] = username
            return redirect(url_for("employees.dashboard"))

        flash("Invalid username or password", "error")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("auth.login"))
