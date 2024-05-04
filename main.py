from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd
from dotenv import load_dotenv
import streamlit as st
from streamlit_chat import message
import uuid
from langchain.tools import tool


def ask(query):

    query_with_contex = """
    Consider that the team is included in the column Labels;
    Don't use the column Assegnee to retrieve the team;
    Consider that the single row can be called ECOM;
    Consider that state refers to column Status;
    Consider that Functional and Technical are determined by one of the values separated by a comma in the Labels field, so you need to check if Labels contains the value;
    Considera come valori technical e functional sempre minuscoli;
    ------------        
    {query}
    """
    file_name = "csv_dir/Jira_Issues_Simulation_Final_With_Dates.csv"
    query_with_contex = query_with_contex.format(query=query)
    df = pd.read_csv(file_name,sep="|")
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        df,
        verbose=True,
        return_intermediate_steps=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        max_iterations=10,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )
    response=agent.invoke(query_with_contex)
    return response
def console_main():

    #query=("Quante ECOM del team Buffon con stato In Progress e quante sono Technical")
    #query = ("La somma degli story point nelle ECOM del team Buffon con stato Done nel terzo sprint")
    #query = "La somma degli story point nelle ECOM del team Buffon con stato Done nel terzo sprint"
    query = "Quanti story point le ECOM in stato Done fino al 7 Febbraio del team Buffon con Reporter PO-Giulia"
    #query = "la lista dei team e quanti story point le loro ECOM in stato Done per i tre sprint"
    #query = "How many ECOM of Zola team in status Done and in Sprint 2?"
    #query = "Somma degli story point del Team Zola nel terzo sprint in stato Done"
    ##query = "gli url delle ECOM del team Baggio in terzo sprint    """
    #res=ask(query)
    res = ask(query)
    print(res)

def build_web_app():
    st.header("LangChain🦜🔗 Jira facilitator example")
    if (
            "chat_answers_history" not in st.session_state
            and "user_prompt_history" not in st.session_state
            and "chat_history" not in st.session_state
    ):
        st.session_state["chat_answers_history"] = []
        st.session_state["user_prompt_history"] = []
        st.session_state["chat_history"] = []

    prompt = st.text_input("Prompt", placeholder="Enter your message here...") or st.button(
        "Submit"
    )

    if prompt:
        with st.spinner("Generating response..."):
            generated_response = ask(prompt)

            st.session_state.chat_history.insert(0,(prompt, generated_response["output"]))
            st.session_state.user_prompt_history.insert(0,prompt)
            st.session_state.chat_answers_history.insert(0,generated_response['output'])

    if st.session_state["chat_answers_history"]:
        for generated_response, user_query in zip(
                st.session_state["chat_answers_history"],
                st.session_state["user_prompt_history"],
        ):
            message(
                user_query,
                is_user=True,
                key=str(uuid.uuid4())
            )
            message(
                generated_response,
                is_user=False,
                key=str(uuid.uuid4())
            )


if __name__ == '__main__':
    load_dotenv()
    console_main()
    #build_web_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
