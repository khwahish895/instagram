from instabot import Bot
bot=Bot()
bot.login(username="khwahish5632",password="KHWAHISH")
bot.follow('meendinesh11')
bot.upload_photo("C:/Users/91960/PycharmProjectsPythonProject11/python.jpg",caption="i like python")
bot.unfollow("meendinesh11")
bot.send_message("i love python",["meendinesh11"])
followers=bot.get_user_followers("khwahish5632")
for follower in followers:
    print(bot.get_user_info(follower))
    following=bot.get_user_following("khwahish5632")
    for following in following:
        print(bot.get_user_info(Following))