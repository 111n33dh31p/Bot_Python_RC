from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton


# --- Main Menu ---
btnOther = KeyboardButton('Другое')
btnOrder = KeyboardButton('Сделать заказ')
btnCont = KeyboardButton('Связь с нами')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnOrder, btnOther, btnCont)

# --- Other Menu (Другое) ---
btnInfo = KeyboardButton('Информация')
btnWhy = KeyboardButton('Почему именно мы')
btnBackToMain1 = KeyboardButton('Вернуться в Глав. Меню')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnWhy, btnBackToMain1)

# --- Order Menu (Сделать заказ) ---
btnFirst = KeyboardButton('Первое блюдо')
btnSecond = KeyboardButton('Второе блюдо')
btnDrinks = KeyboardButton('Напитки')
btnBackToMain2 = KeyboardButton('Назад')
orderMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFirst, btnSecond, btnDrinks, btnBackToMain2)

# --- Another Menu (Связь с нами) ---
btnBackToMain3 = KeyboardButton('Вернуться в главное меню!')
anotherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnBackToMain3)

# --- First Menu (Первое блюдо) ---
btnSoup1 = KeyboardButton('Удон 🍜')
btnSoup2 = KeyboardButton('Том Ям 🍝')
btnSoup3 = KeyboardButton('Гороховый 🍲')
btnBackToMain4 = KeyboardButton('Назад...')
FirstMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSoup1, btnSoup2, btnSoup3, btnBackToMain4)

# --- Second Menu (Второе блюдо) ---
btnFood1 = KeyboardButton('Рис 🍚')
btnFood2 = KeyboardButton('Суши 🍱')
btnFood3 = KeyboardButton('Котлеты 🧆')
btnBackToMain5 = KeyboardButton('Назад...')
SecondMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFood1, btnFood2, btnFood3, btnBackToMain5)

# --- Drinks Menu (Напитки) ---
btnDrink1 = KeyboardButton('Кофе ☕️')
btnDrink2 = KeyboardButton('Чай 🍵')
btnDrink3 = KeyboardButton('Сок 🧃')
btnBackToMain6 = KeyboardButton('Назад...')
DrinksMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnDrink1, btnDrink2, btnDrink3, btnBackToMain6)

# --- Pay Menu ---
btnCard = KeyboardButton('По карте')
btnCash = KeyboardButton('За наличку')
btnBackToMain7 = KeyboardButton('Назад...')
PayMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnCard, btnCash, btnBackToMain7)