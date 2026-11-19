"""
________________________________
Supplier                        |   <-- Class Name
________________________________|   
- __supplier_id: str            |   <-- Attributes
- __name: str                   |
- __contact_email: str          |
________________________________|
+ get_supplier_id(): str        |
+ get_name(): str               |   <-- Methods
+ to_dict(): dict               |
+ display_information(): None   |
________________________________|
"""

class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str):
        self.__supplier_id: str = supplier_id
        self.__name: str = name
        self.__contact_email: str = contact_email
 
    def get_supplier_id(self) -> str:
        return self.__supplier_id
 
    def get_name(self) -> str:
        return self.__name
 
    def display_information(self) -> None:
        print(f"Supplier ID: {self.__supplier_id}")
        print(f"Supplier Name: {self.__name}")
        print(f"Contact Email: {self.__contact_email}")
 
    def to_dict(self) -> dict:
        return {"id": self.__supplier_id, "name": self.__name,
                "contact_email": self.__contact_email}