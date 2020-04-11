from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2

def welcome(update, context):
    try:
        firstName = update.message.from_user.first_name
        message = 'Olá, ' + firstName + '! \n' + 'digite /atendimento para ver as opções'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as e:
        print(str(e))

def Atendimento(update, context):
    message = '''Qual tema você deseja saber mais hoje?\n
        1- Resiliência \n
        2- Autoconhecimento'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def inputAtendimento(update, context):
    Atendimento= (update.message.text).lower()
    print(Atendimento)
    if (Atendimento == '1' or Atendimento == 'Resiliência' or Atendimento == 'resiliencia'):
        message = '''Segue abaixo o Video com mais informações: https://www.youtube.com/watch?v=9PWedS78wfc&t=3s \n
                    e qualquer duvida estamos a disposição!!'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2

    elif (Atendimento == '2' or Atendimento == 'Autoconhecimento'):
        message = '''Segue abaixo o Video com mais informações: https://www.youtube.com/watch?v=RZhXIpXlkKU \n
                    e qualquer duvida estamos a disposição!!'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    
def inputAssunto(update, context):
    message = "Muito obrigada pelo em breve novidades!!"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END   

def main():
    token = '1182820862:AAHGMGWZI6LJPloox6sFKpZmPpebRGdnwbQ'
    updater = Updater(token=token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('Atendimento', Atendimento)],
        states={
            STATE1: [MessageHandler(Filters.text, inputAtendimento)],
            STATE2: [MessageHandler(Filters.text, inputAssunto)]
        },

        fallbacks=[CommandHandler('cancel', cancel)])


    updater.dispatcher.add_handler(conversation_handler)
   
    print(str(updater))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()    
    
