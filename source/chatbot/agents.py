from swarm import Agent
from .models import SystemInstructions

def get_agent(agent_name):
    agent_instructions = SystemInstructions.objects.get(name=agent_name).instructions
    
    # エージェント名と転送関数の対応を定義
    agent_transfer_functions = {
        "在庫管理システム": [transfer_to_agent_b, transfer_to_agent_c],
        "顧客関係管理システム": [transfer_to_agent_a, transfer_to_agent_c],
        "営業管理システム": [transfer_to_agent_a, transfer_to_agent_b]
    }
    
    transfer_functions = agent_transfer_functions.get(agent_name, [])
    
    return Agent(
        name=agent_name,
        instructions=agent_instructions,
        functions=transfer_functions,
        model="gpt-4o-mini"
    )

def run_agent(client, agent, messages):
    return client.run(
        agent=agent,
        messages=messages,
        context_variables={},
        model_override="gpt-4o-mini"
    )

def transfer_to_agent_a():
    print("システム担当者にエスカレーションします。")
    return get_agent("在庫管理システム")

def transfer_to_agent_b():
    print("システム担当者にエスカレーションします。")
    return get_agent("顧客関係管理システム")

def transfer_to_agent_c():
    print("システム担当者にエスカレーションします。")
    return get_agent("営業管理システム")