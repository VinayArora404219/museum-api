import logging
import smtplib
import socket
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
import os
from museum_api.utils import setup_logger
import shutil
from dotenv import load_dotenv

load_dotenv()

error_logger = setup_logger('mail', 'logs/mail_error.log', level=logging.ERROR)


def send_email(from_email, to_email, password, subject='', body='', attachment_file_paths=None):
    """
    function to send an email to specified email address.

    :param from_email: sender email address.
    :param to_email: receiver email address.
    :param password: sender password.
    :param subject: subject of the email.
    :param body: body of the email.
    :param attachment_file_paths: list of file paths of the files to be sent as an attachment.
    """
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = from_email

    # storing the receivers email address
    msg['To'] = to_email

    # storing the subject
    msg['Subject'] = subject

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    if attachment_file_paths is not None:
        for attachment_file_path in attachment_file_paths:

            # mime = MimeTypes()
            # url = pathlib.Path(attachment_file_path).as_uri()
            mime_type = str(mimetypes.guess_type(attachment_file_path)[0])
            main_type, sub_type = mime_type.split('/')

            # instance of MIMEBase and named as p
            p = MIMEBase(main_type, sub_type)
            try:
                with open(attachment_file_path, 'r', encoding='utf-8') as file:
                    p.set_payload(file.read())
            except FileNotFoundError as fn_fe:
                error_logger.error(
                    "Error opening file %s %s",
                    attachment_file_path,
                    fn_fe.args[-1]
                )
            except UnicodeDecodeError:
                with open(attachment_file_path, 'rb') as file:
                    p.set_payload(file.read())

            # encode into base64
            encoders.encode_base64(p)

            file_name = os.path.basename(attachment_file_path)

            p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

            # attach the instance 'p' to instance 'msg'
            msg.attach(p)

    try:
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(from_email, password)

        # Converts the Multipart msg into a string
        text = msg.as_string()

        # sending the mail
        s.sendmail(from_email, to_email, text)

        # terminating the session
        s.quit()
    except socket.gaierror as e:
        logging.error("%s while sending email to %s", e.args[-1], from_email)


def generate_zip(source_dir, target_path):
    """
    Generates a zip file from a given directory.

    :param source_dir: path of source directory.
    :param target_path: path where the new zip file must be generated
    """

    if os.path.exists(source_dir):
        if os.path.isdir(source_dir):
            shutil.make_archive(target_path, 'zip', source_dir)


def unzip_file(source_file, target_dir):
    """
    function to unzip a given file.

    :param source_file: path of the zip file.
    :param target_dir: path where the file must be unzipped.
    """

    if os.path.exists(source_file) and os.path.exists(target_dir):
        if os.path.isdir(target_dir):
            with zipfile.ZipFile(source_file, 'r') as zip_ref:
                zip_ref.extractall(target_dir)


# generate_zipfile(os.path.join(os.getcwd(), 'reports'), os.path.join(os.getcwd(), 'reports'))
# unzip_file(os.path.join(os.getcwd(), 'reports.zip'), os.path.join(os.getcwd(), 'tmp'))

# send_email(os.environ.get('SENDER_EMAIL'),
#            'vinayarora404219@gmail.com',
#            os.environ.get('PASSWORD'),
#            'Museum API Reports',
#            'Please take a look at the generated reports.',
#            [
#                 os.path.join(os.getcwd(), 'reports/museum_data.csv'),
#                 os.path.join(os.getcwd(), 'reports/museum_data.html'),
#                 os.path.join(os.getcwd(), 'reports/museum_data.xml'),
#                 os.path.join(os.getcwd(), 'reports/museum_data.xlsx'),
#                 os.path.join(os.getcwd(), 'reports/museum_data.pdf')
#            ])
