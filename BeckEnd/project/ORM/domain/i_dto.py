from abc import abstractmethod
from typing import Dict, Any


class IDTO():
    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        pass


    @staticmethod
    @abstractmethod
    def create_from_dto(self, dto_dict: Dict[str, Any]) -> object:
        pass

