import vk
import pandas as pd

def vk_auth():
    vk_session = vk.Session(access_token='cbbc066fd5c8e31fbd8c1470161840e0dcc8df26b1202ffe52ca7ada94fb461ca2b600e0112509d8fdee5')
    api = vk.API(vk_session)
    return api

user_ids =[88933032, 260482658, 425750480, 523193937, 352169423, 321522398, 81083164, 238445718, 343507023, 184063229]


def get_information(user_ids):
    information_id = []
    for i in user_ids:
        information_id_tmp =  vk_auth().users.get(v ='5.95', user_ids = i, fields =  ('about', 'activities', 'bdate', 'city', 'country', 'home_town', 'occupation', 'personal', 'schools', 'sex'))
        information_id += information_id_tmp
    df = pd.DataFrame.from_dict(information_id, orient = 'columns')
    print(information_id)
    return df

df = get_information(user_ids)
print(df)
df.to_csv("C:\\Users\\teacher\\Desktop\\проект\\inform.csv")
df = df.isna()