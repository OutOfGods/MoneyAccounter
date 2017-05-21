import unittest
from io import StringIO

import pickle_serialization
import json_serialization
import yaml_serialization


class SerializationTest(unittest.TestCase):
    test_str = "Test_test_123123123"

    def test_pickle_save(self):
        outfile = StringIO()
        pickle_serialization.serialize(self.test_str, outfile.)
        outfile.seek(0)
        content = outfile.read()
        self.assertEquals(content, self.test_str)

    def test_json_save(self):
        outfile = StringIO()
        json_serialization.serialize(self.test_str, outfile)
        outfile.seek(0)
        content = outfile.read()
        self.assertEquals(content, self.test_str)

    def test_yaml_save(self):
        outfile = StringIO()
        yaml_serialization.serialize(self.test_str, outfile)
        outfile.seek(0)
        content = outfile.read()
        self.assertEquals(content, self.test_str)


