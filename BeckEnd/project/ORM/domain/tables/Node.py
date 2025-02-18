from __future__ import annotations
from project.ORM.domain.i_dto import IDTO
from sqlalchemy import Column, Integer, ForeignKey
from typing import Dict, Any

from project import db

class Node(db.Model, IDTO):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    value = Column(Integer, unique=True)
    parent_id = Column(Integer, ForeignKey('node.id'))
    left_id = Column(Integer, ForeignKey('node.id'))
    right_id = Column(Integer, ForeignKey('node.id'))

    parent = db.relationship('Node', remote_side=[id], foreign_keys=[parent_id])
    left = db.relationship('Node', remote_side=[id], foreign_keys=[left_id])
    right = db.relationship('Node', remote_side=[id], foreign_keys=[right_id])

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'value': self.value,
            'parent': self.parent.put_into_dto() if self.parent else "root",
            'left': self.left.put_into_dto() if self.left else None,
            'right': self.right.put_into_dto() if self.right else None
        }

    
    @staticmethod
    def create_from_dto(value, parent_id=None) -> Node:
        return Node(value=value, parent_id=parent_id, left_id=None, right_id=None)
