import streamlit as st
import time
import random

# --- ページ設定 ---
st.set_page_config(page_title="勉強キラリ✨", page_icon="🍓")

# デザイン（維持）
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    .quote-card {
        background: white; padding: 25px; border-radius: 30px;
        box-shadow: 0 10px 25px rgba(255,105,180,0.2);
        text-align: center; border: 2px solid #FFC0CB; margin-bottom: 20px;
    }
    .quote-text { color: #FF1493; font-size: 22px; font-weight: bold; line-height: 1.5; }
    .link-button {
        display: block; background-color: #FFB6C1; color: white !important;
        padding: 18px; border-radius: 40px; font-weight: bold;
        text-decoration: none; margin: 15px 0; border: 3px solid #FFF; text-align: center;
    }
    .stButton > button {
        background: linear-gradient(135deg, #FF69B4 0%, #FFB6C1 100%);
        color: white; height: 80px; width: 100%; border-radius: 40px;
        font-size: 22px; font-weight: bold; border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🍓 勉強キラリ 🍓")

# 名言（維持）
quotes = ["今日ここを開いたあなたは、すでに世界一努力してる。えらい！🧸", "君の努力を、私はちゃんと知ってるよ。🌸", "頑張りすぎないで。1分やったらご褒美だよ。🍯"]
st.markdown(f'<div class="quote-card"><p class="quote-text">{random.choice(quotes)}</p></div>', unsafe_allow_html=True)

# 固定URL
FIXED_URL = "https://tlp.edulio.com/cpa/mypage/chapter/"
st.markdown(f'<a href="{FIXED_URL}" target="_blank" class="link-button">🔗 講義ページを準備する</a>', unsafe_allow_html=True)

if st.button("🔥 1分だけ自分を褒めに行く"):
    placeholder = st.empty()
    bar = st.progress(0)
    for i in range(60):
        seconds_left = 60 - i
        placeholder.markdown(f"<p style='text-align:center; font-size:20px; color:#FF1493;'><b>あと少し！</b><br>残り {seconds_left} 秒</p>", unsafe_allow_html=True)
        bar.progress((i + 1) / 60)
        time.sleep(1)
        
    st.snow()
    st.success("🌸 1分完走！お疲れ様！ 🌸")

    # --- 動画再生の修正ポイント ---
    asmr_links = [
        "https://www.youtube.com/embed/kYI9Q2U107k",
        "https://www.youtube.com/embed/S0rK-zI4_28",
        "https://www.youtube.com/embed/2vS7DqZpW1A",
        "https://www.youtube.com/embed/6m-S2D6P2yM"
    ]
    target_video = random.choice(asmr_links)

    # 方法1: 標準のビデオプレイヤー（埋め込み用URLに変更）
    st.video(target_video)

    # 方法2: もし表示されない時のための直リンク
    st.markdown(f"""
        <div style="text-align:center; margin-top:10px;">
            <p style="font-size:14px; color:#666;">↑動画が表示されない場合は、下をタップしてね！</p>
            <a href="{target_video.replace('embed/', 'watch?v=')}" target="_blank" style="color:#FF69B4; font-weight:bold;">
                📺 YouTubeアプリで直接見る
            </a>
        </div>
    """, unsafe_allow_html=True)
