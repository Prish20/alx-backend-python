#!/usr/bin/env python3
"""Unit tests for GithubOrgClient"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json", return_value={"login": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the expected value"""
        # Instantiate the GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org property (which internally calls get_json)
        result = client.org

        # Assert that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Assert that the result matches the mocked return value
        self.assertEqual(result, {"login": "mocked_org"})

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns
        the expected result based on the mocked payload"""
        # Mock the return value of org to a known payload
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/mock_org/repos"}

        # Instantiate the client
        client = GithubOrgClient("mock_org")

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Assert that the result matches the repos_url from the mocked payload
        self.assertEqual(result, "https://api.github.com/orgs/mock_org/repos")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos
        returns the expected list of repos"""
        # Mock the return value of get_json to simulate a list of repositories
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]

        # Mock the _public_repos_url property to return a specific URL
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = (
                "https://api.github.com/orgs/mock_org/repos"
            )

            # Instantiate the client
            client = GithubOrgClient("mock_org")

            # Call the public_repos method
            repos = client.public_repos()

            # Assert that the list of repos matches the expected result
            self.assertEqual(repos, ["repo1", "repo2"])

            # Assert that _public_repos_url and get_json were called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/mock_org/repos")


if __name__ == "__main__":
    unittest.main()
