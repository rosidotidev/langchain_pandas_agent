from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI, OpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd
from dotenv import load_dotenv
def getAgentExecutorChatOpenAI(df):
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        df,
        verbose=True,
        return_intermediate_steps=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        max_iterations=10,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )
    return agent



def ask(query):
    query_with_contex = """
        Use the column Team to retrieve the team;
        technical or functional refer to the column category;
        Consider that the single row can be called ECOM;
        Consider that state refers to column Status;
        ------------ 
        {query}
        """
    file_name = "csv_dir/Jira_Issues_Simulation_Final_With_Dates.csv"
    query_with_contex = query_with_contex.format(query=query)
    df = pd.read_csv(file_name,sep="|")
    df['Category'] = df['Labels'].apply(lambda x: str(x).split(',')[0].strip() if ',' in str(x) else '')
    df['Team'] = df['Labels'].apply(lambda x: str(x).split(',')[1].strip() if ',' in str(x) else '')
    agent = getAgentExecutorChatOpenAI(df)
    response=agent.invoke(query_with_contex)
    return response
def console_main():

    #query=("Quante ECOM del team Buffon con stato In Progress e quante sono Technical")
    #query = ("La somma degli story point nelle ECOM del team Buffon con stato Done nel terzo sprint")
    #query = "La somma degli story point nelle ECOM del team Buffon con stato Done nel terzo sprint"
    #query = "Quanti story point le ECOM in stato Done fino al 7 Febbraio del team Buffon con Reporter PO-Giulia"
    #query = "la lista dei team e quanti story point le loro ECOM in stato Done per i tre sprint"
    query = """
    una tabella con: il nome del team, gli story point di tipo functional del team, gli story point di tipo technical del team, sprint"
    esempio:
    Baggio   |Sprint 1| 34                   | 67
    Zola     |Sprint 1| 22                   | 34 
    """
    #query = "How many ECOM of Zola team in status Done and in Sprint 2?"
    query = "Somma degli story point del Team Zola nel terzo sprint in stato Done"
    #query = "Somma degli story point delle ECOM functional, del Team Zola, nel terzo sprint, in stato Done"
    ##query = "gli url delle ECOM del team Baggio in terzo sprint    """
    #res=ask(query)
    res = ask(query)
    print(res)

if __name__ == '__main__':
    load_dotenv()
    console_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
