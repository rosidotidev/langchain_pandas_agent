from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI, OpenAI

QUERIES=[
    "How many ECOM does the Buffon team have in \"in Progress\" status, and how many of them are Technical",
    "The sum of story points of the ECOM of Buffon's team with status equals to Done in the third sprint",
    """
    How much story points have the ECOM of Buffon's team, in status Done, with Reporter equals to PO-Giulia 
    before 7 February
    """,
    "Show the list of teams and how much story points in their ECOM with status equal to Done for the 3 sprints",
    "Show the list of teams and how much story points in their ECOM with status equal to Done, in sprint 1"
    """
    How much story points has Materazzi Team in first Sprint, and how much of them are functional, and how much of them are in Done status 
    """,
    "How many ECOM of Zola team in status Done and in Sprint 2?",
    "The URL of all ECOM of the Zola's team in the first sprint having status not equals to Done",


    ]

def getAgentExecutorChatOpenAI(df):
    prefix = """
           Use the column Team to retrieve the team;
           technical or functional refer to the column category;
           Consider that the single row can be called ECOM;
           Consider that state refers to column Status;
           The URL of an ECOM is https://robby.com/{Issue Key}, where {Issue Key} is the value of the column "Issue Key"
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