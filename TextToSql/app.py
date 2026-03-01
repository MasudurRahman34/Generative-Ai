from dotenv import load_dotenv

load_dotenv()  ##load all environments
import streamlit as st
import os
import sqlite3

from langchain_openai import ChatOpenAI


##configure our api
@st.cache_resource
def load_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
    )


llm = load_llm()
##function to Load google gemini Model and Provider sqlquery as the response

# Create the client


# Function to get SQL from Gemini
def get_sql_from_question(question, prompt):
    full_prompt = prompt + f"\nQuestion: {question}\nSQL:"
    response = llm.invoke(full_prompt)
    return response.content.strip()


## function to retrieve query form the sql database


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows


prompt = """
    you are an expert in converting english questions to SQL query.
    the SQL Database has the name Student and has the following 
    columns -name, class, section and marks. \n\nFor example, \nExample 1-how many entries of records are present?
    then the SQL command with be something like this- SELECT COUNT(*) FROM Student;
    \nExample 2- Tell me all the students studying in class Nine? then the SQL command will be something like this- 
    SELECT * FROM Student Where class ="Nine";
    also the sql should not have ``` in the beginning or end and the sql word in the output.
    """


##streamlit app

st.set_page_config(page_title="GPT Text to SQL")
st.header("GPT-powered Text → SQL App")

question = st.text_input("Ask a question about the Student database:")
submit = st.button("Generate SQL & Run")

if submit and question:
    try:
        sql_query = get_sql_from_question(question, prompt)
        st.subheader("Generated SQL")
        st.code(sql_query)

        results = read_sql_query(sql_query, "student.db")

        st.subheader("Query Results")
        for row in results:
            st.write(row)

    except Exception as e:
        st.error(str(e))
