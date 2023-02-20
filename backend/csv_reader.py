import pandas

directory_name = 'D:/Desktop/Hackathon/DisInformation-Challenge-Data/'
file_name = 'Guardians_Russia_Ukraine.csv'

def return_df_from_csv(directory_name, file_name):
    return pandas.read_csv(directory_name + file_name)


a = return_df_from_csv(directory_name=directory_name,file_name=file_name)
print('ok')