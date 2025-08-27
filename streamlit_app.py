import streamlit as st
import time

target = "Streamlit makes apps easy!"

# 初期化
if "correct_input" not in st.session_state:
    st.session_state.correct_input = ""
if "start_time" not in st.session_state:
    st.session_state.start_time = None

st.title("Typing Training")
st.write(f"お題: **{target}**")

# 入力
user_input = st.text_input("入力してください:", st.session_state.correct_input)

# タイマー開始
if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# 判定
if target.startswith(user_input):
    # 正しい部分を更新
    st.session_state.correct_input = user_input
else:
    # 間違った場合 → 強制的に正しい部分まで戻す
    st.session_state.correct_input = st.session_state.correct_input

# 正誤表示
colored_text = ""
for i, c in enumerate(target):
    if i < len(st.session_state.correct_input):
        colored_text += f"<span style='color:green'>{c}</span>"
    else:
        colored_text += f"<span style='color:gray'>{c}</span>"
st.markdown(colored_text, unsafe_allow_html=True)

# クリア判定
if st.session_state.correct_input == target:
    elapsed = time.time() - st.session_state.start_time
    st.success(f"✅ 正解！ 経過時間: {elapsed:.2f} 秒")
