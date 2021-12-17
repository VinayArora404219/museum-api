import requests


class MuseumAPI:
    def __init__(self, headers=None):
        """
        :param headers: dictionary containing headers
        """
        self.headers = headers
        self.base_url = 'https://collectionapi.metmuseum.org/public/collection/v1/'

    def __fetch_response(self, endpoint, headers=None):
        """
        :param endpoint: api endpoint
        :param headers: headers to be sent in request
        :return: Response object
        """
        url = self.base_url + endpoint

        try:
            response = requests.get(url, headers=headers)
        except (requests.ConnectionError, requests.Timeout, requests.ConnectTimeout) as e:
            raise e
        except requests.HTTPError as httpError:
            raise httpError

        return response

    def get_all_object_ids(self):
        """
        fetches all the object ids from the museum api.

        :return: a dictionary with following keys -:
        * total: int
            count of number of objects fetched from museum api
        * objectIds: list
            list of all the object ids fetched from in museum
        """
        endpoint = 'objects'
        return self.__fetch_response(endpoint).json()

    def get_object_for_id(self, object_id):
        """
        fetches an object with specified object_id from museum api.

        :param object_id: object_id of the object to fetch data from museum api
        :return: dictionary containing object detail with the following keys
        """

        endpoint = "objects/" + str(object_id)
        return self.__fetch_response(endpoint).json()
