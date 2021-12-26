import logging
import unittest
import os
import json

from museum_api.utils import Converter

logging.basicConfig(
     filename='logs/test_utils_error.log',
     level=logging.ERROR,
     format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )


class TestConverter(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = None # list of dicts to be converted to different formats
        cls.tmpdir = os.path.abspath('/tmp')
        cls.maxDiff = None

        try:
            with open('tmp/objects_list_for_conversion.json') as f:
                cls.data = json.load(f)

        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)

    def test_convert_to_csv(self):
        new_csv_file_name = 'museum_data.csv'
        new_csv_file_path = os.path.join(self.tmpdir, new_csv_file_name)
        Converter.convert_to_csv(self.data, new_csv_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/museum_data.csv'), 'r')\
                    as old_csv, open(new_csv_file_path) as newly_converted_csv:
                self.assertEqual(old_csv.read(), newly_converted_csv.read())
                
            # os.remove(new_csv_file_path)
        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)

    def test_convert_to_html(self):
        new_html_file_name = 'museum_data.html'
        new_html_file_path = os.path.join(self.tmpdir, new_html_file_name)
        Converter.convert_to_html(self.data, new_html_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/museum_data.html'), 'r')\
                    as old_html, open(new_html_file_path) as newly_converted_html:
                self.assertEqual(old_html.read(), newly_converted_html.read())
                os.remove(new_html_file_path)

        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)

    def test_convert_to_xml(self):
        new_xml_file_name = 'museum_data.xml'
        new_xml_file_path = os.path.join(self.tmpdir, new_xml_file_name)
        Converter.convert_to_xml(self.data, new_xml_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/museum_data.xml'), 'r')\
                    as old_xml, open(new_xml_file_path) as newly_converted_xml:
                self.assertEqual(old_xml.read(), newly_converted_xml.read())
                os.remove(new_xml_file_path)

        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)

    def test_convert_to_excel(self):
        new_xlsx_file_name = 'museum_data.xlsx'
        new_xlsx_file_path = os.path.join(self.tmpdir, new_xlsx_file_name)
        Converter.convert_to_excel(self.data, new_xlsx_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/museum_data.xlsx'),
                      'rb')\
                    as old_xlsx, open(new_xlsx_file_path, 'rb') as newly_converted_xlsx:
                self.assertEqual(old_xlsx.read(), newly_converted_xlsx.read())
                os.remove(new_xlsx_file_path)

        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)

    def test_convert_to_pdf(self):
        new_pdf_file_name = 'museum_data.pdf'
        new_pdf_file_path = os.path.join(self.tmpdir, new_pdf_file_name)
        Converter.convert_to_csv(self.data, new_pdf_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'correct_data/museum_data.pdf'), 'rb')\
                    as old_pdf, open(new_pdf_file_path, 'rb') as newly_converted_pdf:
                self.assertEqual(old_pdf.read(), newly_converted_pdf.read())
                os.remove(new_pdf_file_path)

        except FileNotFoundError as e:
            logging.error(f'File not found : {e.args[-1]}')
            exit(1)


if __name__ == '__main__':
    unittest.main()
