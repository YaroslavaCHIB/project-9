import vk

access_token = "409f9528809d38c810"
session = vk.Session(access_token=access_token)
vkapi = vk.API(session)
def getUserId(link):
    id = link
    if 'vk.com/' in link: #  проверяем эту ссылку
        id = link.split('/')[-1]  # если да, то получаем его последнюю часть
    if not id.replace('id', '321522398').isdigit(): # если в нем после отсечения 'id' сами цифры - это и есть id 
        id = vkapi.utils.resolveScreenName(screen_name=id)['object_id'] # если нет, получаем id с помощью метода API
    else:
        id = id.replace('id', '')
    return int(id)
    # count это количество запросов (и количество постов = 100 * count постов)
def getLikes(user_id, cnt, vkapi):
    import time
    # подписки пользователя
    subscriptions_list = vkapi.users.getSubscriptions(user_id=user_id,extended=0)['groups']['items']
    # формируем список id, который нужно передать в следующий метод
    groups_list = ['-' + str(x) for x in subscriptions_list]
    posts = {}
    # формируем ленту новостей
    newsfeed = vkapi.newsfeed.get(
        filters='post',
        source_ids=', '.join(groups_list),
        count=100, timeout=10)
    # добавляем посты в словарь в формате id_поста: id_группы
    posts.update({x['post_id']: x['source_id'] for x in newsfeed['items']})
    # нужно для получения следующей партии
    # если требуется более одного запроса — делаем остаток в цикле
    if cnt != 1:
        for c in range(cnt - 1):
            next_from = newsfeed['new_from']
            kwargs = {
                'from': next_from,
                'filters': 'post',
                'source_ids': ', '.join(groups_list),
                'count': 100,
                'timeout': 10
            }
            newsfeed = vkapi.newsfeed.get(**kwargs)

            posts.update({x['post_id']: x['source_id'] for x in newsfeed['items']})
            time.sleep(1)
    liked_posts = []

    print('Лайкнутые посты:')
    for post in posts.items():
        try:
            itemID = post[0]
            ownerID = post[1]
            timeOut = 5
            isLiked = vkapi.likes.isLiked(
                user_id=user_id,
                item_id=itemID,
                type='post',
                owner_id=ownerID,
                timeout=timeOut)
        except Exception:
#             print('ERROR! ' + 'vk.com/wall{0}_{1}'.format(post[1], post[0]))
            isLiked = 0

        if isLiked:
            liked_posts.append('vk.com/wall{0}_{1}'.format(post[1], post[0]))
            print('vk.com/wall{}_{}'.format(post[1], post[0]))
            time.sleep(1)
    return liked_posts




