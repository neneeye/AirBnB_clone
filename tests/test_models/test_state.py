#!/usr/bin/python3
"""
Unittest for "state.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_state.py
"""

import shutil
from models import state
from models.state import State
import unittest
import pycodestyle
import os
from time import sleep
from datetime import datetime
from models import storage


class TestState(unittest.TestCase):
    """
    class that test State

    Functions:
        test_conformance
        test_documentation

        test_data_initialization_State
        test_hasattribute_State
        test_create_instance_from_dict_State
        test_update_my_object_State
        test_create_from_dict_State
    """
    path = "models/state.py"  # models/state.py
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
            state.__doc__,
            "Missing: module documentation of file \"state.py\"")

        # classes documentation
        for key, value in state.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in state.__dict__.items():
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
    def test_data_initialization_State(self):
        """This fonction tests data initialization of State"""
        my_state = State()
        my_state.name = "State_name_example"

        self.assertEqual(my_state.name, "State_name_example")
        self.assertIsInstance(my_state.name, str)
        self.assertLessEqual(my_state.created_at, my_state.updated_at)

    def test_hasattribute_State(self):
        """test if instance State has attribute"""
        my_state = State()
        self.assertTrue(hasattr(my_state, "name"))

    def test_create_instance_from_dict_State(self):
        """create a new instance State using a dictionnary \
of another instance already created"""
        my_state = State()
        my_state.name = "State_name_example"
        my_model_json = my_state.to_dict()

        my_new_model = State(**my_model_json)
        my_new_model_json = my_new_model.to_dict()

        self.assertEqual(my_model_json, my_new_model_json)

    def test_update_my_object_State(self):
        """test if created_at is same after a modification but \
updated_at has changed"""
        my_state = State()
        my_state.name = "State_name_example"

        old_updated = my_state.updated_at
        old_created = my_state.created_at

        sleep(0.1)
        my_state.name = "elpmaxe"
        my_state.save()

        self.assertEqual(my_state.name, "elpmaxe")
        self.assertEqual(old_created, my_state.created_at)
        self.assertNotEqual(old_updated, my_state.updated_at)

    def test_create_from_dict_State(self):
        """test create from dict"""
        my_state = State(**{
            "id": "0e2f9562-c0bf-4469-baeb-05cd5e653e56",
            "created_at": "2022-03-02T12:32:23.083225",
            "updated_at": "2022-03-02T12:32:23.183379",
            "name": "elpmaxe",
            "__class__": "State"
        })
        self.assertEqual(my_state.id, "0e2f9562-c0bf-4469-baeb-05cd5e653e56")
        self.assertEqual(my_state.name, "elpmaxe")
        self.assertEqual(my_state.created_at, datetime(
            2022, 3, 2, 12, 32, 23, 83225))
        self.assertNotEqual(my_state.__class__, "State")
