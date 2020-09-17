from app.main import db
from app.main.models.base_model import BaseModel

class ClientModel(BaseModel):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dni = db.Column(db.Numeric(8,0), nullable=False)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    phone = db.Column(db.Integer)
