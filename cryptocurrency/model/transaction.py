from cryptocurrency import db
from sqlalchemy import Enum
import enum
from sqlalchemy.orm import relationship


class TransactionType(enum.Enum):
    BUY = "BUY"
    SELL = "SELL"


class Transactions(db.Model):
    __tablename__ = 'transactions'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('public.users.id'), nullable=False)
    cryptocurrency = db.Column(db.String(128), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(Enum(TransactionType), nullable=False)
    transaction_price = db.Column(db.Float, nullable=False)
    transaction_date = db.Column(db.DateTime, server_default=db.func.GETUTCDATE(), nullable=False)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



