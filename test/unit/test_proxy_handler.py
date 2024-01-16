import os
import unittest
from datetime import datetime
from unittest.mock import patch, Mock, MagicMock

import requests

from log.logger import Logger
from scraper.proxy.proxy_handler import ProxyHandler
from secrets import PROJECT_FOLDER


class TestProxyHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.handler = ProxyHandler("proxies_test.csv")

    def test_relative_build_path(self):
        """
        Ensures _build_path() returns correct absolute path for relative path input.
        :return: None
        """
        test_path = self.handler._build_path("proxies_test.csv")
        project_dir = os.getcwd().rsplit(PROJECT_FOLDER, 1)[0] + PROJECT_FOLDER
        absolute_path = project_dir + "\\scraper\\proxy\\proxies_test.csv"
        self.assertEqual(absolute_path, test_path)

    def test_absolute_build_path(self):
        """
        Ensures _build_path() returns correct absolute path for absolute path input.
        :return: None
        """
        project_dir = os.getcwd().rsplit(PROJECT_FOLDER, 1)[0] + PROJECT_FOLDER
        absolute_path = project_dir + "\\scraper\\proxy\\proxies_test.csv"
        test_path = self.handler._build_path(absolute_path)
        self.assertEqual(absolute_path, test_path)

    def test_load_proxies(self):
        """
        Ensures ProxyHandler.load_proxies() successfully constructs and loads IP:Port.
        :return: None
        """
        self.assertIn("103.84.134.1:1080", self.handler.proxies)

    @patch('scraper.proxy.proxy_handler.requests.get')
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

    @patch('scraper.proxy.proxy_handler.requests.get')
    def test_handle_proxy_failure(self, mock_requests_get):
        """
        Ensures RequestException Error is thrown and handled properly in handle_proxy()
        :param mock_requests_get: Mocks a request
        :return: None
        """
        mock_requests_get.side_effect = requests.RequestException("Error")
        result = self.handler.handle_proxy("invalid_proxy:port")
        self.assertIsNone(result)

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
