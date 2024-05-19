from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI, OpenAI
from langchain.agents.agent_types import AgentType
import pandas as pd
def getAgentExecutorChatOpenAI(df):
    prefix = """
           Use the column Team to retrieve the team;
           technical or functional refer to the column category;
           Consider that the single row can be called ECOM;
           Consider that state refers to column Status;
          """
    suffix="""
    Answer showing also Python code you used to get the answer: this has to be the format
    Answer: <put here the summarized answer>
    Pandas code: <put here the python code used rto generate the answer>
    """
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
        #ChatOpenAI(temperature=0, model="gpt-4o"),
        df,
        prefix=prefix,
        #suffix=suffix,
        verbose=True,
        return_intermediate_steps=True,
        #agent_type=AgentType.OPENAI_FUNCTIONS,
        agent_type="openai-tools",
        max_iterations=10,
        agent_executor_kwargs={"handle_parsing_errors": True}
    )
    return agent