#!/usr/bin/env python3
"""Unit tests for get_json"""

import unittest
from unittest.mock import patch, Mock
from utils import get_json
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test that get_json returns the expected result"""
        # Create a Mock response object with a .json() method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Assert the mock get method was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Assert the result matches the expected payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
