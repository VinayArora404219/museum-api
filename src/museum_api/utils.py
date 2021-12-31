"""
    utils module provides various utility methods to transform data from one
    form to another.
"""

import logging
import os

import pandas as pd
import pdfkit


class Converter:
    """
    Converter class to convert a list of dictionary objects to various formats
    """

    @staticmethod
    def convert_to_pdf(list_of_dicts, path):
        """
        Converts list of dictionary objects to pdf

        :param list_of_dicts: list containing dictionary objects
        :param path: output path of the generated pdf
        """
        if list_of_dicts is None:
            raise TypeError("list_of_dicts cannot be None")

        if not isinstance(list_of_dicts, list) or not isinstance(list_of_dicts[0], dict):
            raise TypeError("list_of_dicts must be a list of dictionaries")

        if path is None:
            raise TypeError("path cannot be None")

        if not os.path.exists(path):
            raise FileNotFoundError(f'File {path} not found')

        dataframe = pd.DataFrame(data=list_of_dicts)
        tmp_html_filename = 'tmp.html'
        dataframe.to_html(tmp_html_filename)
        pdfkit.from_file(tmp_html_filename, output_path=path, options={
            'page-height': '2500',
            'page-width': '1270',
        })
        os.remove(tmp_html_filename)

    @staticmethod
    def convert_to_xml(list_of_dicts, path):
        """
        Converts list of dictionary objects to xml

        :param list_of_dicts: list containing dictionary objects
        :param path: output path of the generated xml
        """
        if list_of_dicts is None:
            raise TypeError("list_of_dicts cannot be None")

        if not isinstance(list_of_dicts, list) or not isinstance(list_of_dicts[0], dict):
            raise TypeError("list_of_dicts must be a list of dictionaries")

        if path is None:
            raise TypeError("path cannot be None")

        dataframe = pd.DataFrame(data=list_of_dicts)
        dataframe.to_xml(path, index=False)

    @staticmethod
    def convert_to_html(list_of_dicts, path):
        """
        Converts list of dictionary objects to html

        :param list_of_dicts: list containing dictionary objects
        :param path: output path of the generated html
        """
        if list_of_dicts is None:
            raise TypeError("list_of_dicts cannot be None")

        if not isinstance(list_of_dicts, list) or not isinstance(list_of_dicts[0], dict):
            raise TypeError("list_of_dicts must be a list of dictionaries")

        if path is None:
            raise TypeError("path cannot be None")

        dataframe = pd.DataFrame(data=list_of_dicts)
        dataframe.to_html(path, index=False)

    @staticmethod
    def convert_to_excel(list_of_dicts, path):
        """
        Converts list of dictionary objects to excel

        :param list_of_dicts: list containing dictionary objects
        :param path: output path of the generated excel
        """
        if list_of_dicts is None:
            raise TypeError("list_of_dicts cannot be None")

        if not isinstance(list_of_dicts, list) or not isinstance(list_of_dicts[0], dict):
            raise TypeError("list_of_dicts must be a list of dictionaries")

        if path is None:
            raise TypeError("path cannot be None")

        dataframe = pd.DataFrame(data=list_of_dicts)
        dataframe.to_excel(path, index=False)

    @staticmethod
    def convert_to_csv(list_of_dicts, path):
        """
        Converts list of dictionary objects to csv

        :param list_of_dicts: list containing dictionary objects
        :param field_names: list of names of the fields
        :param path: output path of the generated csv
        """
        if list_of_dicts is None:
            raise TypeError("list_of_dicts cannot be None")

        if not isinstance(list_of_dicts, list) or not isinstance(list_of_dicts[0], dict):
            raise TypeError("list_of_dicts must be a list of dictionaries")

        if path is None:
            raise TypeError("path cannot be None")

        dataframe = pd.DataFrame(data=list_of_dicts)
        dataframe.to_csv(path, index=False)
        # with open(path, 'w') as csvfile:
        #     writer = csv.DictWriter(csvfile, fieldnames=field_names)
        #     writer.writeheader()
        #     for obj in list_of_dicts:
        #         d = {key: value for key, value in obj.items() if key in field_names}
        #         writer.writerow(d)


def flatten(obj, keys):
    """
    flattens the dictionary object specified in the argument

    :param obj: object to be flattened
    :param keys: list of keys which are not flattened by default
    :return: reference of flattened object
    """
    for key in keys:
        values = obj[key]
        if values:
            for value in values:
                for k, sub_value in value.items():
                    obj[k] = sub_value
            del obj[key]
    return obj


def setup_logger(module_name,
                 log_file,
                 log_format=logging.Formatter('%(asctime)s %(levelname)s %(message)s'),
                 level=logging.INFO):
    """
    for setting up multiple loggers easily

    :param module_name: name of the module to generate logs for
    :param log_file: path of the file to generate the logs
    :param log_format: format of the log
    :param level: log level
    :return:
    """

    handler = logging.FileHandler(log_file)
    handler.setFormatter(log_format)

    logger = logging.getLogger(module_name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
