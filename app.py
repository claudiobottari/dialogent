import streamlit as st
import os
from src.agents.engine import get_response, solve
from src.agents.messages import MessageHandler
from src.utils.logger import logger


def main():
    st.image(os.path.join("assets", "logo.png"), width=200)

    st.title("Dialogent")
    st.subheader("Showcase Chat Application for Agentic behavior through function calling")

    chat_container = st.container()
    chat_container.chat_message("assistant").write("Hello! How can I assist you today?")

    message_handler = MessageHandler()

    # Display the chat history
    logger.info(message_handler.get_messages())
    for i, msg in enumerate(message_handler.get_messages()[1:]):
        chat_container.chat_message(msg["role"]).write(msg["content"])

    user_input = st.chat_input("Ask a question:") # , key='user_input'
    if user_input:
        chat_container.chat_message("user").write(user_input)
        message_handler.enqueue_message_user(user_input)

        with st.spinner("Processing your request..."):
            response = solve(message_handler)
            message_handler.enqueue_message_assistant(response)
            chat_container.chat_message("assistant").write(response)


if __name__ == "__main__":
    main()