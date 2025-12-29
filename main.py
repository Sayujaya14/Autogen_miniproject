from autogen import GroupChat, GroupChatManager
from agents import create_agents
import uuid

SESSION_ID = str(uuid.uuid4())

user, planner, writer, critic, researcher, architect = create_agents(SESSION_ID)
groupchat = GroupChat(
    agents=[user, planner, architect, researcher, critic, writer],
    messages=[],
    max_round=8
)

manager = GroupChatManager(
    groupchat=groupchat,
    system_message="""
You are managing a team of expert agents.
Ensure:
- Planner assigns tasks
- Specialists respond in their domain
- Writer produces the final answer
"""
)

user.initiate_chat(
    manager,
    message="Explain microservices vs monolithic architecture with real-world examples"
)
