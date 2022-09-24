from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)


def upload_to_my_drive(filename):
    gfile = drive.CreateFile({"parents": [{"id": "1KT-ii7smXwwH2JVRCDRHZ2iER_ZesdGb"}]})
    # Read file and set it as the content of this instance.
    gfile.SetContentFile(filename)
    gfile.Upload()  # Upload the file.
