from project.ORM.dao import node_dao
from project.ORM.domain import Node


class NodeService:
    def find_all(self) -> list[Node]:
        return node_dao.find_all()
    
    
    def find_by_id(self, id: int) -> Node:
        return node_dao.find_by_id(id)
    
    
    def find_by_data(self, data: int) -> Node:
        return node_dao.find_by_data(data)
    
    
    def add(self, data: int) -> None:
        node_dao.add(data)
        
    
    def delete(self, data: int) -> bool:
        return node_dao.delete(data)
        
        
    def get_tree(self) -> str:
        return node_dao.get_tree()
