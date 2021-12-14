import os

import pandas as pd
import pdfkit
import csv


class Generator:
    @staticmethod
    def generate_pdf(list_of_dicts, path):
        df = pd.DataFrame(data=list_of_dicts)
        tmp_html_filename = 'tmp.html'
        df.to_html(tmp_html_filename)
        pdfkit.from_file(tmp_html_filename, output_path=path)
        os.remove(tmp_html_filename)

    @staticmethod
    def generate_xml(list_of_dicts, path):
        df = pd.DataFrame(data=list_of_dicts)
        df.to_xml(path)

    @staticmethod
    def generate_html(list_of_dicts, path):
        df = pd.DataFrame(data=list_of_dicts)
        df.to_html(path)

    @staticmethod
    def generate_excel(list_of_dicts, path):
        df = pd.DataFrame(data=list_of_dicts)
        df.to_excel(path)

    @staticmethod
    def generate_csv(list_of_dicts, field_names, path):
        with open(path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for obj in list_of_dicts:
                d = {key: value for key, value in obj.items() if key in field_names}
                writer.writerow(d)


def flatten(obj):
    constituents = obj['constituents']
    if constituents:
        for constituent in constituents:
            for key, value in constituent.items():
                obj[key] = value
        del obj['constituents']

    measurements = obj['measurements']
    if measurements:
        for measurement in measurements:
            for key, value in measurement.items():
                obj[key] = value

        del obj['measurements']

    tags = obj['tags']
    if tags:
        for tag in tags:
            for key, value in tag.items():
                obj[key] = value
        del obj['tags']
    return obj