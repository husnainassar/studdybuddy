import streamlit as st
import random

# ----------------------------
# Flashcards
# ----------------------------
flashcards = [
    {"question": "What is the powerhouse of the cell?", "answer": "mitochondria"},
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "Who developed the theory of relativity?", "answer": "einstein"},
    {"question": "What is 3 x 4?", "answer": "12"},
]

# ----------------------------
# Response Logic (from main.py)
# ----------------------------
def get_response(user_input):
    responses = {
        "hi": "Hey! Ready to study? What topic do you need help with?",
        "help": "Try typing 'flashcards' or ask me a question.",
        "bye": "Catch you later! Stay sharp.",
    }
    return responses.get(user_input.lower(), "I'm still learning. Try 'flashcards' or ask for help.")

# ----------------------------
# Flashcard Quiz Mode
# ----------------------------
def run_flashcards():
    st.subheader("📚 Flashcard Quiz")
    random.shuffle(flashcards)
    for card in flashcards:
        st.write(f"❓ {card['question']}")
        user_answer = st.text_input("Your answer:", key=card['question'])
        if user_answer:
            if user_answer.lower().strip() == card['answer']:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Nope. Correct answer: {card['answer']}")
            st.write("---")

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("🤖 StudyBuddy – AI-Powered Study Assistant")
st.write("Type 'flashcards' to start a quiz or ask me anything!")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input Box
user_input = st.text_input("🧠 You:", key="chat_input")

# Logic
if user_input:
    if user_input.lower() == "flashcards":
        run_flashcards()
    else:
        bot_response = get_response(user_input)
        st.session_state.chat_history.append((user_input, bot_response))

# Show conversation
for user_msg, bot_msg in st.session_state.chat_history:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**StudyBuddy:** {bot_msg}")
