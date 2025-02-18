from project.ORM.domain.tables.Node import Node
from project import db, binary_tree

class NodeDAO:
    def find_all(self) -> list[Node]:
        from project import db
        return db.session.query(Node).all()


    def find_by_id(self, id: int) -> Node:
        return binary_tree.find_by_id(id)
    
    
    def find_by_data(self, data: int) -> Node:
        return binary_tree.find_by_data(data)

        
    def add(self, data: int) -> None:
        binary_tree.add(data)


    def delete(self, data: int) -> bool:
        return binary_tree.delete(data)
        
        
    def get_tree(self) -> str:
        return binary_tree.get_tree()

