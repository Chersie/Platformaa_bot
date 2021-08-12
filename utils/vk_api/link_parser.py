
def link_to_token(link: str):
    token_start = link.find("access_token=") + 13
    token_end = link.find("&", token_start)
    if token_end < 0:
        token_end = len(link)
    return link[token_start:token_end]

if __name__ == "__main__":
    token = link_to_token("https://oauth.vk.com/close.html#access_token=5024980d74947b336cf99d360777df2fea9dfe3807e7baa81d463926919e63a29d46d410eaa83c511edf1&expires_in=0&user_id=258835738")
    print(token)
