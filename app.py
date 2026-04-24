import streamlit as st
import time

# --- ページ設定と可愛いCSS ---
st.set_page_config(page_title="勉強キラリ✨", page_icon="🧸")

st.markdown("""
    <style>
    /* 全体の背景とフォント */
    .stApp {
        background-color: #FFF9E3;
    }
    h1 {
        color: #FF85A2;
        font-family: 'Hiragino Maru Gothic Pro', sans-serif;
        text-align: center;
    }
    /* ボタンを丸っこく、キラキラに */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #FFB7B2, #FF85A2);
        color: white;
        height: 70px;
        width: 100%;
        border-radius: 30px;
        border: none;
        font-size: 20px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(255, 133, 162, 0.3);
    }
    /* 入力欄を可愛く */
    .stTextInput input {
        border-radius: 20px;
        border: 2px solid #FFB7B2;
    }
    /* 成功メッセージ */
    .stSuccess {
        background-color: #FFD1DC;
        color: #D81B60;
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- コンテンツ ---
st.title("✨ 勉強キラリ ✨")
st.write("📖 **CPA講義を1分だけ見る魔法のボタン**")

# キャラクター代わりの絵文字
st.markdown("<div style='text-align: center; font-size: 50px;'>🧸 🐈</div>", unsafe_allow_html=True)

# URL入力
lecture_url = st.text_input("講義のURLを教えてね", placeholder="ここにペースト...")

if lecture_url:
    if st.button("✨ 1分だけ全集中する ✨"):
        # 講義へのリンク
        st.markdown(f'''
            <div style="text-align:center; margin-bottom:20px;">
                <a href="{lecture_url}" target="_blank" style="text-decoration:none;">
                    <button style="background-color: #85D8FF; color: white; border: none; padding: 15px 30px; border-radius: 50px; font-weight: bold; cursor: pointer;">
                        ここをタップして講義を開く 🎥
                    </button>
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
            
        # 完了！
        st.balloons()
        st.success("🌸 お疲れ様！1分頑張ったあなたは最高にキラキラしてるよ！ 🌸")
        
        st.markdown("---")
        st.subheader("🎧 脳を溶かす ご褒美ASMR 🍓")
        # お気に入りのASMR動画（わらび餅やキャンディ系）
        st.video("https://www.youtube.com/watch?v=kYI9Q2U107k") 
        
        st.write("今日はここまでにしてもいいし、もうちょっと頑張ってみてもいいよ。")

else:
    st.info("まずはURLを貼ってみてね。無理しなくて大丈夫だよ。")
