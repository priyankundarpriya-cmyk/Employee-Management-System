from flask import Flask
from config import Config
from models import db
from routes import employee_bp
from auth import auth_bp

app = Flask(_name_)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(employee_bp)
app.register_blueprint(auth_bp)

with app.app_context():
    db.create_all()

if _name_ == "_main_":
    app.run(debug=True)
