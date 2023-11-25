import unittest
import pep8
import os
from os import getenv
import MySQLdb
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


@unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
class TestDBStorage(unittest.TestCase):
    """This will test the DBStorage"""

    @classmethod
    def setUpClass(cls):
        """Set up for the test"""
        cls.test_user = getenv("HBNB_MYSQL_USER")
        cls.test_passwd = getenv("HBNB_MYSQL_PWD")
        cls.test_db = getenv("HBNB_MYSQL_DB")
        cls.test_host = getenv("HBNB_MYSQL_HOST")
        cls.db_connection = MySQLdb.connect(
            host=cls.test_host,
            user=cls.test_user,
            passwd=cls.test_passwd,
            db=cls.test_db,
            charset="utf8"
        )
        cls.db_cursor = cls.db_connection.cursor()
        cls.storage_instance = DBStorage()
        cls.storage_instance.reload()

    @classmethod
    def tearDownClass(cls):
        """At the end of the test, this will tear it down"""
        cls.db_cursor.close()
        cls.db_connection.close()

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_pep8_DBStorage(self):
        """Test Pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0, "Fix Pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_read_tables(self):
        """Existing tables"""
        self.db_cursor.execute("SHOW TABLES")
        tables = self.db_cursor.fetchall()
        self.assertEqual(len(tables), 7)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_user(self):
        """No elements in users"""
        self.db_cursor.execute("SELECT * FROM users")
        users = self.db_cursor.fetchall()
        self.assertEqual(len(users), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_no_element_cities(self):
        """No elements in cities"""
        self.db_cursor.execute("SELECT * FROM cities")
        cities = self.db_cursor.fetchall()
        self.assertEqual(len(cities), 0)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != 'db', 'NO DB')
    def test_add(self):
        """Test same size between storage() and existing db"""
        self.db_cursor.execute("SELECT * FROM states")
        states = self.db_cursor.fetchall()
        self.assertEqual(len(states), 0)
        state_instance = State(name="LUISILLO")
        state_instance.save()
        self.db_connection.autocommit(True)
        self.db_cursor.execute("SELECT * FROM states")
        states = self.db_cursor.fetchall()
        self.assertEqual(len(states), 1)


if __name__ == "__main__":
    unittest.main()
