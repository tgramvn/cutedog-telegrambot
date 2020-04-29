from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram import Update
from quote import get_random_quote
import requests
import re

### replace TOKEN with token generated from BotFather
updater = Updater(TOKEN, use_context=True)

# get random dog image url
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

# to distinguish an image from video or GIF
def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


def start(update, context):
    s = """ 
    Welcome to Random Cute Dog! 
    \n /aww to get a cute image of a doggie to brighten up your day! \U0001f436 
    \n /woof to get a random quote \U0001f4ac
    \n /bye to say byebye \U0001f622
    """
    update.message.reply_text(s)


def aww(update, context):
    url = get_image_url()
    chat_id = update.message.chat_id  # get recipient's ID
    context.bot.send_photo(chat_id=chat_id, photo=url)  # send dog image


def woof(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,text=get_random_quote())


def bye(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Bye! See you again!")


# to run program
def main():
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('aww',aww))
    dispatcher.add_handler(CommandHandler('woof', woof))
    dispatcher.add_handler(CommandHandler('bye', bye))
    updater.start_polling()   # starts the bot
    updater.idle()  # block the script until the user sends a command to break
    
if __name__ == '__main__':
    main()



