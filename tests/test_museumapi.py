"""
    Tests for museumapi module.
"""

import json
import logging
import unittest
import os
import sys
from unittest.mock import patch, Mock

from museum_api.museumapi import MuseumAPI

logging.basicConfig(
     filename='logs/test_museumapi_error.log',
     level=logging.ERROR,
     format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )


class TestMuseumAPI(unittest.TestCase):
    """
    Tests functionality of MuseumAPI class.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        sets up mAPIObj to be used in all the test functions.
        """
        cls.mAPIObj = MuseumAPI()

    @patch('museum_api.museumapi.requests.get')
    def test_getting_object_ids_when_response_is_ok(self, mock_get):
        """
        Tests getting object ids from museum API when response is ok.
        :param mock_get: mocked method get of requests module.
        """
        actual_object_ids_data = None
        tmp_object_ids_data = None
        # getting mocked data from the file
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/object_ids_resp.json'), 'r', encoding='utf-8') \
                    as data:
                actual_object_ids_data = json.load(data)

            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/object_ids_resp.json'), 'r', encoding='utf-8') \
                    as data:
                tmp_object_ids_data = json.load(data)

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a dictionary object.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = tmp_object_ids_data

        # Call the service, which will send a request to the server.
        mocked_object_ids_data = self.mAPIObj.get_all_object_ids()

        # If the request is sent successfully, then I expect a response to be returned.
        self.assertDictEqual(mocked_object_ids_data, actual_object_ids_data)

    @patch('museum_api.museumapi.requests.get')
    def test_getting_object_ids_when_response_is_not_ok(self, mock_get):
        """
        Tests getting object ids from museum API when response is not ok.
        :param mock_get: mocked method get of requests module.
        """
        # Configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        object_ids_data = self.mAPIObj.get_all_object_ids()

        # If the response contains an error, I should get no todos.
        self.assertIsNone(object_ids_data)

    @patch('museum_api.museumapi.requests.get')
    def test_getting_object_when_response_is_ok(self, mock_get):
        """
        Tests getting object from museum API when response is ok.
        :param mock_get: mocked method get of requests module.
        """
        mocked_object_data = None
        tmp_object_data = None
        # getting mocked data from the file
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/object_resp.json'), 'r', encoding='utf-8') \
                    as data:
                actual_object_data = json.load(data)

            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/object_ids_resp.json'), 'r', encoding='utf-8')\
                    as data:
                tmp_object_data = json.load(data)

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a dictionary object.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = tmp_object_data

        # Call the service, which will send a request to the server.
        mocked_object_data = self.mAPIObj.get_object_for_id(1)

        # If the request is sent successfully, then I expect a response to be returned.
        self.assertDictEqual(mocked_object_data, actual_object_data)

    @patch('museum_api.museumapi.requests.get')
    def test_getting_object_when_response_is_not_ok(self, mock_get):
        """
        Tests getting object from museum API when response is not ok.
        :param mock_get: mocked method get of requests module.
        """
        # Configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        object_data = self.mAPIObj.get_object_for_id(1)

        # If the response contains an error, It must return None.
        self.assertIsNone(object_data)


if __name__ == '__main__':
    unittest.main()
