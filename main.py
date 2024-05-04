from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd
from dotenv import load_dotenv
import uuid

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

if __name__ == '__main__':
    load_dotenv()
    console_main()
    #build_web_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
