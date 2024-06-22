import zipfile
import os


class ZipBombMiddleware:
    MAX_FILE_SIZE = 1 * 1024 * 1024  # 1 MB
    MAX_EXTRACTED_FILES = 10

    def __init__(self, zip_file):
        self.zip_file = zip_file

    def extract(self, destination):
        zip_file_size = os.path.getsize(self.zip_file)
        if zip_file_size > self.MAX_FILE_SIZE:
            print("ZIP file size exceeds maximum allowed size. Extraction Stopped.")
            return

        with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
            num_files = len(zip_ref.infolist())
            print(f"Total number of files in the ZIP: {num_files}")
            if num_files >= self.MAX_EXTRACTED_FILES:
                print("Too many files for extract. Extraction Stopped.")
                return
            else:
                for file_info in zip_ref.infolist():
                    if file_info.file_size > self.MAX_FILE_SIZE:
                        print(f"File '{file_info.filename}' out of maximum allowed size. File Skipped.")
                        continue

                    zip_ref.extract(file_info, destination)
                    print(f"File '{file_info.filename}' extracted successfully.")

# zip_file = r"C:\Users\alnaseem\Downloads\ToppanBunkyuMidashiGothicStdN-ExtraBold.zip"
zip_file = r"C:\Users\alnaseem\Downloads\OnlineWebFonts_COM_3648bf8bc79b19d91ab22a318f93770b.zip"
destination = r"C:\Users\alnaseem\Downloads\EXT"

middleware = ZipBombMiddleware(zip_file)
middleware.extract(destination)
