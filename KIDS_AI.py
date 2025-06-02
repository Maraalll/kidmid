import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from PIL import Image
import os
import random
import time

st.set_page_config(page_title='KIDS.AI — Обучающая платформа', layout='wide')

# --- Инициализация состояний ---
if 'page' not in st.session_state: st.session_state.page = 'start'
if 'child_name' not in st.session_state: st.session_state.child_name = ''
if 'interests' not in st.session_state: st.session_state.interests = []
if 'report' not in st.session_state: st.session_state.report = ''
if 'chat_history' not in st.session_state: st.session_state.chat_history = []

# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()
# --- Верхняя навигация ---
def top_nav():
    st.markdown('''<div style="padding:10px;background-color:#e6f2ff;border-radius:10px;font-weight:bold;">
    🏠 Главная | 👤 Профиль | 🧠 Задания | 📊 Программа | 🤖 Чат-бот</div>''', unsafe_allow_html=True)

# --- Боковая панель ---
def sidebar():
    st.sidebar.title('Категории')
    st.sidebar.button('Логика')
    st.sidebar.button('Моторика')
    st.sidebar.button('Речь')
    st.sidebar.button('Эмоции')

# --- Экран приветствия ---
def start_screen():
    st.title('Привет! Добро пожаловать в KIDS.AI')
    name = st.text_input('Как зовут ребёнка?')
    if name: st.session_state.child_name = name; st.session_state.page = 'interests'; st.experimental_rerun()

# --- Экран интересов ---
def interests_screen():
    st.title(f'{st.session_state.child_name}, выбери интересы:')
    opts = st.multiselect('Интересы:', ['Логика','Моторика','Речь','Эмоции'])
    if st.button('Далее') and opts: st.session_state.interests = opts; st.session_state.page = 'home'; st.experimental_rerun()

# --- Главный экран ---
def home_screen():
    st.title(f'Добро пожаловать, {st.session_state.child_name}!')
    st.image('images/kids_ai_avatar.png', width=120)
    st.write('Выбери задание:')
    col1, col2 = st.columns(2)
    if col1.button('Переливание воды'): st.session_state.page = 'pouring'
    if col2.button('Сортировка предметов'): st.session_state.page = 'sorting'

# --- Задание 1 ---
def pouring_task():
    st.header('Задание: Переливание воды')
    st.image('images/2.png')
    st.audio('audio/tts1.mp3')
    st.markdown('1. Возьми кувшин 2. Перелей в другой 3. Промокни губкой')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Задание 2 ---
def sorting_task():
    st.header('Задание: Сортировка предметов')
    st.image('images/sort.png')
    st.markdown('Рассортируй по цветам или размерам.')
    if st.button('Назад'): st.session_state.page = 'home'

# --- Профиль ---
def profile_screen():
    st.title('Профиль ребёнка')
    st.write('Имя:', st.session_state.child_name)
    st.write('Интересы:', ', '.join(st.session_state.interests))
    st.text_area('Отчёт воспитателя', key='report')
    if st.button('Сохранить отчёт'): st.success('Отчёт сохранён!')

# --- Программа ---
def program_screen():
    st.title('Программа развития')
    st.markdown('''🔹 Понедельник: Моторика\n🔹 Вторник: Логика\n🔹 Среда: Речь\n🔹 Четверг: Эмоции\n🔹 Пятница: Повторение''')

# --- Чат-бот ---
def chatbot_screen():
    st.title('🤖 Чат-бот')
    prompt = st.text_input('Задай вопрос')
    if prompt:
        response = f'AI ответ: это хороший вопрос о "{prompt}"'
        st.session_state.chat_history.append((prompt, response))
    for p, r in st.session_state.chat_history[-5:]: st.markdown(f'**Вы:** {p}\n**KIDS.AI:** {r}')

# --- Роутинг ---
top_nav()
sidebar()
if st.session_state.page == 'start': start_screen()
elif st.session_state.page == 'interests': interests_screen()
elif st.session_state.page == 'home': home_screen()
elif st.session_state.page == 'pouring': pouring_task()
elif st.session_state.page == 'sorting': sorting_task()
elif st.session_state.page == 'profile': profile_screen()
elif st.session_state.page == 'program': program_screen()
elif st.session_state.page == 'chatbot': chatbot_screen()