from telebot import *
import requests

app_key = ('6407894610:AAHTe6oWh1tk1CssOUBv44cmkcK3C42AEeY')
app = telebot.TeleBot(app_key)
# -- Buttons -- #
create_host = types.InlineKeyboardButton(text='📡︙انشاء استضافه.',callback_data='c')
dev = types.InlineKeyboardButton(text='👨🏻‍💻︙المطور',url='t.me/C15CS')
#-------
@app.message_handler(commands=['start'])
def startCommand(message):
	first_nameUser = message.from_user.first_name
	btn = types.InlineKeyboardMarkup()
	btn.row_width = 1
	btn.add(create_host,dev)

	app.send_message(message.chat.id, text='~ Hi {} In Create Host Python Bot.\n ~ مرحبا {} في بوت انشاء استضافه بايثون.'.format(first_nameUser,first_nameUser),reply_markup=btn,reply_to_message_id=message.id)

@app.callback_query_handler(func=lambda call:True)
def btn(call):
	if call.data=='c':
		msgLoding = app.send_message(call.message.chat.id,text='**جاري الانشاء ... ⚡**',parse_mode='markdown')
		key = requests.get('http://x-api.tech/Create/Python/Hosting').json()
		keyUsername = key['username']
		keyPassword = key['password']
		keyEmail = key['email']
		keyLogin = key['login']
		btn_login = types.InlineKeyboardButton(text='✅︙تسجيل الدخول',url=keyLogin)
		b = types.InlineKeyboardMarkup()
		b.row_width = 1
		b.add(btn_login,dev)
		
		app.edit_message_text('- تم الانشاء',msgLoding.chat.id,msgLoding.message_id)
		
		app.send_message(call.message.chat.id, text='''
		⌯ تم انشاء استضافه بايثون ✅.
		---------------------
		~ <b>Username</b> : <code>{}</code>
		~ <b>Password</b> : <code>{}</code>
		~ <b>Email</b> : <code>{}</code>
		---------------------
		'''.format(
		keyUsername,
		keyPassword,
		keyEmail
		),parse_mode='html',reply_markup=b,reply_to_message_id=call.message.id)
		app.delete_message(msgLoding.chat.id,msgLoding.message_id)
	
app.infinity_polling()
	
