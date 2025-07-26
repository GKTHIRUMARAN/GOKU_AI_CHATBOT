import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="Goku AI", page_icon="🧠")
st.title("🧠 Goku AI Chatbot")

user_input = st.text_input("You:", "")

if user_input:
    with st.spinner("Goku is thinking..."):
        response = get_response(user_input)
        st.markdown(f"*Goku:* {response}")

        # 🔊 Auto-play Goku voice
        st.markdown(
            f"""
            <audio autoplay="true" style="display:none">
                <source src="goku_reply.mp3" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True
        )