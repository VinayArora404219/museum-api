import json
import logging
import unittest
import os
from unittest.mock import patch, Mock
from unittest import skipIf

from museum_api.museumapi import MuseumAPI

logging.basicConfig(
     filename='logs/test_museumapi_error.log',
     level=logging.ERROR,
     format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )


class TestMuseumAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.mAPIObj = MuseumAPI()

    # def test_get_all_object_ids(self):
    #     # Call the service to hit the actual API.
    #     actual_object_ids_dict = self.mAPIObj.get_all_object_ids()
    #     self.assertIsNotNone(actual_object_ids_dict)
    #
    #     actual_keys = actual_object_ids_dict.keys()
    #
    #     # getting mock data from the file
    #     mocked_object_ids_data = None
    #     try:
    #         with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/object_ids_resp.json'),
    #                   'r') as data:
    #             mocked_object_ids_data = json.load(data)
    #
    #     except FileNotFoundError as e:
    #         logging.error(f'File not found : {e.args[-1]}')
    #         exit(1)
    #     # Call the service to hit the mocked API.
    #     with patch('museum_api.museumapi.requests.get') as mock_get:
    #         mock_get.return_value.ok = True
    #         mock_get.return_value.json.return_value = mocked_object_ids_data
    #
    #         mocked_keys = self.mAPIObj.get_all_object_ids().keys()
    #
    #     # An object from the actual API and an object from the mocked API should have
    #     # the same data structure.
    #     self.assertListEqual(list(actual_keys), list(mocked_keys))
    #
    # def test_get_object_for_id(self):
    #     # Call the service to hit the actual API.
    #     actual_object_dict = self.mAPIObj.get_object_for_id(1)
    #     self.assertIsNotNone(actual_object_dict)
    #
    #     actual_keys = actual_object_dict.keys()
    #
    #     # getting mock data from the file
    #     mocked_object_data = None
    #     # getting mocked data from the file
    #     try:
    #         with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/object_resp.json'),
    #                   'r') as data:
    #             mocked_object_data = json.load(data)
    #
    #     except FileNotFoundError as e:
    #         logging.error(f'File not found : {e.args[-1]}')
    #         exit(1)
    #     # Call the service to hit the mocked API.
    #     with patch('museum_api.museumapi.requests.get') as mock_get:
    #         mock_get.return_value.ok = True
    #         mock_get.return_value.json.return_value = mocked_object_data
    #
    #         mocked_keys = self.mAPIObj.get_all_object_ids().keys()
    #
    #     # An object from the actual API and an object from the mocked API should have
    #     # the same data structure.
    #     self.assertListEqual(list(actual_keys), list(mocked_keys))
















    @patch('museum_api.museumapi.requests.get')
    def test_getting_object_ids_when_response_is_ok(self, mock_get):
        actual_object_ids_data = None
        tmp_object_ids_data = None
        # getting mocked data from the file
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/object_ids_resp.json'), 'r') \
                    as data:
                actual_object_ids_data = json.load(data)

            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/object_ids_resp.json'), 'r') as data:
                tmp_object_ids_data = json.load(data)

        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)

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
        # Configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        object_ids_data = self.mAPIObj.get_all_object_ids()

        # If the response contains an error, I should get no todos.
        self.assertIsNone(object_ids_data)

    @patch('museum_api.museumapi.requests.get')
    def test_getting_object_when_response_is_ok(self, mock_get):
        mocked_object_data = None
        # getting mocked data from the file
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/object_resp.json'),
                      'r') as data:
                mocked_object_data = json.load(data)

        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns a dictionary object.
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = mocked_object_data

        # Call the service, which will send a request to the server.
        actual_object_data = self.mAPIObj.get_object_for_id(1)

        # If the request is sent successfully, then I expect a response to be returned.
        self.assertDictEqual(mocked_object_data, actual_object_data)

    @patch('museum_api.museumapi.requests.get')
    def test_getting_object_when_response_is_not_ok(self, mock_get):
        # Configure the mock to not return a response with an OK status code.
        mock_get.return_value.ok = False

        # Call the service, which will send a request to the server.
        object_data = self.mAPIObj.get_object_for_id(1)

        # If the response contains an error, It must return None.
        self.assertIsNone(object_data)


if __name__ == '__main__':
    unittest.main()
