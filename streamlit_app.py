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
user_input = st.text_input("入力してください:", value=st.session_state.correct_input)

# タイマー開始
if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# 一文字ずつ判定
if len(user_input) > len(st.session_state.correct_input):
    # 新しい文字が入力された場合
    next_index = len(st.session_state.correct_input)
    if target.startswith(user_input):
        # 正しい場合のみ更新
        st.session_state.correct_input = user_input
    else:
        # 間違った場合 → 入力を戻す
        st.warning("❌ 間違いです！")
        st.session_state.correct_input = st.session_state.correct_input
        # 再描画で強制的に戻す
        st.experimental_rerun()

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
