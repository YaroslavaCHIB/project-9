import re
import pandas as pd
import vk
import time

vk_session = vk.Session( access_token='cbbc066fd5c8e31fbd8c1470161840e0dcc8df26b1202ffe52ca7ada94fb461ca2b600e0112509d8fdee5')
api = vk.API(vk_session)

owner_id = ['88933032']


def get_post_id(owner_id):
    post_id = []
    for i in owner_id:
        post_id_tmp = api.wall.get(v ='5.21', owner_id = i)['items']
        post_id = post_id + post_id_tmp
        return post_id

def get_wall_posts(posts_id):
    wall_posts = api.wall.getById( v ='5.21', post_ids = posts_id)
    df = pd.DataFrame.from_dict(wall_posts, orient='columns')
    return df

w = get_post_id(owner_id)
print(get_wall_posts(w))