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
          
