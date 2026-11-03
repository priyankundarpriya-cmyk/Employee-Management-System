from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Employee

employee_bp = Blueprint("employees", _name_)

@employee_bp.route("/employees")
def employee_list():
    employees = Employee.query.all()
    return render_template("employees.html", employees=employees)

@employee_bp.route("/employees/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        employee = Employee(
            name=request.form["name"],
            email=request.form["email"],
            department=request.form["department"],
            designation=request.form["designation"],
            salary=float(request.form["salary"]),
            phone=request.form.get("phone")
        )
        db.session.add(employee)
        db.session.commit()
        flash("Employee added successfully!")
        return redirect(url_for("employees.employee_list"))

    return render_template("add_employee.html")
