#!/usr/bin/python3
"""
Unittest for "city.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_city.py
"""

import shutil
from models import city
from models.city import City
import unittest
import pycodestyle
import os
from time import sleep
from datetime import datetime
from models import storage


class TestCity(unittest.TestCase):
    """
    class that test City

    Functions:
        test_conformance
        test_documentation

        test_data_initialization_City
        test_hasattribute_City
        test_create_instance_from_dict_City
        test_update_my_object_City
        test_create_from_dict_City
    """
    path = "models/city.py"  # models/city.py
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
            city.__doc__, "Missing: module documentation of file \"city.py\"")

        # classes documentation
        for key, value in city.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in city.__dict__.items():
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
    def test_data_initialization_City(self):
        """This fonction tests data initialization of City"""
        my_city = City()
        my_city.state_id = "City_state_id_example"
        my_city.name = "City_name_example"

        self.assertEqual(my_city.state_id, "City_state_id_example")
        self.assertIsInstance(my_city.state_id, str)
        self.assertEqual(my_city.name, "City_name_example")
        self.assertIsInstance(my_city.name, str)
        self.assertLessEqual(my_city.created_at, my_city.updated_at)

    def test_hasattribute_City(self):
        """test if instance City has attribute"""
        my_city = City()
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertTrue(hasattr(my_city, "name"))

    def test_create_instance_from_dict_City(self):
        """create a new instance City using a dictionnary of another instance \
already created"""
        my_city = City()
        my_city.state_id = "City_state_id_example"
        my_city.name = "City_name_example"
        my_model_json = my_city.to_dict()

        my_new_model = City(**my_model_json)
        my_new_model_json = my_new_model.to_dict()

        self.assertEqual(my_model_json, my_new_model_json)

    def test_update_my_object_City(self):
        """test if created_at is same after a modification but \
updated_at has changed"""
        my_city = City()
        my_city.state_id = "City_state_id_example"
        my_city.name = "City_name_example"

        old_updated = my_city.updated_at
        old_created = my_city.created_at

        sleep(0.1)
        my_city.state_id = "elpmaxe_di_etats_ytiC"
        my_city.save()

        self.assertEqual(my_city.state_id, "elpmaxe_di_etats_ytiC")
        self.assertEqual(old_created, my_city.created_at)
        self.assertNotEqual(old_updated, my_city.updated_at)

    def test_create_from_dict_City(self):
        """test create from dict"""
        my_city = City(**{
            "id": "4d8f60bd-ef9e-4186-9b7d-ef3bff6d6b9f",
            "created_at": "2022-03-02T08:30:54.356780",
            "updated_at": "2022-03-02T08:30:54.458488",
            "state_id": "City_state_id_example",
            "name": "City_name_example",
            "__class__": "City"
        })
        self.assertEqual(my_city.id, "4d8f60bd-ef9e-4186-9b7d-ef3bff6d6b9f")
        self.assertEqual(my_city.name, "City_name_example")
        self.assertEqual(my_city.created_at, datetime(
            2022, 3, 2, 8, 30, 54, 356780))
        self.assertNotEqual(my_city.__class__, "City")
