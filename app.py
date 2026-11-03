from flask import Flask

app = Flask(_name_)

@app.route("/")
def home():
    return "<h1>Employee Management System</h1><p>Welcome to the Admin Dashboard!</p>"

if _name_ == "_main_":
    app.run(debug=True)
