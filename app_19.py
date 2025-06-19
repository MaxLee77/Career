import streamlit as st
from datetime import date

st.set_page_config(page_title="Поиск грузов", layout="centered")
st.title("🚛 Поиск грузов")
st.markdown("Найдите подходящие грузы или разместите свой грузовик.")

# --- Главное меню ---
menu = st.sidebar.radio("Выберите действие", ["🔍 Найти груз", "📦 Разместить грузовик"])

if menu == "📦 Разместить грузовик":
    st.header("📦 Разместить грузовик")
    with st.form("post_truck_form"):
        phone = st.text_input("Номер телефона", value="+998 ", placeholder="+998 90 123 45 67")
        truck_type = st.selectbox("Тип грузовика", [
    "Камаз",
    "ЗИЛ",
    "Man",
    "Кран",
    "Бортовой грузовик",
    "Автобетоносмеситель",
    "Погрузчик",
    "Холодильник-грузовик",
    "Экскаватор погрузчик",
    "Экскаватор",
    "Самосвал",
    "Автокран",
    "Howo (стандартные)",
    "Howo 60т",
    "Бульдозеры",
    "Мусоровозы",
    "Цементовоз от 12 до 40 куб",
    "Бетононасос (кобра)",
    "Бортовой",
    "Тентованный",
    "ГАЗель",
    "SHACMAN",
    "Шаланда",
    "SUZU"
])
        # Added two number inputs for capacity (tons and m³)
        col1, col2 = st.columns(2)
        with col1:
            load_capacity_tons = st.number_input("Максимальная грузоподъемность (тонны)", min_value=0, max_value=60, value=0, step=1, help="Укажите в тоннах (если применимо)")
        with col2:
            load_capacity_m3 = st.number_input("Максимальная грузоподъемность (м³)", min_value=0, max_value=100, value=0, step=1, help="Укажите в кубических метрах (если применимо)")
        uzbekistan_regions = [
            "Andijon viloyati",
            "Buxoro viloyati",
            "Farg'ona viloyati",
            "Jizzax viloyati",
            "Namangan viloyati",
            "Navoiy viloyati",
            "Qashqadaryo viloyati",
            "Samarqand viloyati",
            "Sirdaryo viloyati",
            "Surxondaryo viloyati",
            "Toshkent viloyati",
            "Xorazm viloyati",
            "Qoraqalpog'iston Respublikasi",
            "Toshkent shahri"
        ]
        locations = st.multiselect("Базовое местоположение (город или регион)", uzbekistan_regions, placeholder="Выберите один или несколько регионов")
        submit_post = st.form_submit_button("✅ Разместить")

    if submit_post:
        full_phone = phone if phone.strip() != "+998" else "+998 (не указан)"
        # Build capacity string based on user input
        capacity_str = []
        if load_capacity_tons > 0:
            capacity_str.append(f"{load_capacity_tons} тонн")
        if load_capacity_m3 > 0:
            capacity_str.append(f"{load_capacity_m3} м³")
        capacity_display = ", ".join(capacity_str) if capacity_str else "не указана"
        st.success(f"✅ Грузовик размещен: {truck_type} ({capacity_display}) доступен в {', '.join(locations) or 'не указан регион'}. Контакт: {full_phone}")

elif menu == "🔍 Найти груз":
    st.header("🔍 Найти грузы")
    with st.form("find_load_form"):
        truck_type = st.selectbox("Тип вашего грузовика", [
    "Камаз",
    "ЗИЛ",
    "Man",
    "Кран",
    "Бортовой грузовик",
    "Автобетоносмеситель",
    "Погрузчик",
    "Холодильник-грузовик",
    "Экскаватор погрузчик",
    "Экскаватор",
    "Самосвал",
    "Автокран",
    "Howo (стандартные)",
    "Howo 60т",
    "Бульдозеры",
    "Мусоровозы",
    "Цементовоз от 12 до 40 куб",
    "Бетононасос (кобра)",
    "Бортовой",
    "Тентованный",
    "ГАЗель",
    "SHACMAN",
    "Шаланда",
    "SUZU"
])
        load_type = st.selectbox("Ищу груз", ["Шагал", "Песок", "Цемент", "Строительные материалы", "Другое"])
        uzbekistan_regions = [
            "Andijon viloyati",
            "Buxoro viloyati",
            "Farg'ona viloyati",
            "Jizzax viloyati",
            "Namangan viloyati",
            "Navoiy viloyati",
            "Qashqadaryo viloyati",
            "Samarqand viloyati",
            "Sirdaryo viloyati",
            "Surxondaryo viloyati",
            "Toshkent viloyati",
            "Xorazm viloyati",
            "Qoraqalpog'iston Respublikasi",
            "Toshkent shahri"
        ]
        regions = st.multiselect("Регионы для работы", uzbekistan_regions, placeholder="Выберите один или несколько регионов")
        search = st.form_submit_button("🔎 Поиск")

    if search:
        st.success("🎯 Пример результата:")
        st.markdown(f"**🪨 Груз:** {load_type} 15 тонн\n\n**📍 Откуда:** Бекабад → {', '.join(regions) or 'Ташкент'}\n\n**📞 Контакт:** +998 90 123 45 67")