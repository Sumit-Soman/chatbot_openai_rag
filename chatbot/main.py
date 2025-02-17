import streamlit as st
from chatbot_init import Chatbot

def main():
    st.title("📚 Library Assistant OpenAI Chatbot")

    # Initialize the chatbot
    chatbot = Chatbot()

    # User input
    user_query = st.text_input("Ask about a Book name, genre, or author:")
    
    if st.button("Get Response"):
        if user_query:
            response, context = chatbot.generate_response(user_query)
            st.write("🤖 **Chatbot:**", response)
        else:
            st.warning("Please enter a question!")
    
    # Footer
    st.markdown("---")
    st.markdown("Built with ❤️ using LangChain, OpenAI, and Streamlit.")

if __name__ == "__main__":
    main()