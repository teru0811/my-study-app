import streamlit as st
import time
import random

# --- ページ設定 ---
st.set_page_config(page_title="勉強キラリ✨", page_icon="🍓")

# デザイン調整
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1 { color: #FF1493; text-align: center; font-family: 'Hiragino Maru Gothic Pro', sans-serif; text-shadow: 2px 2px #FFB6C1; }
    .stButton > button {
        background: linear-gradient(135deg, #FF69B4, #FF1493);
        color: white;
        height: 100px;
        width: 100%;
        border-radius: 50px;
        font-size: 24px;
        font-weight: bold;
        border: 5px solid #FFFFFF;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .message-box {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        border: 2px dashed #FF69B4;
        text-align: center;
        margin-bottom: 20px;
        font-size: 18px;
        color: #FF1493;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 起動時の演出 ---
st.balloons() # 開いた瞬間に風船を飛ばす！
st.title("🍓 勉強キラリ 🍓")

# --- ランダムメッセージ ---
messages = [
    "今日ここを開いただけで、もう合格に一歩近づいたよ！🌸",
    "CPAの勉強は本当に尊い。自分を誇ってね。🧸",
    "疲れてるのにエラい！1分だけ、無心になろう。✨",
    "今の努力は、絶対に裏切らないよ。応援してる！🍰",
    "まずはボタンをポチッ。そこから世界が変わるよ。🔥"
]
st.markdown(f'<div class="message-box"><b>今日の一言：</b><br>{random.choice(messages)}</div>', unsafe_allow_html=True)

# 固定URL
FIXED_URL = "https://tlp.edulio.com/cpa/mypage/chapter/"

# 着火ボタン
if st.button("🚀 講義へGO！（1分着火）"):
    st.markdown(f'''
        <div style="text-align:center; margin-top:10px; margin-bottom:20px;">
            <a href="{FIXED_URL}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #00BFFF; color: white; padding: 20px; border-radius: 50px; font-weight: bold; font-size: 20px; border: 4px solid #FFFFFF;">
                    👇 ここをタップして講義を開く！
                </div>
            </a>
        </div>
    ''', unsafe_allow_html=True)
    
    # タイマー
    placeholder = st.empty()
    bar = st.progress(0)
    for i in range(60):
        seconds_left = 60 - i
        placeholder.markdown(f"<p style='text-align:center; font-size:24px; color:#FF1493;'>あと <b>{seconds_left}</b> 秒だけ耐えて！ ⌛</p>", unsafe_allow_html=True)
        bar.progress((i + 1) / 60)
        time.sleep(1)
        
    # 完了演出
    st.snow() # 雪を降らせる
    st.success("🌸 1分クリア！あなたは天才！ 🌸")
    
    st.markdown("---")
    st.subheader("🍓 今日のおすすめASMR 🎧")
    
    # ランダムASMR動画リスト
    asmr_list = [
        "https://www.youtube.com/watch?v=kYI9Q2U107k", # わらび餅
        "https://www.youtube.com/watch?v=S0rK-zI4_28", # 琥珀糖
        "https://www.youtube.com/watch?v=2vS7DqZpW1A", # フルーツキャンディ
        "https://www.youtube.com/watch?v=6m-S2D6P2yM"  # マカロン
    ]
    st.video(random.choice(asmr_list))
    st.write("脳を癒やして、リラックスしてね。")
