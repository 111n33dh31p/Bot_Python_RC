import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

# --- Main Settings ---
token = '5575410799:AAHv0Xw_uBn8ZXCAPAznfVDdFNCn0aHfteU'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Здравствуйте {0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
#------------------ Main Menu Open
    if message.text == 'Сделать заказ':
        await bot.send_message(message.from_user.id, 'Что будем выбирать?', reply_markup=nav.orderMenu)
    if message.text == 'Другое':
        await bot.send_message(message.from_user.id, 'Вы можете почитать про нас или же вернуться обратно в меню', reply_markup=nav.otherMenu)
    if message.text == 'Связь с нами':
        await bot.send_message(message.from_user.id, '<b>Телефон:</b> 89204553550 \n<b>Почта:</b> nekrasov.d.a@outlook.com ', reply_markup=nav.anotherMenu, parse_mode=types.ParseMode.HTML)
    if message.text == 'Вернуться в главное меню!':
        await bot.send_message(message.from_user.id, 'Возвращаю вас в главное меню...', reply_markup=nav.mainMenu)
#------------------ Main Menu Close

#------------------ Other Menu Open
    if message.text == 'Информация':
        await bot.send_message(message.from_user.id, 'Мы - один из самых крупных ресторанов Воронежа!', reply_markup=nav.anotherMenu)
    if message.text == 'Почему именно вы':
        await bot.send_message(message.from_user.id, 'Да потому что! А кто ещё?', reply_markup=nav.anotherMenu)
    if message.text == 'Вернуться в Глав. Меню':
        await bot.send_message(message.from_user.id, 'Возвращаю вас в главное меню...', reply_markup=nav.mainMenu)
#------------------ Other Menu Close

#------------------ Order Menu Open
    if message.text == 'Первое блюдо':
        await bot.send_message(message.from_user.id, 'Что будем выбирать?', reply_markup=nav.FirstMenu)
    if message.text == 'Второе блюдо':
        await bot.send_message(message.from_user.id, 'Что будем выбирать?', reply_markup=nav.SecondMenu)
    if message.text == 'Напитки':
        await bot.send_message(message.from_user.id, 'Что будем выбирать?', reply_markup=nav.DrinksMenu)
    if message.text == 'Назад':
        await bot.send_message(message.from_user.id, 'Что будем выбирать?', reply_markup=nav.mainMenu)
#------------------ Order Menu Close

#------------------ First Menu Open
    if message.text == 'Удон 🍜':
        await bot.send_message(message.from_user.id, 'Удон - отличный выбор.', reply_markup=nav.PayMenu)
    if message.text == 'Том Ям 🍝':
        await bot.send_message(message.from_user.id, 'Том Ям - отличный выбор.', reply_markup=nav.PayMenu)
    if message.text == 'Гороховый 🍲':
        await bot.send_message(message.from_user.id, 'Гороховый - отличный выбор', reply_markup=nav.PayMenu)
    if message.text == 'Назад...':
        await bot.send_message(message.from_user.id, 'Что будем выбирать?', reply_markup=nav.orderMenu)
#------------------ First Menu Close

#------------------ Second Menu Open
    if message.text == 'Рис 🍚':
        await bot.send_message(message.from_user.id, 'Рис - отличный выбор!', reply_markup=nav.PayMenu)
    if message.text == 'Суши 🍱':
        await bot.send_message(message.from_user.id, 'Суши - отличный выбор!', reply_markup=nav.PayMenu)
    if message.text == 'Котлеты 🧆':
        await bot.send_message(message.from_user.id, 'Котлеты - отличный выбор!', reply_markup=nav.PayMenu)
#------------------ Second Menu Close

#------------------ Drinks Menu Open
    if message.text == 'Кофе ☕️':
        await bot.send_message(message.from_user.id, 'Кофе - отличный выбор!', reply_markup=nav.PayMenu)
    if message.text == 'Чай 🍵':
        await bot.send_message(message.from_user.id, 'Чай - отличный выбор!', reply_markup=nav.PayMenu)
    if message.text == 'Сок 🧃':
        await bot.send_message(message.from_user.id, 'Сок - отличный выбор!', reply_markup=nav.PayMenu)










if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)