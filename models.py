from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Survey(db.Model):
    __tablename__ = "surveys"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(120))
    feedback = db.Column(db.Text)

    def __init__(self,name,email,feedback):
        self.name = name
        self.email = email
        self.feedback = feedback