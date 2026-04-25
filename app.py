import streamlit as st
import time
import random
from datetime import date
from streamlit_javascript import st_javascript

# --- ページ設定 ---
st.set_page_config(page_title="守護クマ勉強会🧸", page_icon="🧸")

# デザイン（維持）
st.markdown("""
    <style>
    .stApp { background-color: #FFF9F2; }
    .status-card {
        background: white; padding: 20px; border-radius: 20px;
        border: 2px solid #FFE4B5; text-align: center; margin-bottom: 15px;
    }
    .goal-card {
        background: linear-gradient(135deg, #FF4B4B 0%, #FF8E8E 100%);
        color: white; padding: 20px; border-radius: 20px;
        text-align: center; margin-bottom: 15px;
    }
    .bear-bubble {
        background: #FFFFFF; padding: 15px; border-radius: 40px;
        border: 2px solid #FFDAB9; position: relative; margin-bottom: 20px;
        text-align: center; font-weight: bold; color: #8B4513;
    }
    .money-text { color: #D4AF37; font-size: 32px; font-weight: bold; margin: 0; }
    .stButton > button {
        background: linear-gradient(135deg, #FFDAB9, #FFB6C1);
        color: #8B4513; height: 80px; width: 100%;
        border-radius: 40px; font-size: 20px; font-weight: bold; border: 4px solid #FFF;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🧠 記憶の魔法（LocalStorage） ---
# ブラウザに保存されている貯金額を読み込む
stored_money = st_javascript("localStorage.getItem('my_study_money');")

# まだ保存されていない場合は0にする
if stored_money is None or stored_money == "null":
    if 'money' not in st.session_state:
        st.session_state.money = 0
else:
    st.session_state.money = int(stored_money)

st.title("🧸 勉強キラリ・不滅版 💰")

# --- 1. クマのメッセージ ---
bear_messages = [
    "ボク、君が頑張った分をずっと覚えておくことにしたよ！",
    "5/31まで、この貯金箱をパンパンにしようね🧸",
    "リセットされないから、安心して積み上げて大丈夫だよ！",
    "1分が一生の宝物になるよ。今日も始めよう！"
]
st.markdown('<div style="text-align: center; font-size: 60px;">🧸</div>', unsafe_allow_html=True)
st.markdown(f'<div class="bear-bubble">「{random.choice(bear_messages)}」</div>', unsafe_allow_html=True)

# --- 2. カウントダウン ＆ 貯金 ---
goal_date = date(2026, 5, 31)
days_left = (goal_date - date.today()).days

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'''<div class="goal-card"><p style="margin:0; font-size:12px; font-weight:bold;">🏁 5/31まで</p><p style="margin:0; font-size:28px; font-weight:bold;">{max(0, days_left)} 日</p></div>''', unsafe_allow_html=True)
with col2:
    st.markdown(f'''<div class="status-card"><p style="margin:0; font-size:12px; color:#999;">💰 ご褒美貯金</p><p class="money-text">¥{st.session_state.money:,}</p></div>''', unsafe_allow_html=True)

# 固定URL
FIXED_URL = "https://tlp.edulio.com/cpa/mypage/chapter/"
st.markdown(f'<div style="text-align:center; margin-bottom:15px;"><a href="{FIXED_URL}" target="_blank" style="color:#D2691E; font-weight:bold; text-decoration:none;">🔗 講義ページを開く 🔗</a></div>', unsafe_allow_html=True)

# --- 3. 実行ボタン ---
if st.button("🚀 1分着火 ＆ 記憶に刻む！"):
    placeholder = st.empty()
    bar = st.progress(0)
    for i in range(60):
        seconds_left = 60 - i
        placeholder.markdown(f"<p style='text-align:center; font-size:18px; color:#D2691E;'><b>集中タイム...</b><br>残り {seconds_left} 秒</p>", unsafe_allow_html=True)
        bar.progress((i + 1) / 60)
        time.sleep(1)
        
    # 貯金加算
    st.session_state.money += 500
    
    # 🧠 ここでブラウザに保存！
    st_javascript(f"localStorage.setItem('my_study_money', '{st.session_state.money}');")
    
    st.balloons()
    st.success(f"🌸 完走！500円貯まったよ！(合計: ¥{st.session_state.money:,}) 🌸")
    st.image("https://images.unsplash.com/photo-1520004434532-668416a08753?q=80&w=600", use_container_width=True)
