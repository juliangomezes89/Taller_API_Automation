import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
import unittest
from datetime import datetime

from taller_1.Core import authors as aut


class ApiRequestsAuthors(unittest.TestCase):
    now = datetime.now()
    def set_url(self, url):
        aut.set_url(url)

    def test_url(self):
        self.response = aut.get_url()

    def test_get_author_by_book(self, id):
        self.response = aut.get_author_by_book(id)

    def test_get_all_authors(self):
        self.response = aut.get_all_authors()

    def test_get_author(self, id):
        self.response = aut.get_author(id)

    def test_create_author(self, id, id_book, firstname, lastname):
        self.response = aut.create_authors(id,
                                           id_book,
                                           firstname,
                                           lastname)

    def test_update_author(self, id, id_book, firstname, lastname):
        self.response = aut.edit_authors(id,
                                         id_book,
                                         firstname,
                                         lastname)

    def test_delete_author(self, id):
        self.response = aut.delete_authors(id)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


if __name__ == '__main__':
    unittest.main()
