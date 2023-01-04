from fastapi import HTTPException, APIRouter

import sys

sys.path.insert(0, '/home/hiraishin/Documents/layering-lab/data')

from repository import bookrepository
from models.book import Book

app = APIRouter()

# Book Application Interface

@app.get("/")
async def getbooks():
    response = await bookrepository.extractBooks()
    return response


@app.get("/{isbn}")
async def getbook(isbn: str):
    try:
        response = await bookrepository.extractBook(isbn)
        return response
    except:
        raise HTTPException(404, f"Book with isbn:{isbn} not found")


@app.post("/", response_model = Book)
async def postbook(book: Book):
    try:
        response = await bookrepository.addBook(book.dict())
        return response
    except:
        raise HTTPException(404, f"Can't add book")
    

@app.put("/{isbn}")
async def updatebook(isbn: str, book: Book):
    try:
        response = await bookrepository.updateBook(isbn, book.dict())
        return response
    except:
        raise HTTPException(404, f"Can't update book: {isbn}")
    

@app.delete("/{isbn}")
async def deletebook(isbn):
    try:
        await bookrepository.deleteBook(isbn)
        return f"Book with isbn: {isbn} deleted"
    except:
        raise HTTPException(404, f"Can't delete book: {isbn}")


    