import streamlit as st
import time
import random
from datetime import date

# --- ページ設定 ---
st.set_page_config(page_title="守護クマ勉強会🧸", page_icon="🧸")

# デザイン（パステル調の癒やし × ゴージャスな貯金箱）
st.markdown("""
    <style>
    .stApp { background-color: #FFF9F2; }
    .status-card {
        background: white; padding: 20px; border-radius: 20px;
        border: 2px solid #FFE4B5; text-align: center; margin-bottom: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
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

# --- データの保持（貯金箱） ---
if 'money' not in st.session_state:
    st.session_state.money = 0

st.title("🧸 勉強キラリ・最終形態 💰")

# --- 1. 守護クマの励まし ---
bear_messages = [
    "5/31まで一緒に走り抜けよう！ボクがついてるよ！",
    "今の1分が、将来の君を助けるんだ。信じてるよ！",
    "貯金も増えてきたね！合格後のご褒美、何にする？",
    "君の努力は、世界で一番価値があるよ。🧸",
    "1分だけ、ボクと一緒に呼吸を合わせよう。"
]
st.markdown('<div style="text-align: center; font-size: 60px;">🧸</div>', unsafe_allow_html=True)
st.markdown(f'<div class="bear-bubble">「{random.choice(bear_messages)}」</div>', unsafe_allow_html=True)

# --- 2. カウントダウン ＆ 貯金カウンター（合体！） ---
goal_date = date(2026, 5, 31)
days_left = (goal_date - date.today()).days

col1, col2 = st.columns(2)
with col1:
    st.markdown(f'''
        <div class="goal-card">
            <p style="margin:0; font-size:12px; font-weight:bold;">🏁 5/31まで</p>
            <p style="margin:0; font-size:28px; font-weight:bold;">{max(0, days_left)} 日</p>
        </div>
    ''', unsafe_allow_html=True)
with col2:
    st.markdown(f'''
        <div class="status-card">
            <p style="margin:0; font-size:12px; color:#999;">💰 ご褒美貯金</p>
            <p class="money-text">¥{st.session_state.money:,}</p>
        </div>
    ''', unsafe_allow_html=True)

# 固定URL
FIXED_URL = "https://tlp.edulio.com/cpa/mypage/chapter/"
st.markdown(f'<div style="text-align:center; margin-bottom:15px;"><a href="{FIXED_URL}" target="_blank" style="color:#D2691E; font-weight:bold; text-decoration:none;">🔗 講義ページを開く 🔗</a></div>', unsafe_allow_html=True)

# --- 3. 実行ボタン ---
if st.button("🚀 1分着火 ＆ 貯金GET！"):
    placeholder = st.empty()
    bar = st.progress(0)
    
    # 5/31に向けた実況
    live_support = ["いい感じだよ！", "集中、集中...", "完走が見えてきた！", "未来の君が笑ってるよ！", "あと少し、頑張れ！"]
    
    for i in range(60):
        seconds_left = 60 - i
        if i % 12 == 0:
            msg = random.choice(live_support)
        placeholder.markdown(f"<p style='text-align:center; font-size:18px; color:#D2691E;'><b>{msg}</b><br>残り {seconds_left} 秒</p>", unsafe_allow_html=True)
        bar.progress((i + 1) / 60)
        time.sleep(1)
        
    # 完了処理
    st.session_state.money += 500
    st.balloons()
    st.success(f"🌸 1分完走！500円貯まったよ！(合計: ¥{st.session_state.money:,}) 🌸")
    
    # ご褒美：極上の癒やしフォト
    reward_images = [
        "https://images.unsplash.com/photo-1516733968668-dbdce39c46ef?q=80&w=600",
        "https://images.unsplash.com/photo-1512433012647-50a9c538531c?q=80&w=600",
        "https://images.unsplash.com/photo-1520004434532-668416a08753?q=80&w=600"
    ]
    st.image(random.choice(reward_images), caption="5月31日、笑って迎えようね。", use_container_width=True)
