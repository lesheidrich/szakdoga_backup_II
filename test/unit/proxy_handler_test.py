"""
Module: test_proxy_handler.py

This module contains unit tests for the ProxyHandler class, ensuring that methods
related to handling and processing proxies function correctly.

Classes:
- TestProxyHandler: A unittest.TestCase class for testing ProxyHandler functionality.

Methods:
- setUp(): Initializes a ProxyHandler instance for testing purposes.
- test_relative_build_path(): Ensures _build_path() returns the correct absolute path for
  relative path input.
- test_absolute_build_path(): Ensures _build_path() returns the correct absolute path for
  absolute path input.
- test_load_proxies(): Ensures ProxyHandler.load_proxies() successfully constructs and loads
  IP:Port.
- test_handle_proxy_success(): Tests the successful run of handle_proxy() with mock data.
- test_handle_proxy_failure(): Ensures RequestException Error is thrown and handled properly
  in handle_proxy().
- test_process_proxies(): Test run on proxies_test.csv. Both functions used are tested
  separately as well.

Note: Some tests involve the use of mocking to simulate external dependencies such as requests.
"""
import unittest
from unittest.mock import patch, Mock
import project_secrets
import requests
from webscraper.proxy.proxy_handler import ProxyHandler


class TestProxyHandler(unittest.TestCase):
    """
    class: TestProxyHandler
    Unit tests for the ProxyHandler class.

    These tests cover the functionality of the ProxyHandler class, ensuring that methods
    related to handling and processing of proxies function correctly.

    Methods:
    - setUp(): Initializes a ProxyHandler instance for testing purposes.
    - test_relative_build_path(): Ensures _build_path() returns the correct absolute path for
      relative path input.
    - test_absolute_build_path(): Ensures _build_path() returns the correct absolute path for
      absolute path input.
    - test_load_proxies(): Ensures ProxyHandler.load_proxies() successfully constructs and loads
      IP:Port.
    - test_handle_proxy_success(): Tests the successful run of handle_proxy() with mock data.
    - test_handle_proxy_failure(): Ensures RequestException Error is thrown and handled properly
      in handle_proxy().
    - test_process_proxies(): Test run on proxies_test.csv. Both functions used are tested
      separately as well.

    Note: Some tests involve the use of mocking to simulate external dependencies such as requests.
    """
    def setUp(self) -> None:
        self.handler = ProxyHandler("proxies_test.csv")

    def test_relative_build_path(self):
        """
        Ensures _build_path() returns correct absolute path for relative path input.
        :return: None
        """
        test_path = self.handler._build_path("proxies_test.csv")
        absolute_path = project_secrets.get_project_folder() + "\\webscraper\\proxy\\proxies_test.csv"
        self.assertEqual(absolute_path, test_path)

    def test_absolute_build_path(self):
        """
        Ensures _build_path() returns correct absolute path for absolute path input.
        :return: None
        """
        absolute_path = project_secrets.get_project_folder() + "\\webscraper\\proxy\\proxies_test.csv"
        test_path = self.handler._build_path(absolute_path)
        self.assertEqual(absolute_path, test_path)

    def test_load_proxies(self):
        """
        Ensures ProxyHandler.load_proxies() successfully constructs and loads IP:Port.
        :return: None
        """
        self.assertIn("103.84.134.1:1080", self.handler.proxies)

    @patch('webscraper.proxy.proxy_handler.requests.get')
    def test_handle_proxy_success(self, mock_requests_get):
        """
        Tests successful run of handle_proxy() with mock data.
        :param mock_requests_get: Mocks a request
        :return: None
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "unit_test_success"
        mock_requests_get.return_value = mock_response
        result = self.handler.handle_proxy("unit_test_ip")
        self.assertEqual(result, "unit_test_ip")

    @patch('webscraper.proxy.proxy_handler.requests.get')
    def test_handle_proxy_failure(self, mock_requests_get):
        """
        Ensures RequestException Error is thrown and handled properly in handle_proxy()
        :param mock_requests_get: Mocks a request
        :return: None
        """
        mock_requests_get.side_effect = requests.RequestException("Error")
        result = self.handler.handle_proxy("invalid_proxy:port")
        self.assertEqual(result, "")

    def test_process_proxies(self):
        """
        Test run on proxies_test.csv. Both functions used are tested separately as well.
        :return: None
        """
        return_list = self.handler.process_proxies()
        comment = " - APP_LOG - INFO - CURRENT WORKING PROXY LIST"
        result = self.handler.log.check_comment_for_timestamp(comment)
        self.assertTrue(result)
        self.assertIsNotNone(return_list)
