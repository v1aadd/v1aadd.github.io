from aiogram.types import Message, ContentType
from aiogram.types import PreCheckoutQuery, LabeledPrice
from aiogram.dispatcher.filters import Command

from tele_bot import bot, dp
from config import PAYMENTS_TOKEN

from keyboards import keyboard

@dp.message_handler(Command('start'))
async def start(message: Message):
    await bot.send_message(message.chat.id,
                           'Перейдем к оплате',
                           reply_markup=keyboard)

PRICE = {
    '1': [LabeledPrice(label='Item1', amount=150)],
}

@dp.message_handler(content_types='web_app_data')
async def buy_process(web_app_message):
    await bot.send_invoice(web_app_message.chat.id,
                           title='Летуаль',
                           description='Title',
                           provider_token=PAYMENTS_TOKEN,
                           currency='rub',
                           need_email=True,
                           need_phone_number=True,
                           prices=PRICE[f'{web_app_message.web_app_data.data}'],
                           start_parameter='example',
                           payload='some_invoice')

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(message.chat.id,
                           'Платеж совершен успешно!')