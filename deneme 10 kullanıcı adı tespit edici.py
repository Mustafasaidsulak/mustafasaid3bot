import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
updater = Updater(token='5250013854:AAEcVXk_Z6WkcsftE2hiZA16R3nkN5QUxu0', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    numara = str(update.effective_user.id)
    update.message.reply_markdown_v2(
        fr'Merhaba {user.mention_markdown_v2()}\! okumanız gereken sayfaları özel olarak size iletebilmemiz için telegram kullanıcı numaranıza ihtiyacımız var\.',
    )
    update.message.reply_text(
        text = "Kullanıcı Numaranız: " + numara + ". Bunu Whatsapp ile bize iletebilir misiniz. Yapmanız gereken tek şey aşağıdaki butona basıp bağlantıya gitmek, sizi otomatik olarak mesaj yazılmış biçimde Whatsapp sohbetine yönlendirecek. Ardından bize mesajı göndermeniz yeterli. Şimdiden teşekkürler :)",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Whatsapp İle Gönder', url='https://api.whatsapp.com/send?phone=+905510577130&text=Kullanıcı Numaram '+ numara)],
        ])
    )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()