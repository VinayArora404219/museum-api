import logging
import os
import sys

import requests

from museumapi import MuseumAPI
from utils import Converter, flatten, setup_logger

# setting base directory as current directory.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# setting up logger for logging errors.
error_logger = setup_logger('main', 'logs/main_error.log', level=logging.ERROR)

if __name__ == '__main__':
    m = MuseumAPI()

    object_list = None
    for i in range(3):
        try:
            # getting all the objects ids from the museum api.
            object_ids = m.get_all_object_ids()['objectIDs'][0: 15]

            keys = ('constituents', 'measurements', 'tags')
            # getting list of detail of each object corresponding to their object ids.
            object_list = list(
                map(lambda object_id: flatten(m.get_object_for_id(object_id), keys), object_ids)
            )
            break

        except (requests.ConnectionError, requests.ConnectTimeout, requests.Timeout) as connError:
            error_logger.error("Connection error, Retrying (%i/3)" % (i + 1))
            if i == 3:
                error_logger.error(
                    "Maximum retires reached. Either server is not responding, or client is not connected to internet"
                )
                sys.exit(1)

        except Exception as e:
            error_logger.error(str(e))
            sys.exit(1)

    # extracting list of field names from object_list.
    field_names = object_list[0].keys()

    # directory in which reports will be generated.
    report_dir = os.path.join(BASE_DIR, 'reports/')

    # create reports directory if it doesn't exist.
    if os.path.isdir(report_dir):
        pass
    else:
        os.mkdir('reports')

    try:
        Converter.convert_to_csv(object_list, field_names, os.path.join(report_dir, 'museum_data.csv'))
        Converter.convert_to_excel(object_list, os.path.join(report_dir, 'museum_data.xlsx'))
        Converter.convert_to_html(object_list, os.path.join(report_dir, 'museum_data.html'))
        Converter.convert_to_xml(object_list, os.path.join(report_dir, 'museum_data.xml'))
        Converter.convert_to_pdf(object_list, os.path.join(report_dir, 'museum_data.pdf'))

    except Exception as e:
        error_logger.error("Error occurred :" + str(e))
        sys.exit(1)
