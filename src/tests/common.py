# coding: utf-8

import unittest
import mock

from po_file_checker.base import (
    entries_with_missing_translations,
    missing_keys
)


class CommonTestCase(unittest.TestCase):
    def test_gettings_translations(self):
        pofile = [
            mock.Mock(translated=lambda: True),
            mock.Mock(translated=lambda: False),
            mock.Mock(translated=lambda: True),
        ]
        elements = entries_with_missing_translations(pofile)
        self.assertFalse(elements.next().translated())
        self.assertRaises(StopIteration, lambda: elements.next())

    def test_missing_keys(self):
        key_name = 'surrogate_key'
        pofile = [
            mock.Mock(translated=lambda: False, msgid=key_name, msgid_plural=key_name),
        ]
        elements = list(missing_keys(pofile))
        self.assertEqual(len(elements), 1)
        self.assertEqual(elements[0], key_name)
