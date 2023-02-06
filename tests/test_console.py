#!/usr/bin/python3

"""
Unittest for "console.py"
Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_console.py
"""

from models.user import User
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from unittest.mock import patch
from models import storage
import io
import unittest
from console import HBNBCommand
import console
import pycodestyle
import shutil
import os
import ast


class TestConsole(unittest.TestCase):
    """
    class that test console
    """
    path = "console.py"  # models/state.py
    file = os.path.splitext(path)[0].replace("/", ".")  # file to test
    list_function = [
        "create",
        "show",
        "destroy",
        "all",
        "count",
        "update",
    ]
    list_class = [
        "BaseModel",
        "User",
        "Amenity",
        "City",
        "Place",
        "Review",
        "State"
    ]

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files([self.path])
        self.assertEqual(
            result.total_errors, 0,
            f"Found code style errors (pycodestyle) in file test_console.py"
        )

    def test_documentation(self):
        """test all documentation of module"""
        # module documentation
        self.assertIsNotNone(
            console.__doc__,
            "Missing: module documentation of file \"console.py\"")

        # classes documentation
        for key, value in console.__dict__.items():
            if callable(value):
                self.assertIsNotNone(
                    value.__doc__, f"Missing: class documentation \
of class \"{value.__name__}\"")

        # functions documentation
        for key, value in console.__dict__.items():
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

    # test prompt
    def test_prompt(self):
        console = HBNBCommand()
        """This function test the prompt format"""
        self.assertEqual(console.prompt, "(hbnb) ")

    # test create and .create methods

    def test_create_basemodel(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), BaseModel)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_basemodel_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel etctectetc")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), BaseModel)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_basemodel_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), BaseModel)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_basemodel_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), BaseModel)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_user(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), User)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_user_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User etctectec")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), User)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_user_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), User)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_user_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("User.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), User)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_state(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), State)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_state_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State etcetetc")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), State)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_state_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), State)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_state_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("State.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), State)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_city(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), City)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_city_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City etcetcetc")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), City)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_city_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), City)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_city_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("City.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), City)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_amenity(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Amenity)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_amenity_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity etcetcetc")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Amenity)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_amenity_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Amenity)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_amenity_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Amenity)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_place(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Place)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_place_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place etcetcetc")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Place)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_place_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Place)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_place_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Place.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Place)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_review(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Review)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_review_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review etcetcetcetc")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Review)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_review_create(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Review)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_review_create_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review.create(etcetcetc)")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Review)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_review_create_etc_space(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("Review   .create  (   etcetcetc  )")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, storage.all().keys())
            self.assertEqual(
                type(storage._FileStorage__objects[className]), Review)
            self.assertIsInstance(
                storage._FileStorage__objects[className], BaseModel)

    def test_create_without_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create")
        output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_create_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    # test show method

    def test_all_show_BaseModel(self):
        for key_class in self.list_class:
            for key in range(7):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(f"create {key_class}")
                existing_id = f.getvalue().replace("\n", "")
                dict_valid_test = [
                    f'{key_class}.show("{existing_id}")',
                    f'{key_class}.show("{existing_id}" etcetc)',
                    f'{key_class}.show("{existing_id}" etcetc) etcetc',
                    f'{key_class}.show({existing_id} etcetc) etcetc',
                    f'show {key_class} "{existing_id}"',
                    f'show {key_class} "{existing_id}" etcetc',
                    f'show {key_class} {existing_id} etcetc',
                ]
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(dict_valid_test[key])
                output = f.getvalue()
                self.assertTrue(output)
                self.assertEqual(
                    output.replace("\n", ""),
                    storage._FileStorage__objects[
                        f'{key_class}.{existing_id}'
                    ].__str__()
                )

            # ** no instance found **
            dict_non_valid_test = [
                f'show {key_class} "not_existing_id"',
                f'{key_class}.show("not_existing_id")'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** no instance found **\n")

            # ** instance id missing **
            dict_non_valid_test = [
                f'show {key_class}',
                f'{key_class}.show()'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** instance id missing **\n")

            # ** class doesn't exist **
            dict_non_valid_test = [
                f'show Hello {existing_id}',
                f'Hello.show({existing_id})'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** class doesn't exist **\n")

            # ** class name missing **
            dict_non_valid_test = [
                f'show',
                f'.show()'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** class name missing **\n")

    def test_show_basemodel(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show BaseModel {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_basemodel_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show BaseModel {} etctectec".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_user(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show User {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_user_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show User {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_state(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show State {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_state_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show State {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_city(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show City {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_city_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show City {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_amenity(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Amenity {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_amenity_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Amenity {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_place(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Place {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_place_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Place {} etcetcetc".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_review(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Review {}".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show_review_etc(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            expected = storage._FileStorage__objects[className].__str__()
        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("show Review {} etetete".format(id))
            output = g.getvalue().strip()
            self.assertEqual(output, expected)

    def test_show(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show")
        output = f.getvalue()
        self.assertEqual(output, "** class name missing **\n")

    def test_show_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_show_without_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show User")
        output = f.getvalue()
        self.assertEqual(output, "** instance id missing **\n")

    def test_show_with_incorrect_id(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("show User 1212")
        output = f.getvalue()
        self.assertEqual(output, "** no instance found **\n")

    # test all method

    def test_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create State")
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            list_result.append(v.__str__())
        expected = (str(list_result) + "\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all")
        output = f.getvalue()
        self.assertEqual(output, expected)

        with patch('sys.stdout', new=io.StringIO()) as g:
            HBNBCommand().onecmd("all User")
        output_user = g.getvalue()
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            if isinstance(storage._FileStorage__objects[k], User):
                list_result.append(v.__str__())
        expected = (str(list_result)+"\n")
        self.assertEqual(output_user, expected)

        with patch('sys.stdout', new=io.StringIO()) as h:
            HBNBCommand().onecmd("all User blablabla")
        output_user = h.getvalue()
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            if isinstance(storage._FileStorage__objects[k], User):
                list_result.append(v.__str__())
        expected = (str(list_result)+"\n")
        self.assertEqual(output_user, expected)

        with patch('sys.stdout', new=io.StringIO()) as i:
            HBNBCommand().onecmd("          all      User")
        output_user = h.getvalue()
        list_result = []
        for k, v in storage._FileStorage__objects.items():
            if isinstance(storage._FileStorage__objects[k], User):
                list_result.append(v.__str__())
        expected = (str(list_result)+"\n")
        self.assertEqual(output_user, expected)

    def test_all_with_false_class(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("all Model")
        output = f.getvalue()
        self.assertEqual(output, "** class doesn't exist **\n")

    def test_user_all(self):
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("user.all")
        output = f.getvalue()
        self.assertEqual(output, "*** Unknow syntax: user.all\n")

    # test update method

    def test_all_update_BaseModel(self):
        dict_class = [
            "BaseModel",
            "User",
            "Amenity",
            "City",
            "Place",
            "Review",
            "State"
        ]

        list_attributes_str = [
            "email",
            "password",
            "first_name",
            "last_name",
            "name",
            "text",
            "place_id",
            "state_id",
            "city_id",
            "user_id",
            "description",
        ]

        list_attributes_int = [
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
        ]

        list_attributes_float = [
            "latitude",
            "longitude",
        ]
        list_attributes_list = [
            "amenity_ids"
        ]

        dict_int = {"attribute_name": 100}
        dict_float = {"attribute_name": 100.001}
        dict_str = {"attribute_name": "attribute name"}
        dict_many = {
            "attribute_name1": "attribute name",
            "attribute_name2": 100,
            "attribute_name3": 100.001
        }
        for key_class in self.list_class:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd(f"create {key_class}")
            existing_id = f.getvalue().replace("\n", "")
            dict_valid_test = [
                f'{key_class}.update("{existing_id}", \
"attribute_name", "100")',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "100.001")',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "string_value")',
                f'{key_class}.update({existing_id}, \
attribute_name, string_value)',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "composed string value")',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "composed string value") etcetcetc',
                f'{key_class}.update("{existing_id}", \
"attribute_name", "composed string value")',
                f'{key_class}.update("{existing_id}", {dict_int})',
                f'{key_class}.update("{existing_id}", {dict_str})',
                f'{key_class}.update("{existing_id}", {dict_float})',
                f'{key_class}.update("{existing_id}", {dict_many})',
                f'{key_class}.update("{existing_id}", {dict_many}) etcetcetc',
                f'update {key_class} "{existing_id}" \
"attribute_name" "string_value"',
                f'update {key_class} "{existing_id}" \
"attribute_name" "string_value"',
                f'update {key_class} "{existing_id}" \
"attribute_name" "composed string value" etcetcetc',
                f'update {key_class} "{existing_id}" \
"attribute_name" "100"',
                f'update {key_class} "{existing_id}" \
"attribute_name" "100.001"',
                f'update {key_class} {existing_id} \
attribute_name string_value'
            ]
            for key in dict_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertFalse(output)
                self.assertEqual(
                    existing_id,
                    storage._FileStorage__objects[
                        f"{key_class}.{existing_id}"
                    ].id
                )

            # ** no instance found **
            dict_non_valid_test = [
                f'update {key_class} "not_existing_id" \
"attribute_name" "string_value"',
                f'{key_class}.update("not_existing_id", \
"attribute_name", "string_value")'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** no instance found **\n")

            # ** instance id missing **
            dict_non_valid_test = [
                f'update {key_class}',
                f'{key_class}.update()'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** instance id missing **\n")

            # ** attribute name missing **
            dict_non_valid_test = [
                f'update {key_class} {existing_id}',
                f'{key_class}.update({existing_id})'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** attribute name missing **\n")

            # ** value missing **
            dict_non_valid_test = [
                f'update {key_class} {existing_id} "attribute_name"',
                f'{key_class}.update({existing_id}, "attribute_name")'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** value missing **\n")

            # ** class doesn't exist **
            dict_non_valid_test = [
                f'update Hello {existing_id} "attribute_name"',
                f'Hello.update({existing_id}, "attribute_name")'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** class doesn't exist **\n")

            # ** class name missing **
            dict_non_valid_test = [
                f'update',
                f'.update()'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** class name missing **\n")

            # test updated attribue
            for key_class in dict_class:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(f"create {key_class}")
                id = f.getvalue().replace("\n", "")
                key_instance = f"{key_class}.{id}"
                instance = storage.all()[key_instance]
                updated_at_value = instance.updated_at
                for attribute in list_attributes_str:
                    if (hasattr(instance, attribute)):
                        if getattr(instance, attribute) == "":
                            HBNBCommand().onecmd(
                                f"update {key_class} {id} \
{attribute} updated_name")
                            self.assertTrue(getattr(instance, attribute) != "")
                            self.assertTrue(
                                type(getattr(instance, attribute)) == str)
                            self.assertEqual(
                                getattr(instance, attribute), "updated_name")
                            self.assertNotEqual(
                                updated_at_value, instance.updated_at)
                        else:
                            HBNBCommand().onecmd(
                                f"update {key_class} {id} \
{attribute} updated_name")
                            self.assertEqual(
                                getattr(instance, attribute), "updated_name")
                            self.assertTrue(
                                type(getattr(instance, attribute)) == str)
                            self.assertNotEqual(
                                updated_at_value, instance.updated_at)
                for attribute in list_attributes_int:
                    if (hasattr(instance, attribute)):
                        if getattr(instance, attribute) == "":
                            HBNBCommand().onecmd(
                                f"update {key_class} {id} {attribute} 89")
                            self.assertTrue(getattr(instance, attribute) != "")
                            self.assertTrue(
                                type(getattr(instance, attribute)) == int)
                            self.assertEqual(getattr(instance, attribute), 89)
                            self.assertNotEqual(
                                updated_at_value, instance.updated_at)
                        else:
                            HBNBCommand().onecmd(
                                f"update {key_class} {id} {attribute} 89")
                            self.assertEqual(getattr(instance, attribute), 89)
                            self.assertTrue(
                                type(getattr(instance, attribute)) == int)
                            self.assertNotEqual(
                                updated_at_value, instance.updated_at)
                for attribute in list_attributes_float:
                    if (hasattr(instance, attribute)):
                        if getattr(instance, attribute) == "":
                            HBNBCommand().onecmd(
                                f"update {key_class} {id} {attribute} 3.5")
                            self.assertTrue(getattr(instance, attribute) != "")
                            self.assertTrue(
                                type(getattr(instance, attribute)) == float)
                            self.assertEqual(getattr(instance, attribute), 3.5)
                            self.assertNotEqual(
                                updated_at_value, instance.updated_at)
                        else:
                            HBNBCommand().onecmd(
                                f"update {key_class} {id} {attribute} 3.5")
                            self.assertEqual(getattr(instance, attribute), 3.5)
                            self.assertTrue(
                                type(getattr(instance, attribute)) == float)
                            self.assertNotEqual(
                                updated_at_value, instance.updated_at)

    # test help command
    def test_help_create(self):
        for key_class in self.list_function:
            with patch('sys.stdout', new=io.StringIO()) as f:
                HBNBCommand().onecmd(f"help {key_class}")
            output = f.getvalue()
            self.assertTrue(output)

    # test destroy method

    def test_all_destroy_BaseModel(self):
        for key_class in self.list_class:
            for key in range(7):
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(f"create {key_class}")
                existing_id = f.getvalue().replace("\n", "")
                dict_valid_test = [
                    f'{key_class}.destroy("{existing_id}")',
                    f'{key_class}.destroy("{existing_id}" etcetc)',
                    f'{key_class}.destroy("{existing_id}" etcetc) etcetc',
                    f'{key_class}.destroy({existing_id} etcetc) etcetc',
                    f'destroy {key_class} "{existing_id}"',
                    f'destroy {key_class} "{existing_id}" etcetc',
                    f'destroy {key_class} {existing_id} etcetc',
                ]
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(dict_valid_test[key])
                output = f.getvalue()
                self.assertFalse(output)
                self.assertNotIn(existing_id, storage._FileStorage__objects)

            # ** no instance found **
            dict_non_valid_test = [
                f'destroy {key_class} "not_existing_id"',
                f'{key_class}.destroy("not_existing_id")'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** no instance found **\n")

            # ** instance id missing **
            dict_non_valid_test = [
                f'destroy {key_class}',
                f'{key_class}.destroy()'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** instance id missing **\n")

            # ** class doesn't exist **
            dict_non_valid_test = [
                f'destroy Hello {existing_id}',
                f'Hello.destroy({existing_id})'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** class doesn't exist **\n")

            # ** class name missing **
            dict_non_valid_test = [
                f'destroy',
                f'.destroy()'
            ]
            for key in dict_non_valid_test:
                with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(key)
                output = f.getvalue()
                self.assertEqual(output, "** class name missing **\n")

# test count command

    def test_count_function(self):
        for key_class in self.list_class:
            with patch('sys.stdout', new=io.StringIO()) as f:
                    HBNBCommand().onecmd(f"{key_class}.count()")
            output = f.getvalue().replace("\n", "")
            self.assertTrue(output)
            self.assertIsInstance(int(output), int)
            self.assertGreaterEqual(int(output), 0)
