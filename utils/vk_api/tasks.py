from vkwave_api import API, run


async def are_friends(access_token, user_id):
    api = API(access_token)
    friend_status = await api.get_api().users.get(user_ids=user_id, fields="friend_status", return_raw_response=True)
    friend_status = friend_status["response"][0]["friend_status"]
    await api.close()
    return friend_status == 1 or friend_status == 3


async def is_follower_of_group(access_token, group_id):
    api = API(access_token)
    is_member = await api.get_api().groups.is_member(group_id=group_id, return_raw_response=True)
    await api.close()
    return is_member["response"]


async def has_liked_post(access_token, owner_id, post_id):  # owner_id should be negative if group, positive if user
    api = API(access_token)
    is_liked = await api.get_api().likes.is_liked(type="post",
                                                  owner_id=owner_id,
                                                  item_id=post_id,
                                                  return_raw_response=True)
    await api.close()
    return is_liked["response"]["liked"]


async def has_copied_post(access_token, owner_id, post_id):
    api = API(access_token)
    is_liked = await api.get_api().likes.is_liked(type="post",
                                                  owner_id=owner_id,
                                                  item_id=post_id,
                                                  return_raw_response=True)
    await api.close()
    return is_liked["response"]["copied"]

async def main():
    test1 = await is_follower_of_group("86a50419c9888124ced2fb1b2f3f5bf9ffc5f97d78adac658495c5e3e227239720bcb99241c65087651ba",
                                      198971357)
    print(test1)
    test2 = await are_friends("86a50419c9888124ced2fb1b2f3f5bf9ffc5f97d78adac658495c5e3e227239720bcb99241c65087651ba",
                              258835738)
    print(test2)
    test3 = await has_liked_post("86a50419c9888124ced2fb1b2f3f5bf9ffc5f97d78adac658495c5e3e227239720bcb99241c65087651ba",
                                 owner_id=-39485893,
                                 post_id=15298)
    print(test3)
    test4 = await has_copied_post("86a50419c9888124ced2fb1b2f3f5bf9ffc5f97d78adac658495c5e3e227239720bcb99241c65087651ba",
                                  owner_id=-39485893,
                                  post_id=15298)
    print(test4)


if __name__ == "__main__":
    run(main())
