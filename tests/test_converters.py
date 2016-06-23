# coding=utf-8
"""
Unit tests for converters
David Megginson
June 2016

License: Public Domain
"""

import unittest

import hxl


class TaggerTest(unittest.TestCase):
    """Unit tests for hxl.converters.Tagger"""

    UNTAGGED = [
        ['Country Name', 'Country Code', '2016', '2015', '2014', '2013', '2012'],
        ['Sudan', 'SUD', '10000', '8500', '9000', '7500', '6000'],
        ['Syria', 'SYR', '100000', '85000', '90000', '75000', '60000'],
        ['Yemen', 'YEM', '50000', '43000', '45000', '38000', '30000']
    ]

    EXPECTED_TAGS_SIMPLE = ['#country+name', '#country+code', '', '', '', '', '']

    def setUp(self):
        pass

    def test_basic(self):
        """Basic tagging operation."""
        tagging_specs = [('Country Name', '#country+name'), ('Country Code', '#country+code')]
        source = hxl.data(hxl.converters.Tagger(self.UNTAGGED, tagging_specs))
        self.assertEqual(self.EXPECTED_TAGS_SIMPLE, source.display_tags)

    def test_case_insensitive(self):
        """Test that the tagger is case-insensitive."""
        tagging_specs = [('country name', '#country+name'), ('code', '#country+code')]
        source = hxl.data(hxl.converters.Tagger(self.UNTAGGED, tagging_specs))
        self.assertEqual(self.EXPECTED_TAGS_SIMPLE, source.display_tags)

    def test_space_insensitive(self):
        """Test that the tagger is whitespace-insensitive."""
        tagging_specs = [('  Country  Name', '#country+name'), ('Country    Code  ', '#country+code')]
        source = hxl.data(hxl.converters.Tagger(self.UNTAGGED, tagging_specs))
        self.assertEqual(self.EXPECTED_TAGS_SIMPLE, source.display_tags)

    def test_partial_match(self):
        """Test for substrings."""
        tagging_specs = [('name', '#country+name'), ('code', '#country+code')]
        source = hxl.data(hxl.converters.Tagger(self.UNTAGGED, tagging_specs))
        self.assertEqual(self.EXPECTED_TAGS_SIMPLE, source.display_tags)
        
    def test_full_match(self):
        """Test for substrings."""
        tagging_specs = [('country name', '#country+name'), ('code', '#country+code')]
        source = hxl.data(hxl.converters.Tagger(self.UNTAGGED, tagging_specs, allow_partial=False))
        self.assertEqual(['#country+name', '', '', '', '', '', ''], source.display_tags)
        
