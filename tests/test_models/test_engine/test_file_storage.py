#!/usr/bin/python3
"""
This is unit test for test File_storge
"""

import unittest
from models.base_model import BaseModel
import datetime
import models


class Test_FileStorage(unittest.TestCase):
    """
    This is Test class for the
    Test of FileStorage class
    """

    def test_test_file_storage(self):
        """_summary_
        Check if the model key in the
        __objects attribute after using
        the new method
        """

        base = BaseModel()
        models.storage.save()
        key = f"BaseModel.{base.id}"
        obj = models.storage.all()[key]
        self.assertTrue(isinstance(obj, BaseModel))

    def test_test_file_storage(self):
        """_summary_
        Check the equality of the created model
        and the model in the __objects attribute
        """

        base1 = BaseModel()
        base2 = BaseModel()
        models.storage.save()
        key1 = f"BaseModel.{base1.id}"
        key2 = f"BaseModel.{base2.id}"
        obj1 = models.storage.all()[key1]
        obj2 = models.storage.all()[key2]
        self.assertNotEqual(obj1, obj2)

    def test_test_file_storage_obj(self):
        """_summary_
        Check the equality of the created model
        and the model in the __objects attribute
        """

        base1 = BaseModel()
        base2 = BaseModel()
        models.storage.save()
        key1 = f"BaseModel.{base1.id}"
        key2 = f"BaseModel.{base2.id}"
        dic = models.storage.all()
        self.assertTrue(isinstance(dic, dict))

    def test_test_file_new_save(self):
        """_summary_
        Check if the model key in the
        __objects attribute after using
        the new method
        """

        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        key = f"BaseModel.{base.id}"
        self.assertTrue(key in models.storage.all().keys())
