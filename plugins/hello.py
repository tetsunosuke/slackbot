from slackbot.bot import respond_to

@respond_to('(.*)\+\+')
def reply_id(message, arg):
    message.reply(arg)
