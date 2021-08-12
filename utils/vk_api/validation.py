
from vkwave_api import API, run

api = API(token="ae1b0d5b7ca93d7751291e3e237a7fd98457dc92b9dc7d0f9fcc92038595b7258a210a0d28b5ab5b90b51")
vk = api.get_api()


async def friend_count():
    friend_list = await vk.friends.get(return_raw_response=True)
    return friend_list["response"]["count"]

async def subscriber_count():
    subscriber_list = await vk.users.get_followers(return_raw_response=True)
    return subscriber_list["response"]["count"]

async def has_profile_picture():
    profile_photos = await vk.photos.get(return_raw_response=True,
                                  album_id="profile")
    return profile_photos["response"]["count"] > 0


async def is_valid():
    is_valid = (await friend_count() > 48) and (await subscriber_count() > 11) \
           and await has_profile_picture()
    return is_valid

if __name__ == "__main__":
    run(is_valid())



