import os
import sys
import pdb
import yaml

sys.path.append("../")

from src.LLMresponse import LLMresponse
from src.AgentInterpreter import AgentInterpreter

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
    interpreter : AgentInterpreter = AgentInterpreter()
    interpreter.setup(configs["tests"]["interpreter"])

    # Run inference
    interaction : str = input("Enter your problem to be planned: ")
    response : LLMresponse = interpreter.interpret(interaction)
    print(response)

if __name__ == "__main__":
    main()