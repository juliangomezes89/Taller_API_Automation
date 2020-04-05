import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
import unittest
from datetime import datetime

from taller_1.Core import activities as act


class ApiRequestsActivities(unittest.TestCase):
    now = datetime.now()
    def set_url(self, url):
        act.set_url(url)

    def test_url(self):
        self.response = act.get_url()

    def test_get_all_activites(self):
        self.response = act.get_all_activities()

    def test_get_activity(self, id):
        self.response = act.get_activity(id)

    def test_create_activity(self, id, activity_name, date, status):
        self.response = act.create_activity(id,
                                            activity_name,
                                            date,
                                            status)

    def test_update_activity(self, id, activity_name, date, status):
        self.response = act.create_activity(id,
                                            activity_name,
                                            date,
                                            status)

    def test_delete_activity(self, id):
        self.response = act.delete_activity(id)

    def test_validate_status_code(self, status_code):
        code = self.response.status_code
        self.assertEqual(code, status_code)


# if __name__ == '__main__':
# unittest.main()
