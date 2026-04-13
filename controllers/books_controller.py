from flask import request, jsonify
from models.book import Book
from db import db


def create_book():
    post_data = request.form if request.form else request.get_json()

    try:
        book = Book(
            school_id=post_data['school_id'],
            title=post_data['title'],
            author=post_data.get('author'),
            subject=post_data.get('subject'),
            rarity_level=post_data.get('rarity_level'),
            magical_properties=post_data.get('magical_properties'),
            available=post_data.get('available', True)
        )

        db.session.add(book)
        db.session.commit()

        return jsonify(message="Book created successfully", book_id=str(book.book_id)), 201

    except Exception as e:
        return jsonify(error=str(e)), 400


def get_all_books():
    books = Book.query.all()
    return jsonify([
        {
            "book_id": str(b.book_id),
            "school_id": str(b.school_id),
            "title": b.title,
            "author": b.author,
            "subject": b.subject,
            "rarity_level": b.rarity_level,
            "magical_properties": b.magical_properties,
            "available": b.available
        }
        for b in books
    ]), 200


def get_available_books():
    books = Book.query.filter_by(available=True).all()
    return jsonify([
        {
            "book_id": str(b.book_id),
            "title": b.title,
            "author": b.author
        }
        for b in books
    ]), 200


def get_book_by_id(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify(error="Book not found"), 404

    return jsonify({
        "book_id": str(book.book_id),
        "school_id": str(book.school_id),
        "title": book.title,
        "author": book.author,
        "subject": book.subject,
        "rarity_level": book.rarity_level,
        "magical_properties": book.magical_properties,
        "available": book.available
    }), 200


def update_book(book_id):
    post_data = request.form if request.form else request.get_json()

    book = Book.query.get(book_id)
    if not book:
        return jsonify(error="Book not found"), 404

    for key, value in post_data.items():
        setattr(book, key, value)

    db.session.commit()
    return jsonify(message="Book updated successfully"), 200


def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify(error="Book not found"), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify(message="Book deleted successfully"), 200