import streamlit as st
import random

st.set_page_config(page_title="StudyBuddy", page_icon="🧠", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f7f7f7;
        padding: 20px;
        border-radius: 15px;
    }
    .block-container {
        padding-top: 2rem;
    }
    .stTextInput>div>div>input {
        border-radius: 8px;
        padding: 0.6rem;
        border: 1px solid #ccc;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 StudyBuddy")
st.caption("Your all-in-one AI study assistant — flashcards, summaries, and more.")

# Sidebar
with st.sidebar:
    st.header("📚 Tools")
    nav = st.radio("Select a feature:", ["💬 Chat", "📖 Flashcards", "📄 Summarize PDF (coming next!)"])

# Flashcards
flashcards = [
    {"question": "What is the powerhouse of the cell?", "answer": "mitochondria"},
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "Who developed the theory of relativity?", "answer": "einstein"},
    {"question": "What is 3 x 4?", "answer": "12"},
]

def flashcard_ui():
    st.subheader("📖 Flashcard Quiz")
    for card in flashcards:
        st.write(f"**Q:** {card['question']}")
        answer = st.text_input("Your answer:", key=card['question'])
        if answer:
            if answer.lower().strip() == card['answer']:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Answer: {card['answer']}")
            st.write("---")

def chat_ui():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("💬 Ask StudyBuddy anything:", key="chat_input")
    if user_input:
        responses = {
            "hi": "Hey! Ready to study? What topic do you need help with?",
            "help": "Try 'flashcards' or upload a PDF to summarize.",
            "bye": "Catch you later! Stay sharp.",
        }
        reply = responses.get(user_input.lower(), "I'm still learning. Try 'flashcards' or ask me about a topic!")
        st.session_state.chat_history.append((user_input, reply))

    for user, bot in st.session_state.chat_history:
        st.markdown(f"**You:** {user}")
        st.markdown(f"**StudyBuddy:** {bot}")

# Routing logic
if nav == "💬 Chat":
    chat_ui()
elif nav == "📖 Flashcards":
    flashcard_ui()
elif nav == "📄 Summarize PDF (coming next!)":
    st.info("🔧 PDF summarizer is coming up next...")
