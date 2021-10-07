import json
import vk
import pandas as pd
import time

def vk_auth():
    vk_session = vk.Session(access_token='cbbc066fd5c8e31fbd8c1470161840e0dcc8df26b1202ffe52ca7ada94fb461ca2b600e0112509d8fdee5')
    api = vk.API(vk_session)
    return api

def get_group_id(users_id):
    group_id = []
    # group= vk_auth().groups.get(v ='5.21', user_id = id, extended = 1, fields = 'status')['items']
    for i in users_id:
        group_id_tmp = vk_auth().groups.get(v ='5.21', user_id = i)['items']
        group_id = group_id + group_id_tmp
        df1 = pd.DataFrame.from_dict(i, orient='columns')
        #датафрейм с двумя колонками id пользователя и его групп
    return group_id
print(df1)