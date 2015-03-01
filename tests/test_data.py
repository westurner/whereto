
import os
import unittest

import whereto.data as data


def get_path(*path):
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, *path)


class TestWhereToData(unittest.TestCase):
    def test_read_data(self):
        filepath = get_path('data', 'local', 'data.ttl')
        output = data.read_data(filepath)
        self.assertTrue(output)
        import rdflib
        self.assertIsInstance(output, rdflib.Graph)
        self.assertGreater(len(output), 0)
