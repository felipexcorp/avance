from sqlalchemy import Column, String
from .entity import Entity, Base

#from .entity     import Entity, Base


class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String(50))
    description = Column(String(50))

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description
"""
# coding=utf-8

from marshmallow import Schema, fields

# ... other import statements ...

# ... Exam class definition ...

class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()
"""