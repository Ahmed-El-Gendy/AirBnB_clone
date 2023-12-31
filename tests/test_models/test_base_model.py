#!/usr/bin/python3
"""
test for class  base model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for class base model"""
    def test_init(self):
        """test init"""
        the_model = BaseModel()
        self.assertIsNotNone(the_model.updated_at)
        self.assertIsNotNone(the_model.created_at)
        self.assertIsNotNone(the_model.id)

    def test_str(self):
        """test method  str"""
        the_model = BaseModel()
        self.assertTrue(str(the_model).startswith('[BaseModel]'))
        self.assertIn(the_model.id, str(the_model))
        self.assertIn(str(the_model.__dict__), str(the_model))

    def test_dict(self):
        """test method  dict"""
        the_model = BaseModel()
        the_dict = the_model.to_dict()
        t1 = the_dict["updated_at"]
        t2 = the_dict["created_at"]
        self.assertEqual(the_model.updated_at.isoformat(), t1)
        self.assertEqual(the_model.created_at.isoformat(), t2)
        self.assertIsInstance(the_dict, dict)
        self.assertEqual('BaseModel', the_dict["__class__"])
        self.assertEqual(the_model.id, the_dict["id"])

    def test_save(self):
        """test method save"""
        the_model = BaseModel()
        before_update = the_model.updated_at
        now_update = the_model.save()
        self.assertNotEqual(now_update, before_update)


if __name__ == "__main__":
    unittest.main()
