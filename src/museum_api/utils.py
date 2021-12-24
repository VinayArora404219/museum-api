import os

import pandas as pd
import pdfkit
import csv
import logging


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
        df = pd.DataFrame(data=list_of_dicts)
        tmp_html_filename = 'tmp.html'
        df.to_html(tmp_html_filename)
        pdfkit.from_file(tmp_html_filename, output_path=path, options={
            'page-height': '1500',
            'page-width': '660',
        })
        os.remove(tmp_html_filename)

    @staticmethod
    def convert_to_xml(list_of_dicts, path):
        """
        Converts list of dictionary objects to xml

        :param list_of_dicts: list containing dictionary objects
        :param path: output path of the generated xml
        """
        df = pd.DataFrame(data=list_of_dicts)
        df.to_xml(path)

    @staticmethod
    def convert_to_html(list_of_dicts, path):
        """
        Converts list of dictionary objects to html

        :param list_of_dicts: list containing dictionary objects
        :param path: output path of the generated html
        """
        df = pd.DataFrame(data=list_of_dicts)
        df.to_html(path)

    @staticmethod
    def convert_to_excel(list_of_dicts, path):
        """
        Converts list of dictionary objects to excel

        :param list_of_dicts: list containing dictionary objects
        :param path: output path of the generated excel
        """
        df = pd.DataFrame(data=list_of_dicts)
        df.to_excel(path)

    @staticmethod
    def convert_to_csv(list_of_dicts, field_names, path):
        """
        Converts list of dictionary objects to csv

        :param list_of_dicts: list containing dictionary objects
        :param field_names: list of names of the fields
        :param path: output path of the generated csv
        """
        df = pd.DataFrame(data=list_of_dicts)
        df.to_csv(path)
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
                for k, v in value.items():
                    obj[k] = v
            del obj[key]
    # constituents = obj['constituents']
    # if constituents:
    #     for constituent in constituents:
    #         for key, value in constituent.items():
    #             obj[key] = value
    #     del obj['constituents']
    #
    # measurements = obj['measurements']
    # if measurements:
    #     for measurement in measurements:
    #         for key, value in measurement.items():
    #             obj[key] = value
    #
    #     del obj['measurements']
    #
    # tags = obj['tags']
    # if tags:
    #     for tag in tags:
    #         for key, value in tag.items():
    #             obj[key] = value
    #     del obj['tags']
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
