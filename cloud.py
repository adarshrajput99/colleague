import dropbox

try:
    dbx = dropbox.Dropbox('DROPBOX API TOKEN')

except Exception as e:
    print(e)


# UPLOADING A FILE
def upload(file_path):
    print(dbx.files_upload(bytes(file_path, 'utf-8'), file_path))


# searching a file
def search(file_name):
    x = []
    x = file_name
    result = dbx.files_list_folder("", recursive=True)
    file_list = []

    def process_entries(entries):
        for entry in entries:
            file_list.append([entry.name])

    process_entries(result.entries)

    while result.has_more:
        result = dbx.files_list_folder_continue(result.cursor)

        process_entries(result.entries)
    check = False
    for i in file_list:
        for y in i:
            if x == y:
                print("found")
                check = True
                break
        if check:
            break
    else:
        print("not found")


# download
def download(file):
    print(dbx.files_download(path="/home/adarshsingh/" + file))
