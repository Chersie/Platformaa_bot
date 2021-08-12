from vkwave_api import API, run


async def are_friends(follower_token, user_id):
    vk_api = API(follower_token)
    api = vk_api.get_api()
    follower_id = await api.users.get(return_raw_response=True)
    follower_id = follower_id["response"][0]["id"]
    are_friends_raw = await api.friends.are_friends(user_ids=(follower_id, user_id),
                                                    return_raw_response=True)
    friend_status = are_friends_raw["response"][0]["friend_status"]
    await vk_api.close()
    return friend_status == 3 or friend_status == 1  # пользователь в друзьях или же ему отправлена заявка


async def is_follower_of_group(follower_subscriptions, public_id):
    follower_group_subscriptions = follower_subscriptions["groups"]
    return public_id in follower_group_subscriptions


async def has_liked_post(access_token, owner_id, post_id):
    api = API(access_token)
    is_liked = await api.get_api().likes.is_liked(type="post",
                                                  owner_id=-owner_id,
                                                  item_id=post_id,
                                                  return_raw_response=True)
    await api.close()
    return is_liked["response"]["liked"]


async def has_copied_post(access_token, owner_id, post_id):
    api = API(access_token)
    is_liked = await api.get_api().likes.is_liked(type="post",
                                                  owner_id=-owner_id,
                                                  item_id=post_id,
                                                  return_raw_response=True)
    await api.close()
    return is_liked["response"]["copied"]

async def test(access_token, user_id):
    api = API(access_token)
    vk = api.get_api()
    friends_list = await vk.friends.get(user_id=265582492, return_raw_response=True)
    return friends_list

async def main():
    test123 = await test("d99f968706a51e7c447110532da8b557c02cb433aa8edf4b665b5c1c89b6db0847a8cb0811403963fd88a",
                         258835738)
    print(test123)
    await has_liked_post("785976a4581154ff1c244afd3ea75718cc4d77344fb3373287bf493ba10758ff6543a443342c1f1f04890",
                         182186143, 3498)


if __name__ == "__main__":
    run(main())
