from autogen import AssistantAgent, UserProxyAgent
from memory import save_message
from config import config_list

def create_agents(session_id):
    planner = AssistantAgent(
        name="Planner",
        system_message="""
    You are a task planner.
    Your job:
    - Understand the user question
    - Break it into clear sub-tasks
    - Decide which agent should handle each part
    - Do NOT give final answers
    """,
        llm_config={"config_list": config_list},
        is_termination_msg=lambda msg: (
            save_message(session_id, "Planner", msg["role"], msg["content"])
            or False
        )
    )

    architect = AssistantAgent(
        name="Architect",
        system_message="""
    You are a senior system architect.
    Your job:
    - Focus on system design and architecture
    - Compare approaches at a high level
    - Use diagrams-in-words if helpful
    - Avoid implementation details unless needed
    """,
        llm_config={"config_list": config_list},
        is_termination_msg=lambda msg: (
            save_message(session_id, "Architect", msg["role"], msg["content"])
            or False
        )
    )

    researcher = AssistantAgent(
        name="Researcher",
        system_message="""
    You are a technical researcher.
    Your job:
    - Provide real-world examples
    - Mention industry use-cases
    - Reference known systems or patterns
    - Avoid opinions, focus on facts
    """,
        llm_config={"config_list": config_list},
        is_termination_msg=lambda msg: (
            save_message(session_id, "Researcher", msg["role"], msg["content"])
            or False
        )
    )

    critic = AssistantAgent(
        name="Critic",
        system_message="""
    You are a critical reviewer.
    Your job:
    - Identify weaknesses, risks, and trade-offs
    - Point out when something may not scale
    - Question assumptions
    - Be constructive, not negative
    """,
        llm_config={"config_list": config_list},
        is_termination_msg=lambda msg: (
            save_message(session_id, "Critic", msg["role"], msg["content"])
            or False
        )
    )

    writer = AssistantAgent(
        name="Writer",
        system_message="""
    You are a technical writer.
    Your job:
    - Combine all agent inputs
    - Produce a clean, structured final answer
    - Use simple language
    - Make it suitable for blogs or interviews
    """,
        llm_config={"config_list": config_list},
        is_termination_msg=lambda msg: (
            save_message(session_id, "Writer", msg["role"], msg["content"])
            or False
        )
    )

    user = UserProxyAgent(
        name="User",
        human_input_mode="NEVER"
    )
    
    return user, planner, writer, critic, researcher, architect