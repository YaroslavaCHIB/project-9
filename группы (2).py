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
        #df1 = pd.DataFrame.from_dict(i, orient='columns')

        #датафрейм с двумя колонками id пользователя и его групп
    return group_id
#print(df1)

def f(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

#users_id = [88933032, 260482658, 425750480, 523193937, 3691898, 213037282, 28698167, 60669834, 69888678] 
users_id = [88933032, 260482658, 425750480, 523193937, 321522398, 81083164, 238445718, 343507023, 184063229]

# id друзей для 88933032 (915 id получается)
# lst = vk_auth().friends.get(v ='5.95', user_id=88933032)['items']

# получаем список id групп для пользователей users_id (спискок выше)
groups_id = get_group_id(users_id)
# сколько id групп лежит в этом списке? функция len()
print(len(groups_id))

# разделяем список id групп на группы по 400 записей (так как groups.getById за раз принимает не больше 500 групп)
c = f(groups_id, 400)
print(len(c))

# считываем информацию групп
g = []
for i in c:
    time.sleep(30)
    group_content = vk_auth().groups.getById(fields=['activity','description'], v ='5.21', group_ids = i)
    print(len(group_content))
    g += group_content
print(len(g))
df = pd.DataFrame.from_dict(g, orient='columns')
df.drop(['screen_name', 'photo_100', 'photo_200', 'deactivated', 'is_closed', 'type', 'is_admin','is_advertiser', 'photo_50', 'is_member' ], axis=1, inplace=True)
#df.drop([ 'screen_name', 'is_closed', 'type', 'is_admin','admin_level', 'is_member', 'is_advertiser', 'photo_50', 'photo_100', 'photo_200', 'deactivated'], axis=1, inplace=True)
print(df)
#df.to_csv("C:\\Users\\teacher\\Desktop\\проект\\neyron.csv")
#df.to_csv("C:\\Users\\teacher\\Desktop\\проект\\newgr.csv")
