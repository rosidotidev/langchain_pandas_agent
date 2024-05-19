from dotenv import load_dotenv
from agent_manager import getAgentExecutorChatOpenAI
from df_manager import read_df

def ask(query):
    df= read_df()
    agent_executor = getAgentExecutorChatOpenAI(df)
    response=agent_executor.invoke(query)
    return response

def start_web_app():
    from web_app import build_web_app
    build_web_app(ask=ask)


if __name__ == '__main__':
    load_dotenv()
    start_web_app()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
