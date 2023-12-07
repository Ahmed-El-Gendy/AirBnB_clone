#!/usr/bin/python3
"""
test base model
"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        the_model = BaseModel()
        self.assertIsNotNone(the_model.updated_at)
        self.assertIsNotNone(the_model.created_at)
        self.assertIsNotNone(the_model.id)

    def test_str(self):
        the_model = BaseModel()
        #self.assertTrue(str(the_model).startswith('[BaseModel]'))
        #self.assertIn(the_model.id, str(the_model))
        #self.assertIn(str(the_model.__dict__), str(the_model))

    def test_dict(self):
        the_model = BaseModel()
        the_dict = the_model.to_dict()
        self.assertEqual(the_model.updated_at.isoformat(), the_dict["updated_at"])
        self.assertEqual(the_model.created_at.isoformat(), the_dict["created_at"])
        self.assertIsInstance(the_dict, dict)
        self.assertEqual('BaseModel', the_dict["__class__"])
        self.assertEqual(the_model.id, the_dict["id"])

    def test_save(self):
        the_model = BaseModel()
        before_update = the_model.updated_at
        now_update = the_model.save()
        self.assertNotEqual(now_update, before_update)

if __name__ == "__main__":
    unittest.main()
