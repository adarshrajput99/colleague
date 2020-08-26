import dropbox

try:
    dbx = dropbox.Dropbox('L1i-SBazcXAAAAAAAAAAAZd856weXa23bGA_6Cn-E1nsRbOCjmeowIPnNK3Kh2uN')
    print("connected")
except Exception as e:
    print(e)


def upload(file_path):
    dbx.files_upload(bytes(file_path, 'utf-8'), file_path)
