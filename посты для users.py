import re
import pandas as pd
import vk
import time

vk_session = vk.Session(  access_token='cbbc066fd5c8e31fbd8c1470161840e0dcc8df26b1202ffe52ca7ada94fb461ca2b600e0112509d8fdee5')
api = vk.API(vk_session)

users_id = ['213037282', '88933032', '344210747', '139920164', '28698167', '112126728']

def get_wall(posts_id):
    wall = []
    for i in posts_id:
        wall_tmp = api.wall.get(v ='5.21', posts_id = i)['items']
        wall = wall + wall_tmp
    return wall

def get_wall_content(posts_id):
    wall_content = api.groups.getById(fields='activity', v ='5.21', posts_ids = posts_id)
    df = pd.DataFrame.from_dict(wall_content, orient='columns')
    #df.drop (['screen_name', 'is_closed', 'type', 'is_admin',
        #'admin_level', 'is_member', 'is_advertiser', 'photo_50',
        #'photo_100', 'photo_200', 'deactivated'], axis=1, inplace=True)
    return df

w = get_wall(posts_id)
print(get_wall_content(w))