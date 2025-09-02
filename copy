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

# 入力欄（常に正しい部分だけを表示）
user_input = st.text_input("入力してください:", value=st.session_state.correct_input)

# タイマー開始
if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# 判定（必ず1文字ずつチェック）
if len(user_input) > len(st.session_state.correct_input):
    # 入力された最新の文字
    next_char = user_input[-1]
    next_index = len(st.session_state.correct_input)

    # 正しい文字なら進む
    if next_char == target[next_index]:
        st.session_state.correct_input += next_char
        st.experimental_rerun()
    else:
        # 誤入力は無効化 → 強制的に戻す
        st.warning("❌ 間違いです！")
        st.experimental_rerun()

# 正誤表示（色付け）
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
