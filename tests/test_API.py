from sumarpi.models import Document
from tinydb import TinyDB
import unittest
import requests
import pathlib
import random
import lorem


class TestAPI(unittest.TestCase):
    db = TinyDB(str(pathlib.Path(
        __file__).parent.parent.absolute()) + '/db.json')
    
    try:
        last_id = db.all()[-1].doc_id
    except:
        print('Please fill the database with records first, using the form at http://127.0.0.1:5000')
        exit()

    def test_POST_302_scenario(self):
        ''' Test POST HTTP 302 (Found) response for all submitted documents '''
        for id_ in range(1, self.last_id):
            response = requests.post(f'http://127.0.0.1:5000/summary/{id_}')
            if response.status_code != 302:
                self.assertEqual(response.status_code, 302)
        self.assertEqual(1, 1)

    def test_POST_404_scenario(self):
        ''' Test POST HTTP 404 (Not found) response  or non existent id '''
        response = requests.post(
            f'http://127.0.0.1:5000/summary/{self.last_id+1}')
        self.assertEqual(response.status_code, 404)

    def test_GET_302_scenario(self):
        ''' Test GET HTTP 302 (Found) response for all submitted documents '''
        for id_ in range(1, self.last_id):
            response = requests.get(f'http://127.0.0.1:5000/summary/{id_}')
            if response.status_code != 302:
                self.assertEqual(response.status_code, 302)
        self.assertEqual(1, 1)

    def test_GET_404_scenario(self):
        ''' Test GET HTTP 404 (Not found) response for non existent id '''
        response = requests.get(
            f'http://127.0.0.1:5000/summary/{self.last_id+1}')
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
