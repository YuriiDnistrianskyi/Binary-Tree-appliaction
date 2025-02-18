from project.ORM.service import node_service
from flask import abort
from http import HTTPStatus
from project.ORM.domain import Node

class NodeController:
    def find_all(self) -> list[Node]:
        return node_service.find_all()
    
    
    def find_by_id(self, id: int) -> Node:
        return node_service.find_by_id(id)

    
    def find_by_data(self, data: int) -> Node:
        return node_service.find_by_data(data)
    
    
    def add_node(self, data: int) -> None:
        if data is None or type(data) is not int:
            abort(HTTPStatus.BAD_REQUEST, f"Bad data")
        node_service.add(data)
        

    def delete_node(self, data: int) -> None:
        result = node_service.delete(data)
        if result is False:
            abort(HTTPStatus.NOT_FOUND, f"Node not found")
        
        
    def get_tree(self) -> str:
        return node_service.get_tree()
