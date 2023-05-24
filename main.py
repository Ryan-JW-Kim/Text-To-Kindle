from converter import *
# from email_manager import *

KINDLE_EMAIL_DESTINATION = ""
SOURCE_EMAIL = ""
SOURCE_EMAIL_PASSWORD = ""
SMTP_SERVER = ""


def main():
    path="..\Light-Novel-Text-Extraction\downloaded_2023-05-20_15-45-38"
    TextToPdf(path, combine_all=True)

if __name__ == '__main__':
    main()