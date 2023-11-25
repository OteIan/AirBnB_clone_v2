import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsoleCreateCommand(unittest.TestCase):
    def setUp(self):
        """Set up the test environment"""
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()

    def tearDown(self):
        """Clean up the test environment"""
        self.console.do_EOF(None)
        self.console = None

    def capture_output(self, command):
        """Capture the output of the console for a given command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            return mock_stdout.getvalue()

    def test_create_with_string_parameter(self):
        """Test create command with string parameter"""
        out = self.capture_output('create BaseModel name="My_little_house"\n')
        self.assertIn("My little house", out)

    def test_create_with_float_parameter(self):
        """Test create command with float parameter"""
        output = self.capture_output('create BaseModel value=3.14\n')
        self.assertIn("3.14", output)

    def test_create_with_integer_parameter(self):
        """Test create command with integer parameter"""
        output = self.capture_output('create BaseModel count=42\n')
        self.assertIn("42", output)

    def test_create_with_invalid_parameter(self):
        """Test create command with invalid parameter"""
        output = self.capture_output('create BaseModel invalid_param=abc\n')
        self.assertIn("Invalid parameter", output)


if __name__ == '__main__':
    unittest.main()
