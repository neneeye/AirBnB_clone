#!/usr/bin/python3
"""
Unittest for "place.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_place.py
"""

import shutil
from models import place
from models.place import Place
import unittest
import pycodestyle
import os
from time import sleep
from datetime import datetime
from models import storage


class TestPlace(unittest.TestCase):
    """
    class that test Place

    Functions:
        test_conformance
        test_documentation

        test_data_initialization_Place
        test_hasattribute_Place
        test_create_instance_from_dict_Place
        test_update_my_object_Place
        test_create_from_dict_Place
    """
    path = "models/place.py"  # models/place.py
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
            place.__doc__,
            "Missing: module documentation of file \"place.py\"")

        # classes documentation
        for key, value in place.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__,
                    f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in place.__dict__.items():
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
    def test_data_initialization_Place(self):
        """This fonction tests data initialization of Place"""
        my_place = Place()
        my_place.city_id = "Place_place_id_example"
        my_place.user_id = "Place_user_id_example"
        my_place.name = "Place_name_example"
        my_place.description = "Place_description_example"
        my_place.number_rooms = 1
        my_place.number_bathrooms = 2
        my_place.max_guest = 3
        my_place.price_by_night = 4
        my_place.latitude = 5.5
        my_place.longitude = 6.6
        my_place.amenity_ids = [
            "Place_amenity_ids_example1", "Place_amenity_ids_example2"]

        self.assertEqual(my_place.city_id, "Place_place_id_example")
        self.assertIsInstance(my_place.city_id, str)
        self.assertEqual(my_place.user_id, "Place_user_id_example")
        self.assertIsInstance(my_place.user_id, str)
        self.assertEqual(my_place.name, "Place_name_example")
        self.assertIsInstance(my_place.name, str)
        self.assertEqual(my_place.description, "Place_description_example")
        self.assertIsInstance(my_place.description, str)
        self.assertEqual(my_place.number_rooms, 1)
        self.assertIsInstance(my_place.number_rooms, int)
        self.assertEqual(my_place.number_bathrooms, 2)
        self.assertIsInstance(my_place.number_bathrooms, int)
        self.assertEqual(my_place.max_guest, 3)
        self.assertIsInstance(my_place.max_guest, int)
        self.assertEqual(my_place.price_by_night, 4)
        self.assertIsInstance(my_place.price_by_night, int)
        self.assertEqual(my_place.latitude, 5.5)
        self.assertIsInstance(my_place.latitude, float)
        self.assertEqual(my_place.longitude, 6.6)
        self.assertIsInstance(my_place.longitude, float)
        self.assertEqual(my_place.amenity_ids, ["Place_amenity_ids_\
example1", "Place_amenity_ids_example2"])
        self.assertIsInstance(my_place.amenity_ids, list)
        self.assertLessEqual(my_place.created_at, my_place.updated_at)

    def test_hasattribute_Place(self):
        """test if instance Place has attribute"""
        my_place = Place()
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertTrue(hasattr(my_place, "name"))
        self.assertTrue(hasattr(my_place, "description"))
        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertTrue(hasattr(my_place, "amenity_ids"))

    def test_create_instance_from_dict_Place(self):
        """create a new instance Place using a dictionnary \
of another instance already created"""
        my_place = Place()
        my_place.city_id = "Place_place_id_example"
        my_place.name = "Place_name_example"
        my_model_json = my_place.to_dict()

        my_new_model = Place(**my_model_json)
        my_new_model_json = my_new_model.to_dict()

        self.assertEqual(my_model_json, my_new_model_json)

    def test_update_my_object_Place(self):
        """test if created_at is same after a modification but \
updated_at has changed"""
        my_place = Place()
        my_place.city_id = "Place_state_id_example"
        my_place.name = "Place_name_example"

        old_updated = my_place.updated_at
        old_created = my_place.created_at

        sleep(0.1)
        my_place.city_id = "elpmaxe_di_etats_ytiC"
        my_place.save()

        self.assertEqual(my_place.city_id, "elpmaxe_di_etats_ytiC")
        self.assertEqual(old_created, my_place.created_at)
        self.assertNotEqual(old_updated, my_place.updated_at)

    def test_create_from_dict_Place(self):
        """test create from dict"""
        my_place = Place(**{
            "id": "9558dab8-d155-4731-b8bf-43ae1c60d7c4",
            "created_at": "2022-03-02T08:58:33.467526",
            "updated_at": "2022-03-02T08:58:33.467527",
            "city_id": "Place_place_id_example",
            "user_id": "Place_user_id_example",
            "name": "Place_name_example",
            "description": "Place_description_example",
            "number_rooms": 1,
            "number_bathrooms": 2,
            "max_guest": 3,
            "price_by_night": 4,
            "latitude": 5.5,
            "longitude": 6.6,
            "amenity_ids": [
                "Place_amenity_ids_example1",
                "Place_amenity_ids_example2"
            ],
            "__class__": "Place"
        })
        self.assertEqual(my_place.id, "9558dab8-d155-4731-b8bf-43ae1c60d7c4")
        self.assertEqual(my_place.name, "Place_name_example")
        self.assertEqual(my_place.created_at, datetime(
            2022, 3, 2, 8, 58, 33, 467526))
        self.assertNotEqual(my_place.__class__, "Place")
