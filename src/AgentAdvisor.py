import pdb

from src.LLM import LLM
from src.LLMresponse import LLMresponse
from src.InstructionReader import InstructionReader
from enums.ResponseFormat import ResponseFormat

class AgentAdvisor:
    def __init__(self) -> None:
        self._llm : LLM = None
        self._instruction : InstructionReader = None

    def setup(self, configs : dict) -> None:
        self._llm = LLM()
        self._instruction = InstructionReader()

        self._llm.set_key(configs["llm"]["api-key-filepath"])
        self._llm.setup(configs["llm"]["model-specs"])
        self._instruction.setup_template_files(configs["instructions"])

    def generate_interaction(self, interaction : str) -> LLMresponse:
        prompt : list[dict] = []
        sys_instruction_str : str = self._instruction.sys_instruction
        sys_instruction : dict = self._llm.queue_message("system",sys_instruction_str)
        prompt.append(sys_instruction)

        user_instruction_str : str = self._instruction.user_instruction
        user_instruction_str = user_instruction_str.replace("$message",interaction)
        user_instruction : dict = self._llm.queue_message("user",user_instruction_str)
        prompt.append(user_instruction)

        response : LLMresponse = self._llm.request(prompt,ResponseFormat.JSON)
        return response