import pdb

from src.LLM import LLM
from src.LLMresponse import LLMresponse
from src.InstructionReader import InstructionReader
from enums.ResponseFormat import ResponseFormat

class AgentPlanner:
    def __init__(self) -> None:
        # LLMs
        self._llm : LLM = None

        # Instruction Files
        self._instruction_query : InstructionReader = None
        self._instruction_contribution : InstructionReader = None

    def setup(self, configs : dict) -> None:
        self._llm = LLM()
        self._instruction = InstructionReader()

        self._llm.set_key(configs["llm"]["api-key-filepath"])
        self._llm.setup(configs["llm"]["model-specs"])
        self._instruction.setup_template_files(configs["instructions-query"])
        self._instruction.setup_template_files(configs["instructions-contributions"])

    def plan(self, task_dict : dict) -> dict:
        request : str = list(task_dict.keys())[0]
        task : str = task_dict[request]
        if request == "CONTRIBUTION":
            response : LLMresponse = LLMresponse()
            response.set_response(task,0,ResponseFormat.TEXT)
        if request == "QUERY":
            prompt : list = []
            sys_instruction_str : str = self._instruction.sys_instruction
            sys_instruction : dict = self._llm.queue_message("system",sys_instruction_str)
            prompt.append(sys_instruction)

            user_instruction_str : str = self._instruction.user_instruction
            user_instruction_str = user_instruction_str.replace("$interaction",task)
            user_instruction : dict = self._llm.queue_message("user",user_instruction_str)
            prompt.append(user_instruction)

            response : LLMresponse = self._llm.request(prompt,ResponseFormat.SLIST)
        return response