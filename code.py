import streamlit as st #type:ignore

# Set the title of the Streamlit app
st.set_page_config(page_title="🤖Right-Guide", page_icon="🤖")

st.markdown("<center><h1 style='color: white;'>🤖Right-Guide</h1></center>", unsafe_allow_html=True)

# # Background Image and Custom Styles
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('https://your-background-image-url.com');  /* Replace with your background image URL */
#         background-size: cover;
#         background-position: center;
#     }

#     /* Custom styles for chat messages */
#     .stChatMessage {
#         border-radius: 15px;
#         padding: 10px;
#         margin: 10px;
#         max-width: 70%;
#     }

#     /* Styling for user messages */
#     .stChatMessage.user {
#         background-color: #f0f0f0;
#         align-self: flex-start;
#     }

#     /* Styling for assistant messages */
#     .stChatMessage.assistant {
#         background-color: #e0e0e0;
#         align-self: flex-end;
#     }

#     /* Sidebar button custom style */
#     .stButton button {
#         background-color: #00bfae;
#         color: white;
#         border-radius: 8px;
#     }
    
#     .stButton button:hover {
#         background-color: #009d92;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True
# )

# Define avatars for users and bot
USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

# Simulated Bot Response function
def generate_response(user_input):
    # You can customize the bot's responses based on the user input
    if "hello" in user_input.lower():
        return "Bot: Hello there! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "Bot: I'm doing great, thanks for asking! How about you?"
    elif "bye" in user_input.lower():
        return "Bot: Goodbye! Have a great day ahead!"
    else:
        return f"Response: {user_input}"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar with option to clear chat history
with st.sidebar:
    if st.button("Clear Chat History"):
        st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Input from the user
user_input = st.chat_input("Ask me anything!")

# If the user submits a message
if user_input:
    # Add the user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show the user's message on the UI
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(user_input)
    
    # Generate the bot's response
    bot_response = generate_response(user_input)
    
    # Show the bot's response on the UI
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        st.markdown(bot_response)
    
    # Add the bot's response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
