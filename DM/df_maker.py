import pandas
import os

dir_path = 'D:/Desktop/Hackathon/DisInformation-Challenge-Data/'
file_name_1 = 'Guardians_Russia_Ukraine.csv'


def return_df_from_csv(directory_path, file_name):
    return pandas.read_csv(filepath_or_buffer=directory_path + file_name, encoding="ISO-8859-1",
                           engine='python', memory_map=True, on_bad_lines='skip')


def return_df_list_from_directory(directory_path):
    tmp = []
    files = os.listdir(directory_path)
    for f in files:
        tmp.append(return_df_from_csv(directory_path=directory_path, file_name=f))
        print('Dodano df {} z {} --> {}'.format(files.index(f) + 1, len(files), f))
    return tmp


"""
a = return_df_from_csv(directory_path=dir_path, file_name=file_name_1)
b = return_df_from_csv(directory_path=dir_path, file_name='StandWithUkraine.csv')
c = return_df_from_csv(directory_path=dir_path, file_name='Russian_border_Ukraine.csv')
d = return_df_list_from_directory(directory_path=dir_path)
print('ok')
"""
