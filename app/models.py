from flask_appbuilder import Model
from sqlalchemy import Column, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from dataclasses import dataclass

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""
@dataclass
class Coefficient(Model):
    __tablename__ = 'coefficient'
    name: str
    value: Numeric

    name = Column(String(), primary_key=True)
    value = Column(Numeric())