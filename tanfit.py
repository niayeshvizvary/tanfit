#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import os
import time
import logging
from dml import insert_customer_data, insert_product_data, insert_sale_info, insert_sale_row_info
from dql import get_product_info, get_known_users, get_spam_users
from telebot.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton
from telebot.util import antiflood
#logging.basicConfig(filename='project.log',level=logging.info,format='%(asctime)s-%(levelname)s-%(message)s')

API_TOKEN = '9176359608:AAEby9LOkacpU9MECWdSOL4DRq7erfbMy1A'
channel_cid=''
bot = telebot.TeleBot(API_TOKEN)

commands={
    'start' :   'welcome to tanfit gym bot',
    'help'  :   'help menu',
    'keyboard' :   'show sample reply keyboeard',
    'get_info'      :   'get user information',
    'send_file'     :   'send programs file',
    'inline_keyboard'  : 'inline keyboeard',
    'support'   :   'admin account',
    'invite_link' : ''
    }

admin_command={'edit_class' : 'edit DB'

}

admin=[]
hideboard=ReplyKeyboardRemove()
message_ids = {
    'start'     :   2
}

keyword_button={
    '1.show_class':['body bulding',
           'yoga',
           'pilates',
           'crossfit'],
    '2.show_subs': ['buffet',
                 'tredmil',
                 'plan']
                 ,
    '3.trainers_list':['first',
    'second',
    'third',
    'forth'
    ]
}
user_steps={}
user_data={}
shopping_cart ={}

lower_limit = 2
upper_limit = 10
max_score = 5

spam_data = {} 
spam_users = [] 

def is_spam(cid):
    global known_users, spam_data, spam_users
    if cid not in known_users:
        user_info = bot.get_chat(cid)
        insert_customer_data(CID=cid, FIRST_NAME=user_info.first_name, LAST_NAME=user_info.last_name, USERNAME=user_info.username)
        known_users = get_known_users() 
        return False
    if cid in spam_users:
        return True
    spam_data.setdefault(cid, {'last_message': 0, 'score': 0})
    if time.time() - spam_data[cid]['last_message'] < lower_limit:
        spam_data[cid]['last_message'] = time.time()
        spam_data[cid]['score'] += 1
    elif time.time() - spam_data[cid]['last_message'] > upper_limit:
        spam_data[cid]['last_message'] = time.time()
        spam_data[cid]['score'] = max(0, spam_data[cid]['score']-1)    
    if spam_data[cid]['score'] > max_score:
        bot.send_message(cid, 'please dont send spam messages')
        spam_users.append(cid)
        return True   
    return False


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        print(m)
        if m.content_type == 'text':
            print(f'{m.chat.first_name} {m.chat.id}: {m.text}')
        elif m.content_type == 'document':
            print(f'{m.chat.first_name} [{m.chat.id}]:document recived')
        elif m.content_type == 'photo':
            print(f'{m.chat.first_name} [{m.chat.id}]:photo recived')
        elif m.content_type == 'contact':
            print(f'{m.chat.first_name} [{m.chat.id}]:contact recived')


bot.set_update_listener(listener)  # register listener

def send_message(*args,**kwargs):
    try:
        return antiflood(bot.send_message(*args,**kwargs))
    except Exception as e:
        print(e)

# Handle '/start' 
@bot.message_handler(commands=['start'])
def start_command(message):
    cid=message.chat.id
    if is_spam(cid): 
        return
    send_message(cid,'welcome to tanfit gym bot')


#handle  '/help'
@bot.message_handler(commands=['help'])
def help_command(message):
    cid=message.chat.id
    if is_spam(cid): 
        return
    text='here is help menu\n'
    text+='-----------------=\n'
    for command,desc in commands.items():
        text+=f'/{command}:{desc}\n'
    send_message(cid,text)  

@bot.message_handler(commands=['invite_link'])
def command_invite_link_handler(message):
    cid = message.chat.id
    if is_spam(cid): 
        return
    invite_link = f"https://t.me/tanfitgym_bot?start={cid}"
    send_message(cid, f'here is your invite link: \n{invite_link}')      

#@bot.message_handler(content_types=['photo']):
#def get_photo(message):
    #cid=message.chat.id
    #if is_spam(cid): 
        #return
    #file_id=message.photo[-1].file_id
    #file_info=bot.get_file(file_id)
    #file_path=file_info.path
    #file_name=str(time.time()).replace('.','')+'.'+file_path.split('.')[-1]



@bot.message_handler(commands=['send_file'])
def send_programs(message):
    cid=message.chat.id
    if is_spam(cid): 
        return
    pass
    #with open('path','rb') as f:
        #bot.send_document(cid,f) 


@bot.message_handler(content_types=['contact'])
def content_contact_handler(message):
    cid = message.chat.id
    if is_spam(cid): return
    contact = message.contact
    phone_number = contact.phone_number
    if cid == contact.user_id:
        send_message(cid, 'your number is correct')
    else:
        send_message(cid, 'share your own number')

@bot.message_handler(commands=['support'])
def command_support_handler(message):
    cid = message.chat.id
    if is_spam(cid): 
        return
    send_message(cid, 'please conatct [support](tg://user?id=8082244374)', parse_mode='MarkDownV2')


@bot.message_handler(commands=['keyboard'])
def keyboard_command(message):
    cid=message.chat.id
    if is_spam(cid): 
        return
    keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('1.show_class','2.show_subs','3.trainers_list')
    send_message(cid,'here is your keyboard:',reply_markup=keyboard)



@bot.message_handler(func=lambda message: message.text in keyword_button)
def button_handler(message):
    cid=message.chat.id
    if is_spam(cid): 
        return
    if message.text=='1.register':
        command_get_info()
    info=keyword_button[message.text]
    send_message(cid,f'button {message.text} pressed',reply_markup=hideboard)
    keyboard=ReplyKeyboardMarkup(resize_keyboard=True)
    for i in info:
        keyboard.add(i)
    send_message(cid,'choose one',reply_markup=keyboard)
    user_steps[cid]='H'


#def get_class_data(class_id):
    #class_data=dql.class_data(class_id)
    #return class_data



@bot.callback_query_handler(func=lambda call:True)
def callback_handler(call):
    call_id=call.id
    cid=call.message.chat.id
    mid=call.message.message_id
    data=call.data
    if is_spam(cid): 
        return
    print(f'call id:{call_id},cid:{cid},mid:{mid},data:{data}')
    if data.startswith('register'):
        bot.answer_callback_query(call_id,'button register pressed')
        bot.edit_message_reply_markup(cid,mid,reply_markup=None)
    if data.startswith('cancel'):
        bot.answer_callback_query(call_id,'button cancel pressed')
        bot.edit_message_reply_markup(cid,mid,reply_markup=None)


@bot.message_handler(func=lambda message:user_steps.get(message.chat.id)=='H')
def inline_keyboard_handler(message):
    cid=message.chat.id
    if is_spam(cid): 
        return
    #info=get_class_data(4)
    #send_message(cid,info)
    markup=InlineKeyboardMarkup
    markup.add(InlineKeyboardButton('register'))
    markup.add(InlineKeyboardButton('back to menu'))
    #bot.edit_message_text(get_info(),cid,int(send_messagemessage.message_id))
    
    



def get_info(message):
    cid = message.chat.id
    if is_spam(cid): 
        return
    send_message(cid, 'please enter your name:')
    user_steps[cid] = 'A'

@bot.message_handler(func=lambda message:user_steps.get(message.chat.id)=='A')
def command_get_name(message):
    cid = message.chat.id
    if is_spam(cid): 
        return
    first_name=message.text
    user_data.setdefault(cid,{'first_name':None,'last_name':None,'phone_number':None,'adress':None})
    user_data[cid]['first_name']=first_name
    send_message(cid, 'please enter your last name:')
    user_steps[cid] = 'B'

@bot.message_handler(func=lambda message:user_steps.get(message.chat.id)=='B')
def command_get_last_name(message):
    cid = message.chat.id
    if is_spam(cid): 
        return
    last_name=message.text
    send_message(cid, 'please enter your phone number:')
    user_data[cid]['last_name']=last_name
    user_steps[cid] = 'C'

@bot.message_handler(func=lambda message:user_steps.get(message.chat.id)=='C')
def command_get_phone_num(message):
    cid = message.chat.id
    if is_spam(cid): 
        return
    phone_number=message.text
    user_data[cid]['phone_number']=phone_number
    send_message(cid, 'please enter your adress:')
    user_steps[cid] = 'D'


@bot.message_handler(func=lambda message:user_steps.get(message.chat.id)=='D')
def command_get_phone_num(message):
    cid = message.chat.id
    if is_spam(cid): 
        return
    adress=message.text
    user_data[cid]['adress']=adress
    send_message(cid, 'thank you for register in our gym')
    user_steps.pop[cid]


@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    if is_spam(m.chat.id): 
        return
    send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help", reply_to_message_id=m.message_id)

def worker():
    while True:
        print('worker is active')
        time.sleep(2)


import threading
threading.Thread(target=worker).start()

bot.infinity_polling(skip_pending=True)