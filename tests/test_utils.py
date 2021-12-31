"""
    Tests for utils module.
"""

import sys
import hashlib
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
    """
    Class to test the functionality of all the functions of Converter
    class.
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        function to load temporary data in a member variable for testing.
        """
        cls.data = None # list of dicts to be converted to different formats
        cls.tmpdir = os.path.abspath('/tmp')
        cls.maxDiff = None

        try:
            with open('tmp/objects_list_for_conversion.json', encoding='utf-8') as file_ptr:
                cls.data = json.load(file_ptr)

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_csv(self):
        """
        function to test functionality of converting given data
        to csv file.
        """
        new_csv_file_name = 'museum_data.csv'
        new_csv_file_path = os.path.join(self.tmpdir, new_csv_file_name)
        Converter.convert_to_csv(self.data, new_csv_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/museum_data.csv'), 'r', encoding='utf-8')\
                    as old_csv,\
                    open(new_csv_file_path, 'r', encoding='utf-8') as newly_converted_csv:
                self.assertEqual(old_csv.read(), newly_converted_csv.read())
            # os.remove(new_csv_file_path)
        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_csv_when_list_of_dicts_is_invalid(self):
        """
        test failure of convert_to_csv function when list_of_dicts
        argument is invalid.
        """
        new_csv_file_name = 'museum_data.csv'
        new_csv_file_path = os.path.join(self.tmpdir, new_csv_file_name)
        list_of_dicts = None
        with self.assertRaises(TypeError):
            Converter.convert_to_csv(list_of_dicts, new_csv_file_path)

    def test_convert_to_csv_when_path_is_invalid(self):
        """
        test failure of convert_to_csv function when invalid path is
        specified.
        """
        new_csv_file_name = 'museum_data.csv'
        new_csv_file_path = os.path.join('abc', new_csv_file_name)
        with self.assertRaises(FileNotFoundError):
            Converter.convert_to_csv(self.data, new_csv_file_path)

    def test_convert_to_html(self):
        """
        function to test functionality of converting given data
        to html file.
        """
        new_html_file_name = 'museum_data.html'
        new_html_file_path = os.path.join(self.tmpdir, new_html_file_name)
        Converter.convert_to_html(self.data, new_html_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/museum_data.html'), 'r', encoding='utf-8')\
                    as old_html, \
                    open(new_html_file_path, 'r', encoding='utf-8') as newly_converted_html:
                self.assertEqual(old_html.read(), newly_converted_html.read())
                os.remove(new_html_file_path)

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_html_when_list_of_dicts_is_invalid(self):
        """
        test failure of convert_to_html function when list_of_dicts
        argument is invalid.
        """
        new_html_file_name = 'museum_data.html'
        new_html_file_path = os.path.join(self.tmpdir, new_html_file_name)
        list_of_dicts = None
        with self.assertRaises(TypeError):
            Converter.convert_to_html(list_of_dicts, new_html_file_path)

    def test_convert_to_html_when_path_is_invalid(self):
        """
        test failure of convert_to_html function when invalid path is
        specified.
        """
        new_html_file_name = 'museum_data.html'
        new_html_file_path = os.path.join('abc', new_html_file_name)
        with self.assertRaises(FileNotFoundError):
            Converter.convert_to_html(self.data, new_html_file_path)

    def test_convert_to_xml(self):
        """
        function to test functionality of converting given data
        to xml file.
        """
        new_xml_file_name = 'museum_data.xml'
        new_xml_file_path = os.path.join(self.tmpdir, new_xml_file_name)
        Converter.convert_to_xml(self.data, new_xml_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/museum_data.xml'), 'r', encoding='utf-8')\
                    as old_xml,\
                    open(new_xml_file_path, 'r', encoding='utf-8') as newly_converted_xml:
                self.assertEqual(old_xml.read(), newly_converted_xml.read())
                os.remove(new_xml_file_path)

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_xml_when_list_of_dicts_is_invalid(self):
        """
        test failure of convert_to_xml function when list_of_dicts
        argument is invalid.
        """
        new_xml_file_name = 'museum_data.xml'
        new_xml_file_path = os.path.join(self.tmpdir, new_xml_file_name)
        list_of_dicts = None
        with self.assertRaises(TypeError):
            Converter.convert_to_xml(list_of_dicts, new_xml_file_path)

    def test_convert_to_xml_when_path_is_invalid(self):
        """
        test failure of convert_to_xml function when invalid path is
        specified.
        """
        new_xml_file_name = 'museum_data.xml'
        new_xml_file_path = os.path.join('abc', new_xml_file_name)
        with self.assertRaises(FileNotFoundError):
            Converter.convert_to_xml(self.data, new_xml_file_path)

    def test_convert_to_excel(self):
        """
        function to test functionality of converting given data
        to excel file.
        """
        new_xlsx_file_name = 'museum_data.xlsx'
        new_xlsx_file_path = os.path.join(self.tmpdir, new_xlsx_file_name)
        Converter.convert_to_excel(self.data, new_xlsx_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/museum_data.xlsx'), 'rb')\
                    as old_xlsx, open(new_xlsx_file_path, 'rb') as newly_converted_xlsx:
                md5_old_xlsx_hash, md5_newly_converted_xlsx_hash = hashlib.md5(), hashlib.md5()
                md5_old_xlsx_hash.update(old_xlsx.read())
                md5_newly_converted_xlsx_hash.update(newly_converted_xlsx.read())
                digest_old_xlsx = md5_old_xlsx_hash.digest()
                digest_newly_generated_xlsx = md5_newly_converted_xlsx_hash.digest()

                self.assertEqual(digest_old_xlsx, digest_newly_generated_xlsx)
                os.remove(new_xlsx_file_path)

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_excel_when_list_of_dicts_is_invalid(self):
        """
        test failure of convert_to_excel function when list_of_dicts
        argument is invalid.
        """
        new_excel_file_name = 'museum_data.xlsx'
        new_excel_file_path = os.path.join(self.tmpdir, new_excel_file_name)
        list_of_dicts = None
        with self.assertRaises(TypeError):
            Converter.convert_to_excel(list_of_dicts, new_excel_file_path)

    def test_convert_to_excel_when_path_is_invalid(self):
        """
        test failure of convert_to_excel function when invalid path is
        specified.
        """
        new_excel_file_name = 'museum_data.xlsx'
        new_excel_file_path = os.path.join('abc', new_excel_file_name)
        with self.assertRaises(FileNotFoundError):
            Converter.convert_to_excel(self.data, new_excel_file_path)

    def test_convert_to_pdf(self):
        """
        function to test functionality of converting given data
        to pdf file.
        """
        new_pdf_file_name = 'museum_data.pdf'
        new_pdf_file_path = os.path.join(self.tmpdir, new_pdf_file_name)
        Converter.convert_to_csv(self.data, new_pdf_file_path)

        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   'correct_data/museum_data.pdf'), 'rb')\
                    as old_pdf, open(new_pdf_file_path, 'rb') as newly_converted_pdf:
                self.assertEqual(old_pdf.read(), newly_converted_pdf.read())
                os.remove(new_pdf_file_path)

        except FileNotFoundError as fn_fe:
            logging.error('File not found : %s', fn_fe.args[-1])
            sys.exit(1)

    def test_convert_to_pdf_when_list_of_dicts_is_invalid(self):
        """
        test failure of convert_to_pdf function when list_of_dicts
        argument is invalid.
        """
        new_pdf_file_name = 'museum_data.pdf'
        new_pdf_file_path = os.path.join(self.tmpdir, new_pdf_file_name)
        list_of_dicts = None
        with self.assertRaises(TypeError):
            Converter.convert_to_pdf(list_of_dicts, new_pdf_file_path)

    def test_convert_to_pdf_when_path_is_invalid(self):
        """
        test failure of convert_to_pdf function when invalid path is
        specified.
        """
        new_pdf_file_name = 'museum_data.pdf'
        new_pdf_file_path = os.path.join('abc', new_pdf_file_name)
        with self.assertRaises(FileNotFoundError):
            Converter.convert_to_pdf(self.data, new_pdf_file_path)


if __name__ == '__main__':
    unittest.main()
