#!/usr/bin/python3
"""
Unittest for "amenity.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_amenity.py
"""

import shutil
from models import amenity
from models.amenity import Amenity
import unittest
import pycodestyle
import os
from time import sleep
from datetime import datetime
from models import storage


class TestAmenity(unittest.TestCase):
    """
    class that test Amenity

    Functions:
        test_conformance
        test_documentation

        test_data_initialization_Amenity
        test_hasattribute_Amenity
        test_create_instance_from_dict_Amenity
        test_update_my_object_Amenity
        test_create_from_dict_Amenity
    """
    path = "models/amenity.py"  # models/amenity.py
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
            amenity.__doc__,
            "Missing: module documentation of file \"amenity.py\"")

        # classes documentation
        for key, value in amenity.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in amenity.__dict__.items():
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
    def test_data_initialization_Amenity(self):
        """This fonction tests data initialization of Amenity"""
        my_amenity = Amenity()
        my_amenity.name = "example"

        self.assertEqual(my_amenity.name, "example")
        self.assertIsInstance(my_amenity.name, str)
        self.assertLessEqual(my_amenity.created_at, my_amenity.updated_at)

    def test_hasattribute_Amenity(self):
        """test if instance Amenity has attribute"""
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "name"))

    def test_create_instance_from_dict_Amenity(self):
        """create a new instance Amenity using a dictionnary \
of another instance already created"""
        my_amenity = Amenity()
        my_amenity.name = "example"
        my_model_json = my_amenity.to_dict()

        my_new_model = Amenity(**my_model_json)
        my_new_model_json = my_new_model.to_dict()

        self.assertEqual(my_model_json, my_new_model_json)

    def test_update_my_object_Amenity(self):
        """test if created_at is same after a modification but \
updated_at has changed"""
        my_amenity = Amenity()
        my_amenity.name = "example"

        old_updated = my_amenity.updated_at
        old_created = my_amenity.created_at

        sleep(0.1)
        my_amenity.name = "elpmaxe"
        my_amenity.save()

        self.assertEqual(my_amenity.name, "elpmaxe")
        self.assertEqual(old_created, my_amenity.created_at)
        self.assertNotEqual(old_updated, my_amenity.updated_at)

    def test_create_from_dict_Amenity(self):
        """test create from dict"""
        my_amenity = Amenity(**{
            "id": "4d8f60bd-ef9e-4186-9b7d-ef3bff6d6b8f",
            "created_at": "2022-03-02T08:30:54.356780",
            "updated_at": "2022-03-02T08:30:54.458488",
            "name": "example",
            "__class__": "Amenity"
        })
        self.assertEqual(my_amenity.id, "4d8f60bd-ef9e-4186-9b7d-ef3bff6d6b8f")
        self.assertEqual(my_amenity.name, "example")
        self.assertEqual(my_amenity.created_at, datetime(
            2022, 3, 2, 8, 30, 54, 356780))
        self.assertNotEqual(my_amenity.__class__, "Amenity")
