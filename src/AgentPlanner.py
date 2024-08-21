import pdb

from src.LLM import LLM
from src.LLMresponse import LLMresponse
from src.InstructionReader import InstructionReader
from enums.ResponseFormat import ResponseFormat

class AgentPlanner:
    def __init__(self) -> None:
        # LLMs
        self._llm : LLM = None
        # self._llm_reflection : LLM = None
        # self._llm_critic : LLM = None
        # self._llm_chain_of_thought : LLM = None
        # self._llm_goal_decomp : LLM = None

        # Instruction Files
        self._instruction : InstructionReader = None
        # self._instructions_reflection : InstructionReader = None
        # self._instructions_critic : InstructionReader = None
        # self._instructions_chain_of_thought : InstructionReader = None
        # self._instructions_goal_decomp : InstructionReader = None

    def setup(self, configs : dict) -> None:
        self._llm = LLM()
        self._instruction = InstructionReader()

        self._llm.set_key(configs["llm"]["api-key-filepath"])
        self._llm.setup(configs["llm"]["model-specs"])
        self._instruction.setup_template_files(configs["instructions"])

        # if "reflection" in configs:
        #     self._llm_reflection = LLM()
        #     self._instructions_reflection = InstructionReader()

        #     self._llm_reflection.set_key(configs["reflection"])
        #     self._llm_reflection.setup(configs["reflection"])
        #     self._instructions_reflection.setup_template_files(configs["reflection"])

        # if "critic" in configs:
        #     self._llm_critic = LLM()
        #     self._instructions_critic = InstructionReader()

        #     self._llm_critic.set_key(configs["critic"])
        #     self._llm_critic.setup(configs["critic"])
        #     self._instructions_critic.setup_template_files(configs["critic"])

        # if "chain-of-thought" in configs:
        #     self._llm_chain_of_thought = LLM()
        #     self._instructions_chain_of_thought = InstructionReader()

        #     self._llm_chain_of_thought.set_key(configs["chain-of-thought"])
        #     self._llm_chain_of_thought.setup(configs["chain-of-thought"])
        #     self._instructions_chain_of_thought.setup_template_files(configs["chain-of-thought"])

        # if "goal-decomposition" in configs:
        #     self._llm_goal_decomp = LLM()
        #     self._instructions_goal_decomp = InstructionReader()

        #     self._llm_goal_decomp.set_key(configs["goal-decomposition"])
        #     self._llm_goal_decomp.setup(configs["goal-decomposition"])
        #     self._instructions_goal_decomp.setup_template_files(configs["goal-decomposition"])

    def plan(self, interaction : str) -> LLMresponse:
        prompt : list[dict] = []
        sys_instruction_str : str = self._instruction.sys_instruction
        sys_instruction : dict = self._llm.queue_message("system",sys_instruction_str)
        prompt.append(sys_instruction)

        user_instruction_str : str = self._instruction.user_instruction
        user_instruction_str = user_instruction_str.replace("$interaction",interaction)
        user_instruction : dict = self._llm.queue_message("user",user_instruction_str)
        prompt.append(user_instruction)

        response : LLMresponse = self._llm.request(prompt,ResponseFormat.LIST)
        return response