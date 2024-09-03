import os
from datetime import datetime
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create an OpenAI client with your API key
openai_client = openai.Client(api_key=os.environ.get("OPENAI_API_KEY"))

# Retrieve the assistant you want to use (replace with your assistant ID)
assistant = openai_client.beta.assistants.retrieve(
    "asst_7a9qGRMYYdytRD7cfvPSpDtv"  # Replace with your own assistant ID
)

# Path to the file where conversations will be logged
log_file_path = "conversation_logs.txt"

# Session state to store the conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

def log_conversation(user_message, assistant_message):
    """Logs the conversation to a file."""
    with open(log_file_path, "a") as log_file:
        log_file.write(f"Timestamp: {datetime.now()}\n")
        log_file.write(f"User: {user_message}\n")
        log_file.write(f"Assistant: {assistant_message}\n")
        log_file.write("-" * 40 + "\n")

def add_to_conversation(user_message, assistant_message):
    """Add the conversation to the session state for display."""
    st.session_state.conversation.append({"role": "user", "content": user_message})
    st.session_state.conversation.append({"role": "assistant", "content": assistant_message})

def handle_input():
    """Handles the input from the user and generates a response from the assistant."""
    user_message = st.session_state.user_input

    with st.spinner("The assistant is thinking..."):
        messages = [{"role": "user", "content": user_message}]

        # Create a new thread with the user message
        thread = openai_client.beta.threads.create(messages=messages)

        # Create a run with the new thread
        run = openai_client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )

        # Check periodically whether the run is done
        while run.status != "completed":
            run = openai_client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id
            )

        # Once the run is complete, display the assistant's response
        messages = openai_client.beta.threads.messages.list(thread_id=thread.id)
        assistant_response = messages.data[0].content[0].text.value

        # Add to conversation history and log the conversation
        add_to_conversation(user_message, assistant_response)
        log_conversation(user_message, assistant_response)

    # Clear the input box
    st.session_state.user_input = ""

# Create the title for the Streamlit page
st.title("AI Tutor for Computer Networking")

# Split the page into two columns
col1, col2 = st.columns([2, 1])  # Adjusted to give more space to the PDF viewer

# Left column: Display the PDF from Google Drive using an iframe
with col1:
    st.header("Course Book")

    # Use the correct Google Drive preview link
    drive_preview_link = "https://drive.google.com/file/d/1SG6O-6BYzjg3XXQ4AFhdmR1iSkjW8uyv/preview"

    # Embed the PDF from Google Drive using an iframe
    pdf_display = f"""
    <iframe src="{drive_preview_link}" width="100%" height="800px" allow="autoplay"></iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

# Right column: Display the chatbot interface
with col2:
    st.header("Chat with the AI Tutor")

    # Display the conversation thread
    for message in st.session_state.conversation:
        if message["role"] == "user":
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**Assistant:** {message['content']}")

    # Add a horizontal line to separate the conversation from the input area
    st.markdown("---")

    # Create a text input for the user to type a message
    user_input = st.text_input("Type your message here...", key="user_input", on_change=handle_input, placeholder="Type your question here...")
