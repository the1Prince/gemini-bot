import json
import telegram
from telegram.ext import CommandHandler, MessageHandler, Application, ContextTypes, filters, CallbackQueryHandler, CallbackContext
from telegram import  Update, InlineKeyboardButton, InlineKeyboardMarkup
import os
from dotenv import load_dotenv


load_dotenv()

import requests
Token = os.getenv('TELEKEY')

application = Application.builder().token(Token).build()


async def start(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hi there, I'm Gemini... talk to me!")


async def help(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='''
    /start -> Welcome to GeminiGPT
    /help -> Ask me anything, I promise to answer
    /generate -> type a question
    /contact -> Contact the bot creator
    ''')


async def question(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ask a question")



async def contact(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='''
    email: princeodoi39@gmail.com
    linkedin: https://www.linkedin.com/in/prince-odoi/
    ''')


async def chat(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    question = update.message.text
    gemini_url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=' + os.getenv('GKEY')
    
    payload=json.dumps({"contents": [{
        "parts":[{
          "text": question}]}]
          })
    headers = {}
    response = requests.request("POST", gemini_url, headers=headers, data=payload)
    p=response.json()
    l=p['candidates'][0]['content']['parts'][0]['text']
    
    print(l)
    answer=l=p['candidates'][0]['content']['parts'][0]['text']
    print(answer)

    await context.bot.send_message(chat_id=update.effective_chat.id, text='Here are some suggestions:\n' + answer + '\n' 'Thank you!')


echo_handler = MessageHandler(filters.TEXT, chat)
application.add_handler(CommandHandler('contact', contact))
application.add_handler(CommandHandler('help', help))
application.add_handler(CommandHandler('shorten', question))
application.add_handler(CommandHandler('start',start))
application.add_handler(echo_handler)
application.run_polling()



    
