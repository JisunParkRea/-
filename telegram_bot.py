import telegram

# bot 선언, token 넣기
bot = telegram.Bot(token = 'Here is token')

## bot에 대한 업데이트 내용 가져오기
#for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id = 'Here is your id', text = "테스트입니다.")
