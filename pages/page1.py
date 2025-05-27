pip install streamlit
import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Pomodoro 타이머", layout="centered")

st.title("🍅 공부 타이머 (Pomodoro)")
st.write("25분 집중 + 5분 휴식 주기로 공부하세요!")

# 세션 상태 초기화
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "logs" not in st.session_state:
    st.session_state.logs = []

# 타이머 설정
work_duration = 25 * 60  # 25분
break_duration = 5 * 60  # 5분

def format_seconds(seconds):
    mins = seconds // 60
    secs = seconds % 60
    return f"{mins:02}:{secs:02}"

# 타이머 시작
if st.button("⏱️ 타이머 시작"):
    st.session_state.start_time = time.time()

# 타이머 실행 중
if st.session_state.start_time:
    elapsed = int(time.time() - st.session_state.start_time)
    if elapsed < work_duration:
        st.success("💪 공부 중!")
        remaining = work_duration - elapsed
    elif elapsed < work_duration + break_duration:
        st.warning("🧘‍♀️ 휴식 시간!")
        remaining = work_duration + break_duration - elapsed
    else:
        st.session_state.logs.append(datetime.now().strftime("%Y-%m-%d %H:%M"))
        st.session_state.start_time = None
        st.balloons()
        st.success("🎉 한 세트 완료! 타이머를 다시 시작해보세요.")
        remaining = 0

    if remaining > 0:
        st.metric(label="⏳ 남은 시간", value=format_seconds(remaining))
        time.sleep(1)
        st.experimental_rerun()

# 공부 기록
st.divider()
st.subheader("📊 공부한 세트 기록")
if st.session_state.logs:
    for i, log in enumerate(reversed(st.session_state.logs), 1):
        st.write(f"{i}회차 - {log}")
else:
    st.write("아직 기록이 없습니다.")
