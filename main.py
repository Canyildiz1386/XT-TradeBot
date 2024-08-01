from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from pyxt.perp import Perp

API_KEY = '5c0b75fa-2d5b-4484-96ca-bd8e65882608'
SECRET_KEY = 'df762e0e5780e589766f2f224c8f38b09f4202d2'
XT_API = Perp(host="https://fapi.xt.com", access_key=API_KEY, secret_key=SECRET_KEY)

async def start(update: Update, context):
    keyboard = [[InlineKeyboardButton("ثبت سیگنال", callback_data='place_signal')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('سلام! 🤖\nبرای ثبت سیگنال معاملاتی، دکمه زیر را بزنید.', reply_markup=reply_markup)

async def button(update: Update, context):
    query = update.callback_query
    await query.answer()
    if query.data == 'place_signal':
        await query.edit_message_text(text="لطفاً سیگنال خود را به شکل زیر وارد کنید:\n\n"
                                           "نماد_نوع معامله\nجهت معامله (Short یا Long)\n"
                                           "قیمت\nاهرم\nمبلغ معامله به دلار\n"
                                           "حد ضرر\nحد سود\n#توضیحات")

async def handle_message(update: Update, context):
    text = update.message.text
    try:
        lines = text.split('\n')
        symbol_type = lines[0].split('BINANCE_')
        if len(symbol_type) < 2:
            raise ValueError("فرمت نماد نادرست است.")
        symbol = symbol_type[1].lower()
        direction, order_type = lines[1].split()
        price = float(lines[2].replace('$', ''))
        leverage = int(lines[3].replace('Lev ', ''))
        value = float(lines[4].replace('Value ', ''))
        sl = float(lines[5].replace('SL ', ''))
        tp = float(lines[6].replace('TP ', ''))

        order_type = 'LIMIT' if order_type.upper() == 'LIMIT' else 'MARKET'
        order_side = 'BUY' if direction.upper() == 'LONG' else 'SELL'
        position_side = 'LONG' if direction.upper() == 'LONG' else 'SHORT'

        amount = value / price

        res = XT_API.send_order(symbol=symbol, price=price, amount=amount, order_side=order_side, order_type=order_type, position_side=position_side)
        await update.message.reply_text(f"سفارش با پیام زیر ثبت شد:\n{res[1].get('error').get('code')}")
    except Exception as e:
        await update.message.reply_text(f"خطایی رخ داد:\n{e}")

if __name__ == '__main__':
    app = ApplicationBuilder().token("7362757567:AAEFn6ALXKnoO9p96qkgCpQsJY67VwHV4tw").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()
