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
    for i in users_id:
        group_id_tmp = vk_auth().groups.get(v ='5.21', user_id = i)['items']
        group_id = group_id + group_id_tmp
    return group_id

def f(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

users_id = [88933032, 260482658, 425750480, 523193937, 321522398, 81083164, 238445718, 343507023, 184063229]


groups_id = get_group_id(users_id)
print(len(groups_id))

c = f(groups_id, 400)
print(len(c))

g = []
for i in c:
    time.sleep(30)
    group_content = vk_auth().groups.getById(fields=['activity','description'], v ='5.21', group_ids = i)
    print(len(group_content))
    g += group_content
print(len(g))
df = pd.DataFrame.from_dict(g, orient='columns')
df.drop(['screen_name', 'photo_100', 'photo_200', 'deactivated', 'is_closed', 'type', 'is_admin','is_advertiser', 'photo_50', 'is_member' ], axis=1, inplace=True)
print(df)
df.to_csv("C:\\Users\\teacher\\Desktop\\проект\\groups1.csv")
