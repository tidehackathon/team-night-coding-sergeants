import pandas
import os

dir_path = 'D:/Desktop/Hackathon/DisInformation-Challenge-Data/'
file_name_1 = 'Guardians_Russia_Ukraine.csv'
exclusion_list = ['Russia_invade.csv', 'Ukraine_nato.csv', 'StandWithUkraine.csv', 'Ukraine_border.csv', 'Ukraine_troops.csv',
                  'Ukraine_war.csv']


def return_df_from_csv(directory_path, file_name):
    df = pandas.read_csv(filepath_or_buffer=directory_path + file_name, sep=',', encoding="utf-8",
                         engine='python-fwf')
    return df


def return_df_list_from_directory(directory_path):
    tmp = []
    files = os.listdir(directory_path)
    for f in files:
        tmp.append(return_df_from_csv(directory_path=directory_path, file_name=f))
        print('Dodano df: ', f)
    return tmp


# a = return_df_from_csv(directory_path=dir_path, file_name='StandWithUkraine.csv')
b = return_df_list_from_directory(directory_path=dir_path)
print('ok')
