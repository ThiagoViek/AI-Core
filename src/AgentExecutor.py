import pdb

from src.LLM import LLM
from ExecutionMemory import ExecutionMemory
from ExecutionTooling import ExecutionTooling
from src.AgentPlan import AgentPlan
from src.LLMresponse import LLMresponse
from src.InstructionReader import InstructionReader
from enums.ResponseFormat import ResponseFormat

class AgentExecutor:
    def __init__(self) -> None:
        # TODO: Add Tooling
        # TODO: Add Memory
        self._llm : LLM = None
        self._tools : ExecutionTooling = None
        self._memory : ExecutionMemory = None
        self._instruction : InstructionReader = None

    def setup(self, configs : dict) -> None:
        self._llm = LLM()
        self._instruction = InstructionReader()

        self._llm.set_key(configs["llm"]["api-key-filepath"])
        self._llm.setup(configs["llm"]["model-specs"])
        self._instruction.setup_template_files(configs["instructions"])

        self._tools.setup(configs["tools"])
        self._memory.setup(configs["memory"])

    def execute(self, plan : AgentPlan) -> LLMresponse:
        type : str = plan.task_type
        task : str = plan.task_description
        steps : list[str] = plan.task_list

        if type == "CONTRIBUTION":
            # TODO: Check need for data from tools
            # TODO: Check need for data from memory
            # TODO: Execute
            pass
        elif type == "QUERY":
            # TODO: Check need for data from tools
            # TODO: Check need for data from memory
            # TODO: Execute
            pass
        else:
            raise ValueError(f"Unknown type: {type}")
        
        return LLMresponse