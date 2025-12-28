from autogen import AssistantAgent, UserProxyAgent
from config import config_list

planner = AssistantAgent(
    name="Planner",
    system_message="Break the task into clear steps.",
    llm_config={"config_list": config_list}
)

researcher = AssistantAgent(
    name="Researcher",
    system_message="Research the topic thoroughly.",
    llm_config={"config_list": config_list}
)

critic = AssistantAgent(
    name="Critic",
    system_message="Review for correctness and gaps.",
    llm_config={"config_list": config_list}
)

writer = AssistantAgent(
    name="Writer",
    system_message="Write a clear final answer.",
    llm_config={"config_list": config_list}
)

user = UserProxyAgent(
    name="User",
    human_input_mode="NEVER"
)
