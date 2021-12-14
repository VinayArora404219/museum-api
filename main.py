import logging
import os
from museumapi import MuseumAPI
from utils import Generator, flatten

logging.basicConfig(filename='main.log', filemode='w', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.DEBUG)


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    m = MuseumAPI()
    object_ids = m.get_all_objects()['objectIDs'][0: 15]

    object_list = [flatten(m.get_object_for_id(object_id)) for object_id in object_ids]
    field_names = object_list[0].keys()

    report_dir = os.path.join(BASE_DIR, 'reports/')
    if os.path.isdir(report_dir):
        # checking if reports directory exists
        pass
    else:
        os.mkdir('reports')

    try:
        Generator.generate_csv(object_list, field_names, os.path.join(report_dir, 'museum_data.csv'))
        Generator.generate_excel(object_list, os.path.join(report_dir, 'museum_data.xlsx'))
        Generator.generate_html(object_list, os.path.join(report_dir, 'museum_data.html'))
        Generator.generate_xml(object_list, os.path.join(report_dir, 'museum_data.xml'))
        Generator.generate_pdf(object_list, os.path.join(report_dir, 'museum_data.pdf'))

    except FileNotFoundError as e:
        logging.error(str(e))

    except Exception as e:
        logging.error(str(e))
