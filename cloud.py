import dropbox

try:
    dbx = dropbox.Dropbox('8LuAcZYm8OsAAAAAAAAAAYNygi2UMMcIkIBKvf__1kbvQL62ah2FZY_JKla5oGIx')
    print("connected")
except Exception as e:
    print(e)


def file_search(name):
    for entry in dbx.files_list_folder('').entries:
        print(entry)
    #     if name == entry.name:
    #         i = i + 1
    # if i > 0:
    #     return True
    # else:
    #     return False


# try:
#     print(file_search("ar.cpp"))
# except Exception as e:
#     print(e)


def upload(file_path):
    dbx.files_upload(bytes(file_path, 'utf-8'), file_path)
    return 'done'