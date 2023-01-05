import os
import shutil

temp_dir = os.environ['TEMP']
downloads_dir = os.path.join(os.environ['USERPROFILE'], "Downloads")

quit = input("Do you want to delete all the temp files? (Press enter to continue)")

for file in os.listdir(temp_dir):
    file_path = os.path.join(temp_dir, file)
    try:
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)

    except PermissionError:
        pass


print("All the temp files were deleted.")

quit = input("Do you want to delete all the downloads? (Press enter to continue)")

for file in os.listdir(downloads_dir):
    file_path = os.path.join(downloads_dir, file)
    try:
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)

    except PermissionError:
        pass

print("All the downloaded files were deleted.")





