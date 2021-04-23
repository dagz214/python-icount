import unittest
from python_icount import Icount
import random as rand

ic=Icount()
class IcountTestCase(unittest.TestCase):
    
    def setUp(self):
        self.ic=Icount()

    def test_icount_authenticated(self):

        self.assertNotEqual(self.ic.json_response['reason'], 'bad_login')
        self.assertEqual(self.ic.json_response['reason'], 'OK')


    def test_icount_has_sid(self):
        self.assertIsNotNone(self.ic.sid)

    def test_is_created(self):
        client_name=f'client_{rand.randrange(1,1000)}'
        self.assertEqual(self.ic.client.create_client(client_name)['reason'], 'OK')
