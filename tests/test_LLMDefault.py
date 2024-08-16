import sys
import pdb
import yaml

sys.path.append("../")
from entities.llm.LLMdefault import LLMDefault
from entities.llm.LLMresponse import LLMresponse

def read_configs(filepath : str) -> dict:
    with open(filepath,'r') as file:
        return yaml.safe_load(file)

def read_key(filepath : str) -> str:
    with open(filepath,'r') as file:
        return file.read()

if __name__ == "__main__":
    # Load Configs
    openai_key : str = read_key("../.key")
    configs : dict = read_configs("../configs.yaml")
    
    # Init LLM
    llm = LLMDefault()
    llm.set_key(openai_key)
    llm.setup(configs)

    # Run Inference
    prompt : list = []

    sys_instruction : str = "Given a number, return me the sum of this number plus 10."
    prompt.append(llm.queue_message("system",sys_instruction))

    user_instruction : str = "3"
    prompt.append(llm.queue_message("user",user_instruction))

    response : LLMresponse = llm.request(prompt)
    print(response)