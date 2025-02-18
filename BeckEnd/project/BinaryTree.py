from project.ORM.domain import Node
from project import db


class BinaryTree:
    _session = db.session

    def __init__(self, data: int = None) -> None :
        if data is None:
            self.root = None
        else:
            self.root = Node.create_from_dto(value=data)
            self._session.add(self.root)
            self._session.commit()
            
            
    def find_by_id(self, id: int) -> Node:
        return self._session.query(Node).filter(Node.id == id).first()


    def find_by_data(self, data: int) -> Node:
        return self._session.query(Node).filter(Node.value == data).first()


    def add(self, data: int) -> None:
        if self.root is None:
            self.root = Node.create_from_dto(value=data, parent_id=None)
            self._session.add(self.root)
            self._session.commit()
        else:
            self.__add(data, self.root)


    def __add(self, data: int, node: Node) -> None:
        if node.value < data:
            if node.right_id is None:
                node.right = Node.create_from_dto(value=data, parent_id=node.id)
                self._session.add(node.right)
                self._session.commit()
            else:
                self.__add(data, node.right)
        elif node.value > data:
            if node.left_id is None:
                node.left = Node.create_from_dto(value=data, parent_id=node.id)
                self.session.add(node.left)
                self.session.commit()
            else:
                self.__add(data, node.left)
        else:
            pass  #Exeption


    def delete(self, data: int) -> bool:
        return self.__delete(data, self.root)


    def __delete(self, data: int, node: Node) -> bool:
        if node is None:
            return False
        elif node.value < data:
            return self.__delete(data, node.right)
        elif node.value > data:
            return self.__delete(data, node.left)
        else:
            if node.right_id is None and node.left_id is None:
                pass
            elif node.right_id is not None:
                node.right.parent.id = node.parent.id
                if self.check_id(node, node.parent):
                    node.parent.right.id = node.right.id
                else:
                    node.parent.left.id = node.right.id
            elif node.left_id is not None:
                node.left.parent.id = node.parent.id
                if self.__check_id(node, node.parent):
                    node.parent.right.id = node.left.id
                else:
                    node.parent.left.id = node.left.id
            else: # not None
                new_node = self.__min_node(node.right)
                new_node.parent.id = node.parent.id
                if self.__check_id(node, node.parent):
                    node.parent.right.id = new_node.id
                else:
                    node.parent.left.id = new_node.id
                    
                new_node.right.id = node.right.id
                new_node.left.id = node.left.id
                
                new_node.right.parent.id = new_node.id
                new_node.left.parent.id = new_node.id
            
            self._session.delete(node)
            self._session.commit()
            return True


    def __min_node(self, node: Node) -> Node:
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left

        if current_node.right is not None:
            current_node.parent.left.id = current_node.right.id
            current_node.right.parent.id = current_node.parent.left.id
            current_node.right.id = None
        else:
            current_node.parent.right.id = None

        return current_node


    def __check_id(self, node: Node, parent: Node) -> bool:
        result = False
        if(node.id == parent.right.id):
            result = True
        return result


    def get_tree(self) -> str:
        return "Binary Tree"
