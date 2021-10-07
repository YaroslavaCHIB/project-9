import vk_api

vk_session = vk_api.VkApi('+79165295797', 'ELINA2004P')
vk_session.auth()

vk = vk_session.get_api()

print(vk.account.getProfileInfo(id=321522398))