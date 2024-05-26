import streamlit as st
from main_code import define_few_shot_db_chain



def main():
    st.title("LLM GenAI Sales Analysis")
    st.subheader("Exploring Insights with Natural Language Processing")

    question = st.text_input("Question: ")

    if question:
        chain = define_few_shot_db_chain()
        response = chain.run(question)

        st.header("Answer")
        st.write(response)

if __name__ == "__main__":
    main()
