import logging
import requests
import sys

logging.basicConfig(filename='main.log', filemode='w', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.DEBUG)


class MuseumAPI:
    def __init__(self, headers=None):
        """
        :param headers: dictionary containing headers
        """
        self.headers = headers
        self.base_url = 'https://collectionapi.metmuseum.org/public/collection/v1/'

    def fetch_response(self, endpoint, headers=None):
        """
        :param endpoint: api endpoint
        :param headers: headers to be sent in request
        :return:
        """
        response = None
        url = self.base_url + endpoint
        if headers is None:
            headers = self.headers
        try:
            response = requests.get(url, headers=headers)
        except (requests.ConnectionError, requests.Timeout) as e:
            logging.exception("Connection error or Request Timed Out: {}".format(e.args[-1]))
            sys.exit(1)
        except requests.HTTPError as httpError:
            logging.exception("HTTP Error. Status Code: {}. Error: {}".format(response.status_code, httpError.args[-1]))
            sys.exit(1)
        finally:
            logging.info("Response Status: {}".format(response.status_code))
            return response

    def get_all_objects(self):
        """
        :return: {
            objectIDs: list,
            total: int
        }
        """
        endpoint = 'objects'
        return self.fetch_response(endpoint).json()

    def get_object_for_id(self, object_id):
        """
        :param object_id: object_id of the object to get data
        :return: dictionary containing object detail
        """

        endpoint = "objects/" + str(object_id)
        return self.fetch_response(endpoint).json()
