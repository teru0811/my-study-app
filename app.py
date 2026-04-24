import streamlit as st
import time
import random

# --- ページ設定 ---
st.set_page_config(page_title="勉強キラリ✨", page_icon="🍯")

# デザイン調整
st.markdown("""
    <style>
    .stApp { background-color: #FFF5F0; }
    .main-card {
        background: white; padding: 20px; border-radius: 25px;
        box-shadow: 0 10px 30px rgba(255,182,193,0.3);
        text-align: center; border: 2px solid #FFD1DC; margin-bottom: 15px;
    }
    .link-button {
        display: block; background-color: #85D8FF; color: white !important;
        padding: 15px; border-radius: 30px; font-weight: bold;
        text-decoration: none; margin: 10px 0; border: 3px solid #FFF;
    }
    .stButton > button {
        background: linear-gradient(135deg, #FF9A9E 0%, #FECFEF 100%);
        color: white; height: 80px; width: 100%; border-radius: 40px;
        font-size: 20px; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.balloons()
st.title("🍯 勉強キラリ 🍯")

# --- 占い ＆ ミッション ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
fortunes = ["大吉！", "中吉！", "小吉！", "ラッキー！"]
luck_subject = ["財務会計論", "管理会計論", "監査論", "企業法", "租税法"]
st.markdown(f'<p style="color:#FF69B4; font-size:20px; font-weight:bold;">🔮 運勢：{random.choice(fortunes)} (科目：{random.choice(luck_subject)})</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

missions = ["テキストを1ページめくる", "電卓を叩く", "ペンを持つ", "1分だけ座る"]
st.info(f"🎯 今日のミッション：{random.choice(missions)}")

# 固定URL
FIXED_URL = "https://tlp.edulio.com/cpa/mypage/chapter/"

# --- ここがポイント！ ---
st.markdown(f'<a href="{FIXED_URL}" target="_blank" class="link-button">🔗 先に講義ページを開く</a>', unsafe_allow_html=True)

if st.button("⏱️ タイマー開始（1分全集中）"):
    # タイマー中もリンクを表示し続ける
    link_placeholder = st.empty()
    link_placeholder.markdown(f'<a href="{FIXED_URL}" target="_blank" class="link-button">🔗 講義ページに戻る</a>', unsafe_allow_html=True)
    
    placeholder = st.empty()
    bar = st.progress(0)
    
    for i in range(60):
        seconds_left = 60 - i
        placeholder.markdown(f"<p style='text-align:center; font-size:22px; color:#FF69B4;'><b>あと {seconds_left} 秒でご褒美 🍓</b></p>", unsafe_allow_html=True)
        bar.progress((i + 1) / 60)
        time.sleep(1)
        
    st.snow()
    st.success("🌸 1分完走！おめでとう！ 🌸")
    
    asmr_list = ["https://www.youtube.com/watch?v=kYI9Q2U107k", "https://www.youtube.com/watch?v=S0rK-zI4_28", "https://www.youtube.com/watch?v=2vS7DqZpW1A"]
    st.video(random.choice(asmr_list))
