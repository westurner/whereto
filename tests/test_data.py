
import logging
import os
import unittest

import rdflib

import whereto.data as data


def get_path(*path):
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, *path)


class TestWhereToData(unittest.TestCase):
    def test_read_whereto_schema(self):
        filepath = get_path('..', 'whereto', 'ns', 'whereto.ttl')
        output = data.read_data(filepath)
        self.assertTrue(output)
        self.assertIsInstance(output, rdflib.Graph)
        self.assertGreater(len(output), 0)

    def test_read_local_data(self):
        filenames = [get_path('data', 'local', x) for x in
                     os.listdir(get_path('data', 'local'))
                     if x.endswith('.ttl')]
        for filepath in filenames:
            logging.info(filepath)
            output = data.read_data(filepath)
            self.assertTrue(output)
            self.assertIsInstance(output, rdflib.Graph)
            self.assertGreater(len(output), 0)
