import unittest
import time
import subprocess
import requests

cmd_django_server = "python manage.py runserver 127.0.0.1:8005" \
                        " --noreload --nothreading"


class TestDjangoSever(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(cmd_django_server.split())
        # Depending on the machine,
        # you may need to increase the sleep time,
        # sometimes the server will not have time to start.
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.server_process.kill()

    def test_get_course(self):
        r = requests.get("http://localhost:8005/api/rates/?from=USD&to=RUB")
        r_json = r.json()
        self.assertTrue(r.status_code == requests.codes.ok)
        self.assertTrue("result" in r_json)
        self.assertTrue(isinstance(r_json["result"], int | float))

    def test_currency_not_found(self):
        r = requests.get("http://localhost:8005/api/rates/?from=efeefq&to=wefef")
        r_json = r.json()
        self.assertTrue(r.status_code == requests.codes.ok)
        self.assertTrue("error" in r_json)
        self.assertTrue(r_json["error"] == "currency ticker not found")

    def test_value_error(self):
        r = requests.get("http://localhost:8005/api/rates/?from=USD&to=RUB&value=gte")
        r_json = r.json()
        self.assertTrue(r.status_code == requests.codes.ok)
        self.assertTrue("error" in r_json)
        self.assertTrue(r_json["error"] == "value field can only be digit or float")
