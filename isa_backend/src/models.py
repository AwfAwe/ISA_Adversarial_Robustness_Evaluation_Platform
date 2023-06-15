from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class AImodel(db.Model):
    __tablename__ = 'aimodel'
    aimodel_id = db.Column(db.Integer, primary_key=True)
    aiModel_name = db.Column(db.String(128), nullable=False)
    aimodel_model = db.Column(db.String(128))

class Image(db.Model):
    __tablename__ = 'image'
    image_id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(128), nullable=False)
    image_model = db.Column(db.String(128))
    AImodel = db.relationship('AImodel', primaryjoin='AImodel.aimodel_id == Image.image_id')

