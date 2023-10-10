import streamlit as st
from datetime import datetime
import time
import random


def main():
    st.set_page_config("Wild AI gf ")

    def first_page(title):
        st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>',
                    unsafe_allow_html=True)

    # Sidebar Development

    with st.sidebar:
        st.subheader("You know I love you with all my heart ❤️")

        nav = st.radio("", ["Confirm You are an Adult", "Chat :rocket:"])
        st.write(" ")

    # Confirm You are an Adult

    if nav == "Confirm You are an Adult":
        st.markdown(
            f'<h1 style="text-align: centre; color: white; font-size:28px;"> Before using me confirm you are an adult 🎃</h1>',
            unsafe_allow_html=True)
        with st.form("Imp_form"):
            name = st.text_input("Enter your name: ")
            Dob = st.number_input("The year you born")
            Age = datetime.now().year - Dob
            st.form_submit_button('Submit')

            if Age < 18:
                raise ValueError("Comemon kid go to study ")

    if nav == "Chat :rocket:":
        st.header("Kaise ho tum? Chalo baat karo ab mujhse ❤️")

        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("What is up?"):
            # Display user message in chat message container
            with st.chat_message("user"):
                st.markdown(prompt)
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})

        # React to user input
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            assistant_response = random.choice(["Ab mein samne huu kuch bologe nahi? 🫡", "Areyy Padhai Likhai karo IAS-YS bano or desh ko sambhalo kya kar rahi ho ye sab, Papa se batau abhi?"])

            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response.split():
                full_response += chunk + " "
                time.sleep(0.09)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            # message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})






if __name__ == "__main__":
    main()
