import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
import unittest
from datetime import datetime

from taller_1.Core import books as book


class ApiRequestsBooks(unittest.TestCase):
    now = datetime.now()
    def set_url(self, url):
        book.set_url(url)

    def test_url(self):
        self.response = book.get_url()

    def test_get_all_books(self):
        self.response = book.get_all_books()



    def test_create_book(self, id, book_title, book_description, page_count, excerpt, date):
        self.response = book.create_book(id,
                                         book_title,
                                         book_description,
                                         page_count,
                                         excerpt,
                                         date)


    def test_delete_book(self, id):
        self.response = book.delete_book(id)

    def test_get_book(self, id):
        self.response = book.get_book(id)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)

    def test_update_book(self, id, book_title, book_description, page_count, excerpt, date):
        self.response = book.edit_book(id,
                                       book_title,
                                       book_description,
                                       page_count,
                                       excerpt,
                                       date)


if __name__ == '__main__':
    unittest.main()