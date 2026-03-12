
from flask import Blueprint, request
from controllers.books_controller import (
    create_book,
    get_all_books,
    get_available_books,
    get_book_by_id,
    update_book,
    delete_book
)

books_routes = Blueprint('books_routes', __name__)

@books_routes.route('/book', methods=['POST'])
def create():
    return create_book(request.json)

@books_routes.route('/books', methods=['GET'])
def get_all():
    return get_all_books()

@books_routes.route('/books/available', methods=['GET'])
def get_available():
    return get_available_books()

@books_routes.route('/book/<book_id>', methods=['GET'])
def get_by_id(book_id):
    return get_book_by_id(book_id)

@books_routes.route('/book/<book_id>', methods=['PUT'])
def update(book_id):
    return update_book(book_id, request.json)

@books_routes.route('/book/delete/<book_id>', methods=['DELETE'])
def delete(book_id):
    return delete_book(book_id)
