#!/usr/bin/python3
"""
Unittest for "base_model.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_base_model.py
"""

from models import base_model
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import os
import shutil
import time
import unittest
import pycodestyle


class TestBaseModel(unittest.TestCase):
    """
    class that test BaseModel

    Functions:
        test_conformance
        test_documentation

        test_data_initialization
        test_create_instance_from_dict
        test_update_my_object
        test_create_from_dict

        test_type_id
        test_len_id
        test_uniq_id

        test_type_create_at
        test_type_create_at_to_dict
        test_type_updated_at
        test_type_updated_at_to_dict

        test_type_str
        test_print_str

        test_type_to_dict
    """
    path = "models/base_model.py"  # models/base_model.py
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
            base_model.__doc__,
            "Missing: module documentation of file \"base.model\"")

        # classes documentation
        for key, value in base_model.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in base_model.__dict__.items():
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
    def test_data_initialization(self):
        """This fonction tests data initialization"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)
        self.assertLessEqual(my_model.created_at, my_model.updated_at)

    def test_create_instance_from_dict(self):
        """create a new instance using a dictionnary of another instance \
already created"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)
        my_new_model_json = my_new_model.to_dict()

        self.assertEqual(my_model_json, my_new_model_json)

    def test_update_my_object(self):
        """test if created_at is same after a modification but \
updated_at has changed"""
        my_model = BaseModel()
        my_model.name = "Hello"

        old_updated = my_model.updated_at
        old_created = my_model.created_at

        time.sleep(0.1)
        my_model.name = "bye"
        my_model.save()

        self.assertEqual(old_created, my_model.created_at)
        self.assertNotEqual(old_updated, my_model.updated_at)

    def test_create_from_dict(self):
        """test create from dict"""
        my_model = BaseModel(**{
            "id": "08400995-36d2-46a8-b932-364e7aef5eeb",
            "created_at": "2022-03-01T14:12:29.585036",
            "updated_at": "2022-03-01T14:12:29.585130",
            "name": "toto",
            "my_number": 89,
            "__class__": "BaseModel"
        })
        self.assertEqual(my_model.id, "08400995-36d2-46a8-b932-364e7aef5eeb")
        self.assertEqual(my_model.name, "toto")
        self.assertEqual(my_model.created_at, datetime(
            2022, 3, 1, 14, 12, 29, 585036))
        self.assertNotEqual(my_model.__class__, "BaseModel")

    def test_with_one_argument(self):
        """test create with one argument, has to do nothing with"""
        my_model = BaseModel("hello")
        my_model.name = "Mr.X"

        self.assertEqual(my_model.name, "Mr.X")

# =========================
# test id
# =========================
    def test_len_id(self):
        """This function tests len of id"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        my_model3 = BaseModel()
        my_model4 = BaseModel()
        my_model5 = BaseModel()
        id_list = [my_model1.id, my_model2.id,
                   my_model3.id, my_model4.id, my_model5.id]
        for id in range(len(id_list)-1):
            self.assertEqual(len(id_list[id]), 36)

    def test_uniq_id(self):
        """This function tests if id is different for all models"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        my_model3 = BaseModel()
        my_model4 = BaseModel()
        my_model5 = BaseModel()
        id_list = [my_model1.id, my_model2.id,
                   my_model3.id, my_model4.id, my_model5.id]
        for id in range(len(id_list)-1):
            self.assertNotEqual(id_list[id], id_list[id+1])

# =========================
# test created_at
# =========================
    def test_type_create_at(self):
        """This function test if the return of create_at method \
is a datetime object"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_type_create_at_to_dict(self):
        """This function test if the return of to_dict() at index create_at \
is a string object"""
        my_model = BaseModel()
        dict = my_model.to_dict()
        self.assertIsInstance(dict["created_at"], str)

# =========================
# test updated_at
# =========================
    def test_type_update_at(self):
        """This function test if the return of update_at method \
is a datetime object"""
        my_model = BaseModel()
        self.assertIsInstance(my_model.created_at, datetime)

    def test_type_updated_at_to_dict(self):
        """This function test if the return of to_dict() at index updated_at \
is a string object"""
        my_model = BaseModel()
        dict = my_model.to_dict()
        self.assertIsInstance(dict["updated_at"], str)

# =========================
# test __str__
# =========================
    def test_type_str(self):
        """This function tests if __str__ method returns a string"""
        my_model = BaseModel()
        self.assertIsInstance((my_model.__str__()), str)

    def test_print_str(self):
        """This function tests if __str__ is print correctly"""
        my_model = BaseModel(**{
            "id": "08400995-36d2-46a8-b932-364e7aef5eeb",
            "created_at": "2022-03-01T14:12:29.585036",
            "updated_at": "2022-03-01T14:12:29.585130",
            "name": "toto",
            "my_number": 89,
            "__class__": "BaseModel"
        })
        self.assertEqual((my_model.__str__(
        )), "[BaseModel] (08400995-36d2-46a8-b932-364e7aef5eeb) \
{'id': '08400995-36d2-46a8-b932-364e7aef5eeb', 'created_at': \
datetime.datetime(2022, 3, 1, 14, 12, 29, 585036), 'updated_at': \
datetime.datetime(2022, 3, 1, 14, 12, 29, 585130), 'name': \
'toto', 'my_number': 89}")

# =========================
# test to_dict
# =========================
    def test_type_to_dict(self):
        """This function tests if to_dict method returns dict """
        my_model = BaseModel()
        self.assertIsInstance(my_model.to_dict(), dict)
