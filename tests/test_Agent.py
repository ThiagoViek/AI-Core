import os
import sys
import pdb
import uuid
import yaml

sys.path.append("../")

from src.LLMresponse import LLMresponse
from AgentGraph import AgentGraph

def read_configs(filepath : str) -> dict:
    with open(filepath,'r') as file:
        return yaml.safe_load(file)

def read_key(filepath : str) -> str:
    with open(filepath,'r') as file:
        return file.read()

def main():
    # Load Configs
    configs : dict = read_configs("../configs.yaml")
    
    # Init Agent Planner
    graph : AgentGraph = AgentGraph()
    graph.setup(configs["tests"]["agent"])

    # Run inference
    user_id : str = uuid.uuid4()
    interaction : str = input("Enter your problem to be solved: ")
    graph.handle_ticket(user_id, interaction)

if __name__ == "__main__":
    main()