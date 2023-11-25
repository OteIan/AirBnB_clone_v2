#!/usr/bin/python3
"""
Test cases for filestorage
"""
import unittest
import os
import json
import models.engine.file_storage as file_storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test case class for the FileStorage class.

    This class contains unit tests
      for various methods of the FileStorage class.
    """
    def setUp(self):
        """
        Set up a new instance of FileStorage before each test.
        """
        self.file_storage = FileStorage()
        self.file_storage.reload()

    def tearDown(self):
        """
        Remove the JSON file after the test
        """
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_docsrings(self):
        """Test for module, class and function docstrings"""
        self.assertIsNotNone(file_storage.__doc__)
        self.assertIsNotNone(self.file_storage.__doc__)
        self.assertIsNotNone(self.file_storage.all.__doc__)
        self.assertIsNotNone(self.file_storage.new.__doc__)
        self.assertIsNotNone(self.file_storage.save.__doc__)
        self.assertIsNotNone(self.file_storage.reload.__doc__)
        self.assertIsNotNone(self.file_storage.delete.__doc__)

    def test_file_path(self):
        """Checks if __file_path is a string"""
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test_objects(self):
        """Checks if objects is a dictionary"""
        self.assertIsInstance(storage.all(), dict)

    def test_initial_list_is_empty(self):
        """ """
        self.assertEqual(len(storage.all()), 0)

    def test_new_object_to___objects(self):
        """ """
        new = BaseModel()
        loaded = storage.all().get(f"{BaseModel.__name__}.{new.id}")
        self.assertTrue(new is loaded)

    def test_all_method_returns_dictionary(self):
        """
        Test if the all method returns a dictionary.
        """
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_instantiation_BaseModel(self):
        """
        File is not created on instantiation
        """
        new = BaseModel()
        self.assertFalse(os.path.exists("file.json"))

    def test_key_format(self):
        """Checks if key is in the format: <class name>.<id>"""
        keys = storage.all().keys()
        for key in keys:
            args = key.split('.')
            self.assertEqual(len(args), 2)
            class_name, obj_id = args
            self.assertEqual(key, f"{class_name}.{obj_id}")

    def test_new_method_adds_to_objects(self):
        """
        Test if the new method adds an object to the __objects dictionary.
        """
        user = User()
        storage.new(user)
        self.assertIn(f'User.{user.id}', storage.all())

    def test_save_method_creates_json_file(self):
        """
        Test if the save method creates a JSON file.
        """
        new = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method_loads_objects_from_json(self):
        """
        Test if the reload method loads objects
          from a JSON file into __objects.
        """
        new = BaseModel()
        storage.save()
        storage.reload()
        loaded = storage.all().get(f"{BaseModel.__name__}.{new.id}")
        self.assertIsNotNone(loaded)
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_from_empty_file(self):
        """Load from an empty file"""
        with open("file.json", "w") as file:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """Nothing occurs if the file is not there"""
        self.assertEqual(storage.reload(), None)
        
    def test_delete_method_removes_object(self):
        """ Checks if object is deleted """
        user = User()
        storage.new(user)
        storage.save()
        storage.delete(user)
        self.assertNotIn(f'User.{User.id}', storage.all())
        
    def test_create_method_with_invalid_parameters


if __name__ == '__main__':
    unittest.main()
