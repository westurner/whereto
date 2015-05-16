#!/usr/bin/env python
from __future__ import print_function, division

import collections

import rdflib


def read_data(path, format="turtle"):
    """
    Read an RDFLib graph from the given path

    Arguments:
        path (str): path to a graph file

    Keyword Arguments:
        format (str): RDFLib format string (default="turtle")

    Returns:
        rdflib.Graph: a parsed rdflib.Graph

    """
    g = rdflib.Graph()
    g.parse(path, format=format)
    return g


def build_context_from_schema_graph(g):
    assert isinstance(g, rdflib.Graph)
    c = collections.OrderedDict()


