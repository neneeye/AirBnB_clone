#!/usr/bin/python3
"""
Unittest for "review.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_review.py
"""

import shutil
from models import review
from models.review import Review
import unittest
import pycodestyle
import os
from time import sleep
from datetime import datetime
from models import storage


class TestReview(unittest.TestCase):
    """
    class that test Review

    Functions:
        test_conformance
        test_documentation

        test_data_initialization_Review
        test_hasattribute_Review
        test_create_instance_from_dict_Review
        test_update_my_object_Review
        test_create_from_dict_Review
    """
    path = "models/review.py"  # models/review.py
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
            review.__doc__,
            "Missing: module documentation of file \"review.py\"")

        # classes documentation
        for key, value in review.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in review.__dict__.items():
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
    def test_data_initialization_Review(self):
        """This fonction tests data initialization of Review"""
        my_review = Review()
        my_review.place_id = "Review_place_id_example"
        my_review.user_id = "Review_user_id_example"
        my_review.text = "Review_text_example"

        self.assertEqual(my_review.place_id, "Review_place_id_example")
        self.assertIsInstance(my_review.place_id, str)
        self.assertEqual(my_review.user_id, "Review_user_id_example")
        self.assertIsInstance(my_review.user_id, str)
        self.assertEqual(my_review.text, "Review_text_example")
        self.assertIsInstance(my_review.text, str)
        self.assertLessEqual(my_review.created_at, my_review.updated_at)

    def test_hasattribute_Review(self):
        """test if instance Review has attribute"""
        my_review = Review()
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertTrue(hasattr(my_review, "text"))

    def test_create_instance_from_dict_Review(self):
        """create a new instance Review using a dictionnary \
of another instance already created"""
        my_review = Review()
        my_review.place_id = "Review_place_id_example"
        my_review.user_id = "Review_user_id_example"
        my_review.text = "Review_text_example"
        my_model_json = my_review.to_dict()

        my_new_model = Review(**my_model_json)
        my_new_model_json = my_new_model.to_dict()

        self.assertEqual(my_model_json, my_new_model_json)

    def test_update_my_object_Review(self):
        """test if created_at is same after a modification but \
updated_at has changed"""
        my_review = Review()
        my_review.place_id = "Review_place_id_example"
        my_review.user_id = "Review_user_id_example"
        my_review.text = "Review_text_example"

        old_updated = my_review.updated_at
        old_created = my_review.created_at

        sleep(0.1)
        my_review.user_id = "4321"
        my_review.save()

        self.assertEqual(my_review.user_id, "4321")
        self.assertEqual(old_created, my_review.created_at)
        self.assertNotEqual(old_updated, my_review.updated_at)

    def test_create_from_dict_Review(self):
        """test create from dict"""
        my_review = Review(**{
            "id": "b21883f7-f591-4eba-8ea4-db95d345db77",
            "created_at": "2022-03-02T12:28:19.074340",
            "updated_at": "2022-03-02T12:28:19.177011",
            "place_id": "Review_place_id_example",
            "user_id": "4321",
            "text": "Review_text_example",
            "__class__": "Review"
        })
        self.assertEqual(my_review.id, "b21883f7-f591-4eba-8ea4-db95d345db77")
        self.assertEqual(my_review.user_id, "4321")
        self.assertEqual(my_review.created_at, datetime(
            2022, 3, 2, 12, 28, 19, 74340))
        self.assertNotEqual(my_review.__class__, "Review")
