import streamlit as st



def sidebar():
    st.sidebar.title("NLP Toolset")
    st.sidebar.write("Please choose a tool to use:")
    options = ['Populate Database', 'Train Chatbot Model']
    choice = st.sidebar.selectbox("Tool", options)
    
def main():
    st.title("NLP Toolset")
    st.write("This is a toolset for NLP tasks like population your databse, training a chatbot model, etc.")

    sidebar() 


if __name__ == "__main__":
    main()