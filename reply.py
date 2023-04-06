from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

intil = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 Uzbek tili", callback_data="uzb"),
            InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="rus")
        ]
    ]
)

menukirishuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌍 Hudud tanlash"),
            KeyboardButton(text="⚙ Tilni o'zlashtirish🇺🇿🇷🇺")

        ],
        [
            KeyboardButton(text="☪ Namoz haqida hadislar")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

vaqtuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳Sirdaryo viloyati"),
            KeyboardButton(text="⏳Toshkent shahar")
        ],
        [
            KeyboardButton(text="⏳Andijon viloyati"),
            KeyboardButton(text="⏳Buxoro viloyati")
        ],
        [
            KeyboardButton(text="⏳Farg'ona viloyati"),
            KeyboardButton(text="⏳Jizzax viloyati")
        ],
        [
            KeyboardButton(text="⏳Xorazm viloyati"),
            KeyboardButton(text="⏳Namangan viloyati")
        ],
        [
            KeyboardButton(text="⏳Navoiy viloyati"),
            KeyboardButton(text="⏳Samarqand viloyati")
        ],
        [
            KeyboardButton(text="⏳Qoraqalpog'iston Respublikasi")
        ],
        [
            KeyboardButton(text="📥Menyuga qaytish")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

sirdaryo_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_sirdayo")
        ]
    ]
)

sirdaryo_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)


toshkent_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_toshkent")
        ]
    ]
)

toshkent_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)


andijon_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_andijon")
        ]
    ]
)

andijon_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

buxora_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_buxora")
        ]
    ]
)

buxora_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

fargona_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_fargona")
        ]
    ]
)

fargona_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

jizzax_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_jizzax")
        ]
    ]
)

jizzax_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

xorazm_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_xorazm")
        ]
    ]
)

xorazm_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

namangan_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_namangan")
        ]
    ]
)

namangan_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

navoiy_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_navoiy")
        ]
    ]
)

navoiy_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

samarqand_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_samarqand")
        ]
    ]
)

samarqand_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)

qoraqalpoq_bugun = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga"),
            InlineKeyboardButton(text="Ertangi kun ➡", callback_data="ertangi_qoraqalpoq")
        ]
    ]
)

qoraqalpoq_erta = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Orqaga", callback_data="orqaga")
        ]
    ]
)
#----------------------------------------------------------------------------------------------------
"""Ruscha"""

menukirishrus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🌍 Выбор региона"),
            KeyboardButton(text="⚙ Овладение языком🇺🇿🇷🇺")

        ],
        [
            KeyboardButton(text="☪ Хадисы о молитве")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


vaqtrus = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⏳Сырдарьинская область"),
            KeyboardButton(text="⏳город Ташкент")
        ],
        [
            KeyboardButton(text="⏳Андижанская область"),
            KeyboardButton(text="⏳Бухарская область")
        ],
        [
            KeyboardButton(text="⏳Ферганская область"),
            KeyboardButton(text="⏳Джизакская область")
        ],
        [
            KeyboardButton(text="⏳Хорезмская область"),
            KeyboardButton(text="⏳Наманганская область")
        ],
        [
            KeyboardButton(text="⏳Навоийская область"),
            KeyboardButton(text="⏳Самаркандская область")
        ],
        [
            KeyboardButton(text="⏳Республика Каракалпакстан")
        ],
        [
            KeyboardButton(text="📥Вернуться в меню")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


sirdaryo_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_sirdayo_rus")
        ]
    ]
)

sirdaryo_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)


toshkent_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_toshkent_rus")
        ]
    ]
)

toshkent_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)


andijon_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_andijon_rus")
        ]
    ]
)

andijon_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

buxora_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_buxora_rus")
        ]
    ]
)

buxora_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

fargona_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_fargona_rus")
        ]
    ]
)

fargona_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

jizzax_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_jizzax_rus")
        ]
    ]
)

jizzax_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

xorazm_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_xorazm_rus")
        ]
    ]
)

xorazm_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

namangan_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_namangan_rus")
        ]
    ]
)

namangan_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

navoiy_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_navoiy_rus")
        ]
    ]
)

navoiy_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

samarqand_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_samarqand_rus")
        ]
    ]
)

samarqand_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)

qoraqalpoq_bugun_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm"),
            InlineKeyboardButton(text="Завтра день ➡", callback_data="ertangi_qoraqalpoq_rus")
        ]
    ]
)

qoraqalpoq_erta_rus = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅ Назад", callback_data="mmm")
        ]
    ]
)












#----------------------------------------------------------------------------------------------------
namoztxt = (f"HADISLARDAN NAMUNALAR \n"
f"* Payg‘ambarimiz (s.a.v.) ashoblaridan so‘radilar: «Birortangiz uyingizning oldidan oqib o‘tadigan daryoda (yoki soyda) har kuni besh mahal yuvinsangiz, badanimda kir qolibdi, deb aytasizmi?» Sahobalar: «Sira ham kir qolmaydi», deyishdi. Rasuli Akram: «Besh vaqt namoz ham shunga o‘xshash bo‘lib, Alloh taolo bu o‘qilgan namozlar tufayli gunohlarni kechiradi».\n"
f"* «Asr namozini qazo qilib qo‘ygan odam bola-chaqasiyu mol-dunyosidan ajragan kishi yanglig‘dir».\n"
f"* «Qorong‘u kechalarda masjidga borgan kishilarga, Qiyomat kuni bir nurga mazhar bo‘lishlari xushxabarini yetkazing».\n"
f"* «Sizlardan birlaringiz namoz o‘qigan joyda tahoratini buzmasdan o‘tirgan muddatgacha, farishtalar: «Iloho, bu kishining gunohlarini kechir va unga rahm ayla», deb duo etishadi»\n"
f"* «Allohga qasamki, shunday narsa xayolimdan o‘tyapti: o‘tin to‘plashni buyursam va o‘tinlar to‘plansa. Keyin namozga buyursam, namoz uchun azon aytilsa, keyin bir kishini mo‘minlarga imomlikka o‘tishni buyursam-da, namozga kelmaganlarning borib uylarini yoqsam...»\n"
f"* «Mo‘minlar xufton va bomdod namozlaridagi savobni bilganlarida edi, bu namozlarni jamoat bilan o‘qish uchun, emaklab bo‘lsa ham, masjidga kelishar edi».\n"
f"* «Namoz inson bilan shirk va kufr o‘rtasidagi bir pardadir. Namozni tark etish bu pardani ko‘tarish bo‘ladi».\n"
f"* «Ular (kofirlar) bilan bizning o‘rtamizni farqlaydigan alomat namozdir. Binobarin, namozni tark qilgan kimsa kofirlarga o‘xshabdi».\n"
f"* «Banda Qiyomat kunida eng avvalo namozdan hisob-kitob qilinadi. Agar namozi durust chiqsa, qutulibdi va yutibdi. Agar namozi durust chiqmasa, yutqazibdi. Farz namozlari kam chiqsa, Alloh azza va jalla: «Qarang-chi, qulimning nafl namozlari bormi?» deydi. Namozlarining kami nafl namozlar bilan to‘ldiriladi. Qolgan amallari ham shu tarzda hisob-kitob qilinadi».\n"
f"* «Bir kuni Payg‘ambar, alayhissalom, huzurlarida namoz o‘qimay tong otguncha uxlagan bir kishining nomi tilga olindi. Rasuli Akram: «Unday bo‘lsa, u odamning quloqlariga yo qulog‘iga shayton bavl etibdi», deya marhamat qildilar».\n"
f"* «Sizlardan birov uxlab qolsa, shayton uning orqa miyasiga uch tugun tugib qo‘yadi va har tugunga: «Hali tunlar uzun, (bemalol) uxla», deya afsun o‘qiydi. Agar u odam uy-g‘onib Allohni zikr etsa, tugunlardan bittasi, tahorat olganida yana biri, namoz o‘qiganida esa, qolgani ham yechiladi va qalbi quvonch va xushnudlikka to‘lib tong ottiradi. Aks holda, shayton tugib qo‘ygan tugunlarning ta’sirida dangasalik bilan tong otguncha uxlab qoladi».\n"
f"* Kechasi turib ibodat qilgan va xotinini uyg‘otgan, xotini turishni xohlamasa, yuziga suv sepgan odamga Alloh rahmatini yog‘dirsin. Kechasi turib namoz o‘qigan va erini uyg‘otgan, eri turishni xohlamasa, yuziga suv sepgan xotinga Alloh rahmatini yog‘dirsin».\n"
f"* «Namoz jannatning kalitidir».\n"
f"* «Namoz dinning ustunidir».\n"
f"* «Namoz mo‘minning me’rojidir».\n"
f"* «Ey Muhammad, bir kecha-kunduzda ummatlaringga besh vaqt namozni farz qildim. O‘zimcha ahd qildimki, kim shu besh vaqt namozni o‘z vaqtida ado etib yursa, u kishini jannatga kiritaman. Kim o‘z vaqtida ado etib yurmasa, u banda xususida ahdim yo‘qdir» (Hadisi qudsiy).")


namoztxtrus = (f"ПРИМЕРЫ ИЗ ХАДИСОВ\n"
f"* Пророк (мир ему и благословение) спросил своих сподвижников: «Кто-нибудь из вас сказал бы, что если бы я пять раз в день мылся в реке (или ручье), которая протекает перед моим домом, мое тело стало бы грязным?» Сподвижники сказали: «В Сире не осталось грязи». Пророк Акрам сказал: «Пять раз молитвы подобны этой, и Аллах прощает грехи из-за этих молитв».\n"
f"* «Человек, пропускающий молитву аср, — плохой человек, разлученный со своими детьми и богатством».\n"
f"* «Обрадуй тех, кто ходит в мечеть темными ночами, что они будут благословлены светом в День Воскресения». \n"
f"* «Когда один из вас заснет, сатана завяжет три узла на его позвоночнике и прочитает заклинание на каждый узел, говоря: «Ночи еще длинны, спи (легко)». Если тот человек поминает Аллаха дома, то один из узлов развяжется, когда он совершает омовение, другой и когда он молится, остальные развяжутся, и его сердце наполнится радостью и счастьем. В противном случае, под влиянием созданных сатаной узлов, он будет лениво спать до рассвета».\n"
f"* Да помилует Бог человека, который ночью молился и будил жену, а если она не хотела вставать, брызгал ей на лицо водой. Да помилует Бог жену, которая вставала ночью и молилась, и будила мужа, и окропляла водой его лицо, когда он не хотел вставать».\n"
f"* «Молитва — это ключ к небу».\n"
f"* «Молитва — столп религии».\n"
f"* «Молитва — это благословение верующего».\n"
f"* «О Мухаммад, я обязал твой народ молиться пять раз за одну ночь. Я дал себе обещание, что кто будет выполнять эти пять ежедневных молитв вовремя, того человека я войду в рай. У меня нет завета с тем, кто не совершает омовения вовремя» (хадис кудси).")