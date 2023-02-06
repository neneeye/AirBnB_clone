#!/usr/bin/python3
"""
Unittest for "user.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_user.py
"""

import shutil
from models import user
from models.user import User
import unittest
import pycodestyle
import os
from time import sleep
from datetime import datetime
from models import storage


class TestUser(unittest.TestCase):
    """
    class that test User

    Functions:
        test_conformance
        test_documentation

        test_data_initialization_User
        test_hasattribute_User
        test_create_instance_from_dict_User
        test_update_my_object_User
        test_create_from_dict_User
    """
    path = "models/user.py"  # models/user.py
    file = os.path.splitext(path)[0].replace("/", ".")  # file to test

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([self.path])
        self.assertEqual(
            result.total_errors, 0,
            f"Found code style errors (pycodestyle) in file \"{self.path}\""
        )

    def test_documentation(self):
        """test all documentation of module"""
        # module documentation
        self.assertIsNotNone(
            user.__doc__, "Missing: module documentation of file \"user.py\"")

        # classes documentation
        for key, value in user.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in user.__dict__.items():
            if callable(value):
                for key2, value2 in value.__dict__.items():
                    if callable(value2):
                        self.assertIsNotNone(
                            value2.__doc__, f"Missing: function documentation \
of function \"{value2.__name__}\"")

    def setUp(self):
        try:
            shutil.copyfile("file.json", "tmp_file.json")
            os.remove("file.json")
            open("file.json", "w").close()
            storage._FileStorage__objects = {}
        except Exception:
            pass

    def tearDown(self):
        try:
            shutil.copyfile("tmp_file.json", "file.json")
            os.remove("tmp_file.json")
            storage._FileStorage__objects = {}
        except Exception:
            pass

# =========================
# test __init__
# =========================
    def test_data_initialization_User(self):
        """This fonction tests data initialization of User"""
        my_user = User()
        my_user.email = "example@example.x"
        my_user.password = "1234"
        my_user.first_name = "John"
        my_user.last_name = "SMITH"

        self.assertEqual(my_user.email, "example@example.x")
        self.assertIsInstance(my_user.email, str)
        self.assertEqual(my_user.password, "1234")
        self.assertIsInstance(my_user.password, str)
        self.assertEqual(my_user.first_name, "John")
        self.assertIsInstance(my_user.first_name, str)
        self.assertEqual(my_user.last_name, "SMITH")
        self.assertIsInstance(my_user.last_name, str)
        self.assertLessEqual(my_user.created_at, my_user.updated_at)

    def test_hasattribute_User(self):
        """test if instance User has attribute"""
        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))

    def test_create_instance_from_dict_User(self):
        """create a new instance User using a dictionnary of another instance \
already created"""
        my_user = User()
        my_user.email = "example@example.x"
        my_user.password = "1234"
        my_user.first_name = "John"
        my_user.last_name = "SMITH"
        my_model_json = my_user.to_dict()

        my_new_model = User(**my_model_json)
        my_new_model_json = my_new_model.to_dict()

        self.assertEqual(my_model_json, my_new_model_json)

    def test_update_my_object_User(self):
        """test if created_at is same after a modification but \
updated_at has changed"""
        my_user = User()
        my_user.email = "example@example.x"
        my_user.password = "1234"
        my_user.first_name = "John"
        my_user.last_name = "SMITH"

        old_updated = my_user.updated_at
        old_created = my_user.created_at

        sleep(0.1)
        my_user.password = "4321"
        my_user.save()

        self.assertEqual(my_user.password, "4321")
        self.assertEqual(old_created, my_user.created_at)
        self.assertNotEqual(old_updated, my_user.updated_at)

    def test_create_from_dict_User(self):
        """test create from dict"""
        my_user = User(**{
            "id": "4d8f60bd-ef9e-4186-9b7d-ef3bff6d6b7f",
            "created_at": "2022-03-02T08:30:54.356780",
            "updated_at": "2022-03-02T08:30:54.458488",
            "email": "example@example.x",
            "password": "4321",
            "first_name": "John",
            "last_name": "SMITH",
            "__class__": "User"
        })
        self.assertEqual(my_user.id, "4d8f60bd-ef9e-4186-9b7d-ef3bff6d6b7f")
        self.assertEqual(my_user.first_name, "John")
        self.assertEqual(my_user.created_at, datetime(
            2022, 3, 2, 8, 30, 54, 356780))
        self.assertNotEqual(my_user.__class__, "User")
