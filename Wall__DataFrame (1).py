import re
import pandas as pd
import vk
import time

vk_session = vk.Session( access_token='cbbc066fd5c8e31fbd8c1470161840e0dcc8df26b1202ffe52ca7ada94fb461ca2b600e0112509d8fdee5')
api = vk.API(vk_session)

owner_id =['88933032', '260482658']


def get_post_id(owner_id):
    post_id = []
    for i in owner_id:
        post_id_tmp = api.wall.get(v ='5.21', owner_id = i)['items']
        post_id += post_id_tmp
    df = pd.DataFrame.from_dict(post_id, orient = 'columns')
    df.drop(['from_id', 'likes', 'reposts', 'attachments', 'date', 'copy_history', 'post_source', 'comments', 'post_type'], axis=1, inplace=True)
    return df       
       
    

print (get_post_id(owner_id))

