from aiogram import executor
from aiogram.types import CallbackQuery, Message
from config import dp
import datetime
from datetime import *
import requests
from reply import *
import logging
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def start(msg: Message):
    txt = f"<i><b>Assalomu alekum {msg.from_user.full_name}. Namoz vaqtlari botiga xush kelibsiz!\nПривет {msg.from_user.full_name}. Добро пожаловать в бот время молитвы</b></i>"
    await msg.answer(txt, parse_mode='html', reply_markup=intil)


@dp.callback_query_handler(text="uzb")
async def uzb(call: CallbackQuery):
    await call.message.answer("<b>O'zbek tili</b>", parse_mode='html', reply_markup=menukirishuz)
    await call.message.delete()
    await call.answer(cache_time=30)


@dp.message_handler(text="🌍 Hudud tanlash")
async def hudud_uz(msg: Message):
    await msg.answer("<b>Hududlar</b>", parse_mode='html', reply_markup=vaqtuz)


@dp.message_handler(text="⚙ Tilni o'zlashtirish🇺🇿🇷🇺")
async def til_uz(msg: Message):
    await msg.answer(f"<b>Tilni o'zlashtirish</b>", parse_mode='html', reply_markup=intil)


@dp.message_handler(text="📥Menyuga qaytish")
async def menyuga_qaytish(msg: Message):
    await msg.answer(f"<b>Menyuga qaytish</b>", parse_mode='html', reply_markup=menukirishuz)

@dp.message_handler(text="☪ Namoz haqida hadislar")
async def namoz_haqida_hadislar(msg: Message):
    await msg.answer(namoztxt, parse_mode='html', reply_markup=menukirishuz)

#sirdaryo
@dp.message_handler(text="⏳Sirdaryo viloyati")
async def sirdaryo_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Sirdaryo Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=sirdaryo_bugun)

@dp.callback_query_handler(text="ertangi_sirdayo")
async def ertangi_sirdayo(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Sirdaryo Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=sirdaryo_erta)

#toshkent
@dp.message_handler(text="⏳Toshkent shahar")
async def toshkent_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Toshkent shahri</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=toshkent_bugun)

@dp.callback_query_handler(text="ertangi_toshkent")
async def ertangi_toshkent(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Toshkent shahri</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=toshkent_erta)

#andijon
@dp.message_handler(text="⏳Andijon viloyati")
async def andijon_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Andijon Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=andijon_bugun)

@dp.callback_query_handler(text="ertangi_andijon")
async def ertangi_andijon(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Andijon Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=andijon_erta)

#buxoro
@dp.message_handler(text="⏳Buxoro viloyati")
async def buxoro_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Buxoro Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=buxora_bugun)

@dp.callback_query_handler(text="ertangi_buxoro")
async def ertangi_buxoro(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Buxoro Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=buxora_erta)

#fargona
@dp.message_handler(text="⏳Farg'ona viloyati")
async def sirdaryo_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Farg'ona Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=fargona_bugun)

@dp.callback_query_handler(text="ertangi_fargona")
async def ertangi_fargona(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Farg'ona Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=fargona_erta)

#jizzax
@dp.message_handler(text="⏳Jizzax viloyati")
async def jizzax_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Jizzax Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=jizzax_bugun)

@dp.callback_query_handler(text="ertangi_jizzax")
async def ertangi_jizzax(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Jizzax Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=jizzax_erta)

#xorazm
@dp.message_handler(text="⏳Xorazm viloyati")
async def xorazm_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Xorazm Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=xorazm_bugun)

@dp.callback_query_handler(text="ertangi_xorazm")
async def ertangi_xorazm(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Xorazm Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=xorazm_erta)

#namangan
@dp.message_handler(text="⏳Namangan viloyati")
async def namangan_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Namangan Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=namangan_bugun)

@dp.callback_query_handler(text="ertangi_namangan")
async def ertangi_namangan(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Namangan Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=namangan_erta)

#navoiy
@dp.message_handler(text="⏳Navoiy viloyati")
async def navoiy_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Navoiy Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=navoiy_bugun)

@dp.callback_query_handler(text="ertangi_navoiy")
async def ertangi_navoiy(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Navoiy Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=navoiy_bugun)

#nukus
@dp.message_handler(text="⏳Qoraqalpog'iston Respublikasi")
async def nukus_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Nukus Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=qoraqalpoq_bugun)

@dp.callback_query_handler(text="ertangi_qoraqalpoq")
async def ertangi_nukus(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Nukus Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=qoraqalpoq_erta)

#samarqand
@dp.message_handler(text="⏳Samarqand viloyati")
async def samarqand_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Samarqand Viloyati</b> bugungi namoz vaqtlari bilan tanishing:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Bomdod           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Quyosh           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Peshin           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Asr              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Shom             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Xufton           {xufton}\n", parse_mode='html', reply_markup=samarqand_bugun)

@dp.callback_query_handler(text="ertangi_samarqand")
async def ertangi_samarqand(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Samarqand Viloyati</b> ertangi namoz vaqtlari bilan tanishing:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Albatta namoz mo'minlarga vaqtida farz qilindi \n(Niso surasi, 103 oyat)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Bomdod           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Quyosh           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Peshin           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Asr              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Shom             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Xufton           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=samarqand_bugun)

@dp.callback_query_handler(text_contains="orqaga")
async def orqagaa(call: CallbackQuery):
    await call.message.answer(f"<b>Hududlar</b>", parse_mode='html', reply_markup=vaqtuz)
#------------------------------------------------------------------------------------------------------------------------------------
"""Ruscha"""

@dp.callback_query_handler(text="rus")
async def rus(call: CallbackQuery):
    await call.message.answer(f"<b>Русский язык</b>", parse_mode='html', reply_markup=menukirishrus)

@dp.message_handler(text="🌍 Выбор региона")
async def hudud_rus(msg: Message):
    await msg.answer(f"<b>Выбор региона</b>", parse_mode='html', reply_markup=vaqtrus)

@dp.message_handler(text="⚙ Овладение языком🇺🇿🇷🇺")
async def tilni_ozgartrish_rus(msg: Message):
    await msg.answer(f"<b>Овладение языком</b>", parse_mode='html', reply_markup=intil)

@dp.message_handler(text="☪ Хадисы о молитве")
async def hadislar_rus(msg: Message):
    await msg.answer(namoztxtrus, parse_mode='html', reply_markup=menukirishrus)

@dp.message_handler(text="📥Вернуться в меню")
async def menyuga_qaytish_rus(msg: Message):
    await msg.answer(f"<b>Вернуться в меню</b>", parse_mode='html', reply_markup=menukirishrus)

#sirdaryo_rus
@dp.message_handler(text="⏳Сырдарьинская область")
async def sirdaryo_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Сырдарьинская область</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=sirdaryo_bugun_rus)

@dp.callback_query_handler(text="ertangi_sirdayo_rus")
async def ertangi_sirdayo(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Сырдарьинская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=sirdaryo_erta_rus)

#toshkent
@dp.message_handler(text="⏳город Ташкент")
async def toshkent_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>город Ташкент</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=toshkent_bugun_rus)

@dp.callback_query_handler(text="ertangi_toshkent_rus")
async def ertangi_toshkent(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/toshkent").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>город Ташкент</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=toshkent_erta_rus)

#andijon
@dp.message_handler(text="⏳Андижанская область")
async def andijon_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Андижанская область</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=andijon_bugun)

@dp.callback_query_handler(text="ertangi_andijon_rus")
async def ertangi_andijon(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/andijon").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Андижанская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=andijon_erta_rus)

#buxoro
@dp.message_handler(text="⏳Бухарская область")
async def buxoro_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Buxoro Viloyati</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=buxora_bugun_rus)

@dp.callback_query_handler(text="ertangi_buxoro_rus")
async def ertangi_buxoro(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/buxoro").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Бухарская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=buxora_erta_rus)

#fargona
@dp.message_handler(text="⏳Ферганская область")
async def sirdaryo_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/farg'ona").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Ферганская область</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=fargona_bugun_rus)

@dp.callback_query_handler(text="ertangi_fargona_rus")
async def ertangi_fargona(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Ферганская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя\n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=fargona_erta_rus)

#jizzax
@dp.message_handler(text="⏳Джизакская область")
async def jizzax_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Джизакская область</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=jizzax_bugun_rus)

@dp.callback_query_handler(text="ertangi_jizzax_rus")
async def ertangi_jizzax(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/jizax").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Джизакская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=jizzax_erta_rus)

#xorazm
@dp.message_handler(text="⏳Хорезмская область")
async def xorazm_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Xorazm Viloyati</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=xorazm_bugun_rus)

@dp.callback_query_handler(text="ertangi_xorazm_rus")
async def ertangi_xorazm(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Хорезмская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=xorazm_erta_rus)

#namangan
@dp.message_handler(text="⏳Наманганская область")
async def namangan_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Наманганская область</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя\n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=namangan_bugun_rus)

@dp.callback_query_handler(text="ertangi_namangan_rus")
async def ertangi_namangan(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/namangan").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Наманганская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя\n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=namangan_erta_rus)

#navoiy
@dp.message_handler(text="⏳Навоийская область")
async def navoiy_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Навоийская область</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=navoiy_bugun_rus)

@dp.callback_query_handler(text="ertangi_navoiy_rus")
async def ertangi_navoiy(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/navoiy").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Навоийская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=navoiy_bugun_rus)

#nukus
@dp.message_handler(text="⏳Республика Каракалпакстан")
async def nukus_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Республика Каракалпакстан</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                        f"Конечно, молитва обязательна для верующих вовремя\n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=qoraqalpoq_bugun_rus)

@dp.callback_query_handler(text="ertangi_qoraqalpoq_rus")
async def ertangi_nukus(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/nukus").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Республика Каракалпакстан</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b> \n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=qoraqalpoq_erta_rus)

#samarqand
@dp.message_handler(text="⏳Самаркандская область")
async def samarqand_bugunn(msg: Message):
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['today']["Fajr"]
    quyosh_ch = data['today']["Sunrise"]
    peshin = data['today']["Dhuhr"]
    asr = data['today']["Asr"]
    shom = data['today']["Maghrib"]
    xufton = data['today']["Isha'a"]
    await msg.answer(f"<i><b>Самаркандская область</b> узнать время сегодняшней молитвы:{today}\n\n"
                        f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                        f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                        f"-------------------------------------\n"
                        f"⏳Утро           {bomdod}\n"
                        f"-------------------------------------\n"
                        f"⏱Солнце           {quyosh_ch}\n"
                        f"-------------------------------------\n"
                        f"⏳Полдень           {peshin}\n"
                        f"-------------------------------------\n"
                        f"⏳Аср              {asr}\n"
                        f"-------------------------------------\n"
                        f"⏳Вечер             {shom}\n"
                        f"-------------------------------------\n"
                        f"⏳Ночь           {xufton}\n", parse_mode='html', reply_markup=samarqand_bugun_rus)

@dp.callback_query_handler(text="ertangi_samarqand_rus")
async def ertangi_samarqand(call: CallbackQuery):
    await call.answer(cache_time=30)
    today = datetime.today()
    data = requests.get(f"https://dailyprayer.abdulrcs.repl.co/api/samarqand").json()
    bomdod = data['tomorrow']["Fajr"]
    quyosh_ch = data['tomorrow']["Sunrise"]
    peshin = data['tomorrow']["Dhuhr"]
    asr = data['tomorrow']["Asr"]
    shom = data['tomorrow']["Maghrib"]
    xufton = data['tomorrow']["Isha'a"]
    await call.message.edit_text(f"<i><b>Самаркандская область</b> узнать о времени завтрашней молитвы:\n\n"
                                 f"<b>إنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا</b>\n\n"
                            f"Конечно, молитва обязательна для верующих вовремя \n(Сура Ан-Ниса, аят 103)</i>\n"
                            f"-------------------------------------\n"
                            f"⏳Утро           {bomdod}\n"
                            f"-------------------------------------\n"
                            f"⏱Солнце           {quyosh_ch}\n"
                            f"-------------------------------------\n"
                            f"⏳Полдень           {peshin}\n"
                            f"-------------------------------------\n"
                            f"⏳Аср              {asr}\n"
                            f"-------------------------------------\n"
                            f"⏳Вечер             {shom}\n"
                            f"-------------------------------------\n"
                            f"⏳Ночь           {xufton}\n", parse_mode='html')
    await call.message.edit_reply_markup(reply_markup=samarqand_bugun_rus)

@dp.callback_query_handler(text_contains="mmm")
async def orqagaa(call: CallbackQuery):
    await call.message.answer(f"<b>Области</b>", parse_mode='html', reply_markup=vaqtrus)



if __name__ == '__main__':
    executor.start_polling(dp)
