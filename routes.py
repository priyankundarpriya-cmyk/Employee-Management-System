from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Employee

employee_bp = Blueprint("employees", _name_)


@employee_bp.route("/")
def dashboard():
    total_employees = Employee.query.count()
    total_departments = db.session.query(
        Employee.department
    ).distinct().count()

    return render_template(
        "dashboard.html",
        total_employees=total_employees,
        total_departments=total_departments
    )


@employee_bp.route("/employees")
def employee_list():
    employees = Employee.query.all()
    return render_template("employees.html", employees=employees)


@employee_bp.route("/employees/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        try:
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
            flash("Employee added successfully!", "success")
            return redirect(url_for("employees.employee_list"))

        except Exception:
            db.session.rollback()
            flash("Unable to add employee. Check the entered details.", "error")

    return render_template("add_employee.html")


@employee_bp.route("/employees/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):
    employee = Employee.query.get_or_404(id)

    if request.method == "POST":
        employee.name = request.form["name"]
        employee.email = request.form["email"]
        employee.department = request.form["department"]
        employee.designation = request.form["designation"]
        employee.salary = float(request.form["salary"])
        employee.phone = request.form.get("phone")

        db.session.commit()
        flash("Employee updated successfully!", "success")
        return redirect(url_for("employees.employee_list"))

    return render_template("edit_employee.html", employee=employee)


@employee_bp.route("/employees/delete/<int:id>", methods=["POST"])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)

    db.session.delete(employee)
    db.session.commit()

    flash("Employee deleted successfully!", "success")
    return redirect(url_for("employees.employee_list"))
