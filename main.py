from autogen import GroupChat, GroupChatManager
from agents import user, planner, researcher, critic, writer

groupchat = GroupChat(
    agents=[user, planner, researcher, critic, writer],
    messages=[],
    max_round=6
)

manager = GroupChatManager(groupchat=groupchat)

user.initiate_chat(
    manager,
    message="Explain microservices vs monolithic architecture with examples"
)
