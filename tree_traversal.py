import os
import csv
import time

from tkinter.filedialog import askdirectory
from tkinter import *


class DirectoryTreeStructure:

    def __init__(self, save_flag=False):

        root=Tk()
        root.withdraw()


        self.file_structure = list()
        init_dir=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')


        self.start_directory = askdirectory(
            title='SELECT TOP DIRECTORY',
            initialdir=init_dir)

        self.save_structure_to_csv = save_flag


    def list_files(self):
        
        for root, dirs, all_dir_files in os.walk(self.start_directory):

            '''
            root: directory path
            dirs: directory name
            all_dir_files: all directory files
            '''

            level = root.replace(self.start_directory, '').count(os.sep)
            directory = os.path.basename(root)


            for dir_file in all_dir_files:

                file_path = os.path.join(root, dir_file)


                file_name = os.path.splitext(dir_file)[0]
                file_extension = os.path.splitext(dir_file)[1]
                file_size_bytes = os.stat(file_path).st_size


                file_date_created = os.path.getmtime(file_path)
                file_date_created = time.ctime(file_date_created)
                t_obj = time.strptime(file_date_created)
                file_date_created_formatted = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)


                file_info = (directory, level, root, file_name, file_extension, file_size_bytes, file_date_created_formatted)
                self.file_structure.append(file_info)




        if self.save_structure_to_csv:
            
            column_names = ['directory_name', 'directory_level_from_root', 'directory_path', 'file_name', 'file_extension', 'file_size (bytes)', 'date_created']
            
            
            # Specify the CSV file name
            filename = os.path.join(self.start_directory, 'directory_structure.csv')
            
            # Open the file in write mode ('w')
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)

                # Write the header row (optional)
                writer.writerow(column_names)

                # Write the data rows
                writer.writerows(self.file_structure[1:])



if __name__ == '__main__':
    dir_trav = DirectoryTreeStructure(save_flag=True)
    dir_trav.list_files()
