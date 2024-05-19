import pandas as pd
from dotenv import load_dotenv
from agent_manager import getAgentExecutorChatOpenAI, QUERIES
from df_manager import read_df

def ask(query):
    df= read_df()
    agent_executor = getAgentExecutorChatOpenAI(df)
    response=agent_executor.invoke(query)
    return response
def console_main():
    query=QUERIES[0]
    res = ask(query)
    print(res)

if __name__ == '__main__':
    load_dotenv()
    console_main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
