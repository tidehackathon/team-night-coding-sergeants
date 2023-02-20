import pandas as pd

directory_name = 'D:/Desktop/Hackathon/DisInformation-Challenge-Data/'
file_name = 'Guardians_Russia_Ukraine.csv'

df = pd.read_csv(directory_name + file_name)

print(df.to_string())


def return_df_from_csv(directory_name, file_name):
    return pd.read_csv(directory_name + file_name)
