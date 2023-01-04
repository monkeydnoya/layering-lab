import motor.motor_asyncio as motor
from dotenv import dotenv_values

import sys
sys.path.insert(0, '/home/hiraishin/Documents/layering-lab/data')

from models.book import Book

settings = dotenv_values("/home/hiraishin/Documents/layering-lab/.env")

client = motor.AsyncIOMotorClient(f'mongodb://{settings["mongodbHost"]}:{settings["mongodbPort"]}')
database = client.swa
collection = database.books


async def extractBooks():
    books = []
    cursor = collection.find()

    async for document in cursor:
        books.append(Book(**document))

    return books


async def extractBook(isbn):
    document = await collection.find({"isbn": isbn})

    return document


async def addBook(book):
    document = book
    result = await collection.insert_one(document)

    return document


async def updateBook(isbn, book):
    await collection.find_one_and_update({"isbn: isbn"}, {
        "$set": book
    })
    document = await collection.find({"isbn": isbn})

    return document


async def delete_order(order):
    await collection.delete_one({"orderTitle": order})

    return True