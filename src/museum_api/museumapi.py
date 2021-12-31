"""
    This module provides MuseumAPI class, which allows the user to fetch the data from
    Museum api through methods. The user doesn't need to know the urls of Museum API.
"""
import requests


class MuseumAPI:
    """
        MuseumAPI class allows you to easily get the objects from museum API through
        objects without knowing much details of the endpoints.
    """
    def __init__(self):
        self.base_url = 'https://collectionapi.metmuseum.org'

    def __fetch_response(self, endpoint, headers=None):
        """
        :param endpoint: api endpoint
        :param headers: headers to be sent in request
        :return: Response object
        """
        url = self.base_url + endpoint

        try:
            response = requests.get(url, headers=headers)
        except (requests.ConnectionError, requests.Timeout, requests.ConnectTimeout) as conn_error:
            raise conn_error
        except requests.HTTPError as http_error:
            raise http_error

        return response

    def get_all_object_ids(self, headers=None):
        """
        fetches all the object ids from the museum api.

        :param headers: headers to be sent in request
        :return: a dictionary with following keys -:
        * total: int
            count of number of objects fetched from museum api
        * objectIds: list
            list of all the object ids fetched from in museum
        """
        endpoint = '/public/collection/v1/objects'
        response = self.__fetch_response(endpoint, headers)
        if response.ok:
            return response.json()

        return None

    def get_object_for_id(self, object_id, headers=None):
        """
        fetches an object with specified object_id from museum api.

        :param object_id: object_id of the object to fetch data from museum api
        :param headers: headers to be sent in request
        :return: dictionary containing detail of the object.
        """

        endpoint = f'/public/collection/v1/objects/{str(object_id)}'
        response = self.__fetch_response(endpoint, headers)
        if response.ok:
            return response.json()

        return None
