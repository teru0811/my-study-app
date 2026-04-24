import streamlit as st
import time
import random

# --- ページ設定 ---
st.set_page_config(page_title="勉強キラリ✨", page_icon="🍓")

# デザイン
st.markdown("""
    <style>
    .stApp { background-color: #FFF9F9; }
    .stamp-card {
        background: white; padding: 20px; border-radius: 25px;
        border: 3px solid #FFB6C1; text-align: center; margin-bottom: 20px;
    }
    .stamp-grid { font-size: 35px; letter-spacing: 10px; line-height: 2; }
    .quote-text { color: #FF1493; font-size: 18px; font-weight: bold; }
    .stButton > button {
        background: linear-gradient(135deg, #FF69B4, #FFB6C1);
        color: white; height: 70px; width: 100%; border-radius: 35px;
        font-size: 20px; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- スタンプの記憶機能 ---
if 'stamps' not in st.session_state:
    st.session_state.stamps = 0

st.title("🍓 勉強キラリ 🍓")

# --- 合格スタンプ帳エリア ---
st.markdown('<div class="stamp-card">', unsafe_allow_html=True)
st.markdown('<p style="color:#FF69B4; font-weight:bold; margin-bottom:10px;">💮 合格スタンプ帳 💮</p>', unsafe_allow_html=True)

# スタンプを表示（10個で1行にする演出）
stamp_display = "🌸" * st.session_state.stamps
if st.session_state.stamps == 0:
    stamp_display = "（まだスタンプがないよ。1分頑張ろう！）"

st.markdown(f'<div class="stamp-grid">{stamp_display}</div>', unsafe_allow_html=True)
st.markdown(f'<p style="font-size:14px; color:#666; margin-top:10px;">現在の合計：{st.session_state.stamps} 個</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 応援メッセージ ---
quotes = ["1分やれば、スタンプ1個ゲット！🧸", "スタンプを貯めて合格を掴み取ろう！🌸"]
st.info(random.choice(quotes))

# 固定URL
FIXED_URL = "https://tlp.edulio.com/cpa/mypage/chapter/"
st.markdown(f'<div style="text-align:center;"><a href="{FIXED_URL}" target="_blank" style="color:#FF69B4; font-weight:bold; text-decoration:none;">🔗 講義ページを開く</a></div>', unsafe_allow_html=True)

# --- 実行ボタン ---
if st.button("⏱️ 1分着火 ＆ スタンプGET！"):
    placeholder = st.empty()
    bar = st.progress(0)
    
    for i in range(60):
        seconds_left = 60 - i
        placeholder.markdown(f"<p style='text-align:center; font-size:20px; color:#FF1493;'>あと {seconds_left} 秒でスタンプ！ 🔥</p>", unsafe_allow_html=True)
        bar.progress((i + 1) / 60)
        time.sleep(1)
        
    # 完走したらスタンプを増やす！
    st.session_state.stamps += 1
    st.balloons()
    st.success(f"🌸 1分完走！スタンプ {st.session_state.stamps} 個目ゲット！ 🌸")
    
    # おまけ：ときめきフォトも表示
    reward_images = [
        "https://images.unsplash.com/photo-1514517604298-cf80e0fb7f1e?q=80&w=600",
        "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?q=80&w=600",
        "https://images.unsplash.com/photo-1548546738-8509cb246ed3?q=80&w=600"
    ]
    st.image(random.choice(reward_images), use_container_width=True)
