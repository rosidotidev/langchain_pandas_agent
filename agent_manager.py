from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI, OpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd

QUERIES=[
    "Quante ECOM del team Buffon con stato In Progress e quante di queste sono Technical",
    "La somma degli story point nelle ECOM del team Buffon con stato Done nel terzo sprint",
    "La somma degli story point nelle ECOM del team Buffon con stato Done nel terzo sprint",
    "Quanti story point le ECOM in stato Done fino al 7 Febbraio del team Buffon con Reporter PO-Giulia",
    "la lista dei team e quanti story point le loro ECOM in stato Done per i tre sprint",
    """
    una tabella con: il nome del team, gli story point di tipo functional del team, gli story point di tipo technical del team, sprint
    esempio:
    Baggio   |Sprint 1| 34                   | 67
    Zola     |Sprint 1| 22                   | 34 
    """,
    "How many ECOM of Zola team in status Done and in Sprint 2?",
    "Somma degli story point del Team Zola nel terzo sprint in stato Done",
    "Somma degli story point delle ECOM functional, del Team Zola, nel terzo sprint, in stato Done",
    "gli url delle ECOM del team Baggio in terzo sprint    "

    ]

def getAgentExecutorChatOpenAI(df):
    prefix = """
           Use the column Team to retrieve the team;
           technical or functional refer to the column category;
           Consider that the single row can be called ECOM;
           Consider that state refers to column Status;
          """
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        df,
        prefix=prefix,
        verbose=True,
        return_intermediate_steps=True,
        #agent_type=AgentType.OPENAI_FUNCTIONS,
        agent_type="openai-tools",
        max_iterations=10,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )
    return agent