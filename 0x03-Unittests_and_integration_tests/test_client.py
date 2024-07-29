#!/usr/bin/env python3
""" Unittest that test function and return from the functions"""

from unittest.mock import patch, MagicMock
import unittest
from parameterized import parameterized

from client import GithubOrgClient
from utils import get_json, access_nested_map, memoize
import requests
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])

    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns the correct value"""
        mock_response = {"repos_url": "https://api.github.com/orgs/{org}/repos"}
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org_name)
        result = client.org
        
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, mock_response)

    @patch.object(GithubOrgClient, 'org', new_callable=MagicMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url returns the correct URL"""
        mock_response = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }
        mock_org.return_value = mock_response

        client = GithubOrgClient("google")

        result = client._public_repos_url
        self.assertEqual(result, mock_response["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns the correct list of repos"""
        mock_payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "GPL"}},
            {"name": "repo3", "license": {"key": "MIT"}}
        ]
        mock_get_json.return_value = mock_payload

        with patch.object(GithubOrgClient, '_public_repos_url', new_callable=MagicMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient("google")

            result = client.public_repos()
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            result_with_license = client.public_repos(license="MIT")
            expected_repos_with_license = ["repo1", "repo3"]
            self.assertEqual(result_with_license, expected_repos_with_license)

            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license returns the correct boolean value"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
    {
        'org_payload': org_payload,
        'repos_payload': repos_payload,
        'expected_repos': expected_repos,
        'apache2_repos': apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up patchers and mocks for the test class"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if 'orgs/google' in url:
                mock_response = unittest.mock.Mock()
                mock_response.json.return_value = cls.org_payload
                return mock_response
            elif 'orgs/google/repos' in url:
                mock_response = unittest.mock.Mock()
                mock_response.json.return_value = cls.repos_payload
                return mock_response
            else:
                raise ValueError("Unexpected URL")

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patchers after tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos integration"""
        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license_filter(self):
        """Test GithubOrgClient.public_repos with license filter integration"""
        client = GithubOrgClient("google")
        result = client.public_repos(license="Apache-2.0")
        self.assertEqual(result, self.apache2_repos)
