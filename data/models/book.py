from pydantic import BaseModel 

class Book(BaseModel):
    isbn: str
    title: str
    price: int