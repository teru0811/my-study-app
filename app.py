import streamlit as st
import time

# --- ページ設定 ---
st.set_page_config(page_title="勉強キラリ✨", page_icon="🧸")

# デザイン調整
st.markdown("""
    <style>
    .stApp { background-color: #FFF9E3; }
    h1 { color: #FF85A2; text-align: center; font-family: 'Hiragino Maru Gothic Pro', sans-serif; }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #FFB7B2, #FF85A2);
        color: white;
        height: 80px;
        width: 100%;
        border-radius: 30px;
        border: none;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 133, 162, 0.3);
    }
    .main-text { font-size: 16px; color: #666; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- コンテンツ ---
st.title("✨ 勉強キラリ ✨")
st.markdown('<p class="main-text">URLは設定済みだよ！ボタンを押すだけ🧸</p>', unsafe_allow_html=True)

# 固定の講義ページURL
FIXED_URL = "https://tlp.edulio.com/cpa/mypage/chapter/"

# キャラクター
st.markdown("<div style='text-align: center; font-size: 60px; margin-bottom: 20px;'>🌸🧸🌸</div>", unsafe_allow_html=True)

# 着火ボタン
if st.button("🔥 1分だけ全集中する"):
    # 講義ページを開くリンク
    st.markdown(f'''
        <div style="text-align:center; margin-bottom:20px;">
            <a href="{FIXED_URL}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #85D8FF; color: white; padding: 20px; border-radius: 50px; font-weight: bold; font-size: 18px;">
                    👈 ここをタップして講義ページへ！
                </div>
            </a>
        </div>
    ''', unsafe_allow_html=True)
    
    # カウントダウン
    placeholder = st.empty()
    bar = st.progress(0)
    
    for i in range(60):
        seconds_left = 60 - i
        placeholder.markdown(f"<p style='text-align:center; font-size:24px; color:#FF85A2;'>解放まであと <b>{seconds_left}</b> 秒 ⏳</p>", unsafe_allow_html=True)
        bar.progress((i + 1) / 60)
        time.sleep(1)
        
    # 完了演出
    st.balloons()
    st.success("🌸 1分完走！お疲れ様！ 🌸")
    
    st.markdown("---")
    st.subheader("🎧 脳を溶かす ご褒美ASMR 🍓")
    # お気に入りのASMR（わらび餅/キャンディ系）
    st.video("https://www.youtube.com/watch?v=kYI9Q2U107k") 
    
    st.write("今のあなたなら、もう少し見れちゃうかも？無理はしないでね。")
