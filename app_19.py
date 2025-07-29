import streamlit as st
from datetime import date, datetime
import pandas as pd
import csv
import os

# Function to save truck data to CSV
def save_truck_to_csv(phone, truck_type, capacity_tons, capacity_m3, locations):
    """Save truck posting data to CSV file"""
    csv_file = "truck_posts.csv"
    
    # Prepare data for CSV
    submission_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    locations_str = ", ".join(locations) if locations else "не указан"
    
    # Check if file exists to determine if we need to write headers
    file_exists = os.path.exists(csv_file)
    
    # Write data to CSV
    with open(csv_file, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write headers if file doesn't exist
        if not file_exists:
            writer.writerow(['phone', 'truck_type', 'capacity_tons', 'capacity_m3', 'locations', 'submission_date'])
        
        # Write data row
        writer.writerow([phone, truck_type, capacity_tons, capacity_m3, locations_str, submission_date])

# Function to load and display existing truck posts
def load_truck_posts():
    """Load existing truck posts from CSV and return as DataFrame"""
    csv_file = "truck_posts.csv"
    if os.path.exists(csv_file):
        try:
            df = pd.read_csv(csv_file, encoding='utf-8')
            return df
        except Exception as e:
            st.error(f"Ошибка при загрузке данных: {e}")
            return pd.DataFrame()
    return pd.DataFrame()

st.set_page_config(page_title="Поиск грузов", layout="centered")
st.title("🚛 Поиск грузов")
st.markdown("Найдите подходящие грузы или разместите свой грузовик.")

# --- Главное меню ---
menu = st.sidebar.radio("Выберите действие", ["🔍 Найти груз", "📦 Разместить грузовик", "📋 Просмотр объявлений"])

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
        
        # Save data to CSV
        try:
            save_truck_to_csv(full_phone, truck_type, load_capacity_tons, load_capacity_m3, locations)
            
            # Build capacity string based on user input
            capacity_str = []
            if load_capacity_tons > 0:
                capacity_str.append(f"{load_capacity_tons} тонн")
            if load_capacity_m3 > 0:
                capacity_str.append(f"{load_capacity_m3} м³")
            capacity_display = ", ".join(capacity_str) if capacity_str else "не указана"
            
            st.success(f"✅ Грузовик размещен и сохранен: {truck_type} ({capacity_display}) доступен в {', '.join(locations) or 'не указан регион'}. Контакт: {full_phone}")
            st.info("💾 Данные сохранены в файл truck_posts.csv")
            
        except Exception as e:
            st.error(f"❌ Ошибка при сохранении данных: {e}")
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

elif menu == "📋 Просмотр объявлений":
    st.header("📋 Просмотр объявлений")
    
    # Load existing truck posts
    df = load_truck_posts()
    
    if not df.empty:
        st.subheader(f"📊 Всего объявлений: {len(df)}")
        
        # Display data in a nice table
        st.dataframe(
            df,
            column_config={
                "phone": "📞 Телефон",
                "truck_type": "🚛 Тип грузовика", 
                "capacity_tons": "⚖️ Грузоподъемность (т)",
                "capacity_m3": "📦 Грузоподъемность (м³)",
                "locations": "📍 Регионы",
                "submission_date": "📅 Дата размещения"
            },
            hide_index=True,
            use_container_width=True
        )
        
        # Download button for CSV
        csv_data = df.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label="📥 Скачать данные (CSV)",
            data=csv_data,
            file_name="truck_posts.csv",
            mime="text/csv"
        )
        
    else:
        st.info("📭 Пока нет размещенных объявлений. Будьте первым!")
