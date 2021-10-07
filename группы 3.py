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
    user_id = []
    # group= vk_auth().groups.get(v ='5.21', user_id = id, extended = 1, fields = 'status')['items']
    for i in users_id:
        group_id_tmp = vk_auth().groups.get(v ='5.21', user_id = i)['items']
        group_id = group_id + group_id_tmp
        user_id = user_id + [i]*len(group_id)
    #df1 = pd.DataFrame.from_dict(user_id, orient='columns')
    df2 = pd.DataFrame.from_dict(group_id, orient='columns')
    #df1 = pd.concat([df1, df2], axis=1)
        #датафрейм с двумя колонками id пользователя и его групп
    return df2

users_id = [88933032, 260482658, 425750480, 523193937, 321522398, 81083164, 238445718, 343507023, 184063229]
#df1 = get_group_id(users_id)
df2 = get_group_id(users_id)
print(df2)
#df1.to_csv("C:\\Users\\teacher\\Desktop\\проект\\df.csv")
