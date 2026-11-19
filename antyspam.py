import telebot

lower_limit=2
upper_limit=10
score_limit=10

command={'spam':   'spam the user'}
spam_user=[]
users_message={}    #cid:[tim1,time2]
@bot.message_handler(func=lambda message:True)
def spam(message):
    cid=message.chat.id
    message_time=message.date
    users_message.setdefault(cid,[])
    users_message[cid].append(message_time)

@bot.message_handler(command='spam')
def dates(message,users_massage):
    cid=message.chat.id
    for i in users_message[cid]:
        
    counter=0
    if distance>lower_limit:
        counter-=1
    if distance>lower_limit:
        counter+=1
    if counter==score_limit:
        spam_user.append(cid)
        




