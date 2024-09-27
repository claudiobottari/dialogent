import streamlit as st
from src.utils.logger import logger

## TODO: multi users
class MessageHandler:
    def __init__(self):
        # Initialize the messages in session state if it's empty
        if len(self.get_messages()) == 0:
            self.load_system_prompt()

    def load_system_prompt(self):
        """Loads the system prompt from a file and adds it to the message queue."""
        try:
            file_path = './prompts/system.md'
            with open(file_path, 'r') as file:
                content = file.read().strip()  # Read and strip any extra whitespace
            self.enqueue_message("system", content)
        except FileNotFoundError:
            st.error(f"System prompt file not found at {file_path}. Please check the path.")
        except Exception as e:
            st.error(f"An error occurred while loading the system prompt: {e}")

    def enqueue_message(self, role, content, name=None):
        """Adds a message to the queue."""
        message = {
            "role": role,
            "name": name,
            "content": content
        }
        logger.warning("storing", message)
        self.get_user_config().append(message)

    def enqueue_message_user(self, content):
        self.enqueue_message("user", content)

    def enqueue_message_assistant(self, content):
        self.enqueue_message("assistant", content)

    # Future implementation for user configurations
    def get_user_config(self):
        # Placeholder for database retrieval logic
        if 'session_state' not in st.session_state:
            st.session_state['session_state'] = []
        return st.session_state['session_state']

    def get_messages(self):
        """Returns the list of messages."""
        return self.get_user_config()