from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def get_main_menu_kb(user_id, admin_id):
    kb = ReplyKeyboardBuilder()
    kb.button(text="📚 Математика")
    kb.button(text="👤 Мой профиль")
    if user_id == admin_id:
        kb.button(text="⚙️ Админка")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

# algebra
def get_math_topic_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🧮 Алгебра", callback_data="math_al")
    kb.button(text="📐 Геометрия", callback_data="math_geo")
    kb.button(text="🎲 Вер. и стат.", callback_data="math_ver")
    kb.adjust(1)
    return kb.as_markup()

def get_al_topic_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="📦 ФСУ", callback_data="al_fsy")
    kb.button(text="⚡️ Степени", callback_data="al_step")
    kb.button(text="⚖️ Уравнения", callback_data="al_yrov")
    kb.button(text="⬅️ Назад", callback_data="math")
    kb.adjust(1)
    return kb.as_markup()

# geometry

def get_geo_topic_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="🔺 Треугольники", callback_data="math_tri")
    kb.button(text="🔳 Площадь", callback_data="math_area")
    kb.button(text="⬅️ Назад", callback_data="back_to_subjects")
    kb.adjust(1)
    return kb.as_markup()

def get_geo_topic2_kb():
    kb = InlineKeyboardBuilder()
    kb.button(text="📐 Прям. △", callback_data="geo_tri2")
    kb.button(text="🔺 Равнобренный △", callback_data="geo_tri3")
    kb.button(text="🔺 Равносторонний △", callback_data="geo_tri4")
    kb.button(text="🌀 Общие свойства", callback_data="geo_sv")
    kb.button(text="⬅️ Назад", callback_data="math_geo")
    kb.adjust(1)
    return kb.as_markup()