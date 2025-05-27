import streamlit as st

st.title("클릭 게임!")

if "score" not in st.session_state:
    st.session_state.score = 0

if st.button("클릭!"):
    st.session_state.score += 1

st.write(f"점수: {st.session_state.score}")
