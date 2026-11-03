from flask import Flask
from models import db
from routes import employee_bp

app = Flask(_name_)

app.config["SECRET_KEY"] = "change-this-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:password@localhost/employee_db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(employee_bp)

with app.app_context():
    db.create_all()

if _name_ == "_main_":
    app.run(debug=True)
