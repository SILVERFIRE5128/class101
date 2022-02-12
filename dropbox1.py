import dropbox

class TransferData:
    def __init__ (self,access_token):
        self.access_token = access_token
    def upload_file (self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open (file_from,'rb') as f:
            dbx.files_upload(f.read().file_to)

def main ():
    access_token = 'sl.BB5IwPJWYSGGA_FDXSFkjgIubzPg-5o6scGySwlJ4OBkv4e_my2p6jYjMgWeXsIsxgHtyKO3BbUODdvcyZU5ukljFNncFUjxETPXFo7QqJNmFNR1wYoElPSjoPyUWXOE3PQ_44c'
    transferdata = TransferData (access_token)
    files_from = input("enter the file path to transfer.")
    files_to = input("enter the full path")

    transferdata.upload_file(files_from,files_to)
    print("files have moved.")


main ()