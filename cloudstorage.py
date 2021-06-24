import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AyEW9_dilV8BuImk8tyDUWOchSxPwpGxYKbNn8KBJNM_zqAd5-RoYwS3fuJEXKCGAyCm0cv2HFrtnrMyD-7frScIro9rnP9m4hDHKedKVvUouwjPaNnI9EfilSnKS05r2D_M5-2mRRM'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("file uploaded")

main()

