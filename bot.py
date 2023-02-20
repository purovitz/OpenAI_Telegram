import telebot
import openai


#BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_TOKEN="XXX"
bot = telebot.TeleBot(BOT_TOKEN)

openai.api_key = "XXX"

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, "Yoo")


@bot.message_handler(commands=['image'])
def send_image(message):
    message_txt = message.text
    response = openai.Image.create(
        prompt=message_txt,
        n=1,
        size="1024x1024",
    )

    image_url = response['data'][0]['url']

    bot.send_photo(message.chat.id, photo=image_url)

@bot.message_handler(func=lambda msg: True)
def respond(message):

    message_text = message.text


    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message_text,
    temperature=0.3,
    max_tokens=300,
    # n=1,
    # top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    stop=None,
)

    bot.send_message(message.chat.id, response.choices[0].text)

bot.infinity_polling()

