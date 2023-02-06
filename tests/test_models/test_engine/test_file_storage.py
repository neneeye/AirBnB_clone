#!/usr/bin/python3
"""
Unittest for "FileStorage.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_file_storage.py
"""

from curses.ascii import US
from subprocess import call
from models.engine.file_storage import FileStorage
import models
from models.user import User
from models.base_model import BaseModel
import unittest
import pycodestyle
import os
import shutil
import tempfile
from time import sleep
from datetime import datetime
import json


class TestFileStorage(unittest.TestCase):
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

    path = "models/engine/file_storage.py"  # models/FileStorage.py
    file = os.path.splitext(path)[0].replace("/", ".")  # file to test

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([self.path])
        self.assertEqual(
            result.total_errors,
            0, f"Found code style errors (pycodestyle) in file \"{self.path}\""
        )

    def test_documentation(self):
        """test all documentation of module"""
        # module documentation
        self.assertIsNotNone(
            FileStorage.__doc__,
            "Missing: module documentation of file \"FileStorage.py\"")

        # classes documentation
        for key, value in FileStorage.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in FileStorage.__dict__.items():
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
        except Exception:
            pass

    def tearDown(self):
        try:
            shutil.copyfile("tmp_file.json", "file.json")
            os.remove("tmp_file.json")
        except Exception:
            pass

    def test_attributes_assignement(self):
        self.assertIn("_FileStorage__objects", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIn("_FileStorage__file_path", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_all(self):
        models.storage._FileStorage__objects = {}
        self.assertFalse(models.storage.all())
        models.storage._FileStorage__objects = {"Hello": "olleH"}
        self.assertTrue(models.storage.all())

    # def test_save(self):
    #     models.storage._FileStorage__objects = ""
    #     models.storage.save()
    #     with open("file.json", "r") as f:
    #         exception = f.read()
    #     self.assertTrue(exception)

    def test_reload(self):
        models.storage._FileStorage__objects = {}
        self.assertFalse(models.storage.all())
        with open("file.json", "w") as f:
            f.write(json.dumps({
                "BaseModel.70549f31-bff4-4a34-bd10-b8eaaeb3bb6b":
                {"id": "70549f31-bff4-4a34-bd10-b8eaaeb3bb6b", "created_at":
                 "2022-03-01T20:27:24.506780", "updated_at":
                 "2022-03-01T20:27:24.506790", "__class__":
                 "BaseModel"}}))
        models.storage.reload()
        self.assertTrue(models.storage.all())

    def test_new(self):
        models.storage._FileStorage__objects = {}
        models.storage.new(User())
        models.storage.save()
        self.assertTrue(models.storage._FileStorage__objects)

    def test_save_new(self):
        models.storage._FileStorage__objects = {}
        self.assertFalse(models.storage.all())
        models.storage.new(User())
        models.storage.save()
        models.storage.reload()
        self.assertEqual(models.storage.all(), models.storage.__dict__[
                         '_FileStorage__objects'])
