#!/usr/bin/python3
"""defines uinttest for console.py"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import sys
import os


class TestHBNBCommand_prompt(unittest.TestCase):
    """Unittests for testing prompt interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help interpreter."""

    def test_help(self):
        hlp = "ctrl+z"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(hlp, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """Unittests for testing exiting interpreter."""

    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """testing create method"""

    def test_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(correct, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
